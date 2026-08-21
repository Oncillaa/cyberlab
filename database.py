#!/usr/bin/env python3
"""
Модуль для работы с базой данных CyberLab
Автор: Oncilla (https://github.com/Oncillaa)
"""

import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Database:
    """
    Класс для работы с SQLite базой данных.
    """
    
    def __init__(self, db_path="instance/cyberlab.db"):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        """Создаёт новое соединение с БД."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Инициализирует все таблицы в базе данных."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Таблица пользователей
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                points INTEGER DEFAULT 0,
                is_admin INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP
            )
        """)
        
        # Таблица завершённых заданий
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS completed_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                room_id TEXT NOT NULL,
                task_id TEXT NOT NULL,
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id),
                UNIQUE(user_id, room_id, task_id)
            )
        """)
        
        # Таблица для отслеживания попыток
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                room_id TEXT NOT NULL,
                task_id TEXT NOT NULL,
                answer TEXT NOT NULL,
                is_correct INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        
        # Проверяем, есть ли колонка is_admin (для старых баз данных)
        cursor.execute("PRAGMA table_info(users)")
        columns = [col[1] for col in cursor.fetchall()]
        if 'is_admin' not in columns:
            cursor.execute("ALTER TABLE users ADD COLUMN is_admin INTEGER DEFAULT 0")
        
        conn.commit()
        conn.close()
    
    # === МЕТОДЫ ДЛЯ ПОЛЬЗОВАТЕЛЕЙ ===
    
    def create_user(self, username, email, password):
        """
        Создаёт нового пользователя.
        Возвращает (success, message).
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            password_hash = generate_password_hash(password)
            cursor.execute(
                "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                (username, email, password_hash)
            )
            conn.commit()
            return (True, "Пользователь создан")
        except sqlite3.IntegrityError:
            return (False, "Пользователь с таким именем или email уже существует")
        except Exception as e:
            return (False, f"Ошибка: {e}")
        finally:
            conn.close()
    
    def get_user_by_username(self, username):
        """Возвращает пользователя по имени."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        return user
    
    def get_user_by_id(self, user_id):
        """Возвращает пользователя по ID."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user
    
    def get_user_by_email(self, email):
        """Возвращает пользователя по email."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()
        return user
    
    def verify_password(self, username, password):
        """Проверяет пароль пользователя."""
        user = self.get_user_by_username(username)
        if user and check_password_hash(user["password_hash"], password):
            return user
        return None
    
    def update_last_login(self, user_id):
        """Обновляет время последнего входа."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET last_login = ? WHERE id = ?",
            (datetime.now().isoformat(), user_id)
        )
        conn.commit()
        conn.close()
    
    def add_points(self, user_id, points):
        """Добавляет очки пользователю."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET points = points + ? WHERE id = ?",
            (points, user_id)
        )
        conn.commit()
        conn.close()
    
    def mark_task_completed(self, user_id, room_id, task_id):
        """
        Отмечает задание как выполненное.
        Возвращает True, если задание ещё не было выполнено.
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT id FROM completed_tasks WHERE user_id = ? AND room_id = ? AND task_id = ?",
            (user_id, room_id, task_id)
        )
        existing = cursor.fetchone()
        
        if existing:
            conn.close()
            return False
        
        cursor.execute(
            "INSERT INTO completed_tasks (user_id, room_id, task_id) VALUES (?, ?, ?)",
            (user_id, room_id, task_id)
        )
        conn.commit()
        conn.close()
        return True
    
    def get_completed_tasks(self, user_id):
        """Возвращает список выполненных заданий пользователя."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT room_id, task_id FROM completed_tasks WHERE user_id = ?",
            (user_id,)
        )
        tasks = cursor.fetchall()
        conn.close()
        return [(t["room_id"], t["task_id"]) for t in tasks]
    
    def log_attempt(self, user_id, room_id, task_id, answer, is_correct):
        """Записывает попытку ответа."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO attempts (user_id, room_id, task_id, answer, is_correct) VALUES (?, ?, ?, ?, ?)",
            (user_id, room_id, task_id, answer, is_correct)
        )
        conn.commit()
        conn.close()
    
    def get_leaderboard(self, limit=10):
        """Возвращает таблицу лидеров."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT username, points, created_at FROM users ORDER BY points DESC LIMIT ?",
            (limit,)
        )
        leaders = cursor.fetchall()
        conn.close()
        return leaders
    
    def get_user_stats(self, user_id):
        """Возвращает статистику пользователя."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) as count FROM completed_tasks WHERE user_id = ?", (user_id,))
        completed = cursor.fetchone()["count"]
        
        cursor.execute("SELECT COUNT(*) as count FROM attempts WHERE user_id = ?", (user_id,))
        attempts = cursor.fetchone()["count"]
        
        cursor.execute(
            "SELECT COUNT(*) as count FROM attempts WHERE user_id = ? AND is_correct = 1",
            (user_id,)
        )
        correct = cursor.fetchone()["count"]
        
        conn.close()
        
        accuracy = (correct / attempts * 100) if attempts > 0 else 0
        
        return {
            "completed_tasks": completed,
            "total_attempts": attempts,
            "correct_attempts": correct,
            "accuracy": round(accuracy, 1)
        }
    
    # === МЕТОДЫ ДЛЯ БЕЙДЖЕЙ И УРОВНЕЙ ===
    
    def get_user_badges(self, user_id):
        """Возвращает бейджи пользователя на основе его статистики."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT points FROM users WHERE id = ?", (user_id,))
        user_row = cursor.fetchone()
        points = user_row["points"] if user_row else 0
        
        cursor.execute("SELECT COUNT(*) as count FROM completed_tasks WHERE user_id = ?", (user_id,))
        completed = cursor.fetchone()["count"]
        
        cursor.execute("SELECT COUNT(DISTINCT room_id) as count FROM completed_tasks WHERE user_id = ?", (user_id,))
        rooms_count = cursor.fetchone()["count"]
        
        conn.close()
        
        badges = []
        
        # Бейджи за очки
        if points >= 10:
            badges.append({"icon": "🌱", "name": "Новичок", "description": "Набрал 10 очков"})
        if points >= 50:
            badges.append({"icon": "📚", "name": "Ученик", "description": "Набрал 50 очков"})
        if points >= 100:
            badges.append({"icon": "⚔️", "name": "Практик", "description": "Набрал 100 очков"})
        if points >= 300:
            badges.append({"icon": "🛡", "name": "Специалист", "description": "Набрал 300 очков"})
        if points >= 500:
            badges.append({"icon": "👑", "name": "Мастер", "description": "Набрал 500 очков"})
        if points >= 1000:
            badges.append({"icon": "🔥", "name": "Легенда", "description": "Набрал 1000 очков"})
        
        # Бейджи за задания
        if completed >= 1:
            badges.append({"icon": "✅", "name": "Первое задание", "description": "Выполнил первое задание"})
        if completed >= 5:
            badges.append({"icon": "📝", "name": "Старательный", "description": "Выполнил 5 заданий"})
        if completed >= 10:
            badges.append({"icon": "💪", "name": "Упорный", "description": "Выполнил 10 заданий"})
        if completed >= 20:
            badges.append({"icon": "🚀", "name": "Прогрессивный", "description": "Выполнил 20 заданий"})
        if completed >= 30:
            badges.append({"icon": "🏆", "name": "Чемпион", "description": "Выполнил 30 заданий"})
        
        # Бейджи за комнаты
        if rooms_count >= 1:
            badges.append({"icon": "🏠", "name": "Исследователь", "description": "Начал первую комнату"})
        if rooms_count >= 3:
            badges.append({"icon": "🗺", "name": "Путешественник", "description": "Прошёл 3 комнаты"})
        if rooms_count >= 5:
            badges.append({"icon": "🌍", "name": "Покоритель", "description": "Прошёл 5 комнат"})
        if rooms_count >= 8:
            badges.append({"icon": "🌟", "name": "Звезда", "description": "Прошёл 8 комнат"})
        
        return badges
    
    def get_user_level(self, user_id):
        """Возвращает уровень пользователя на основе очков."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT points FROM users WHERE id = ?", (user_id,))
        user_row = cursor.fetchone()
        points = user_row["points"] if user_row else 0
        conn.close()
        
        levels = [
            (0, "Новичок", "🌱"),
            (10, "Ученик", "📚"),
            (50, "Практик", "⚔️"),
            (100, "Специалист", "🛡"),
            (300, "Мастер", "👑"),
            (500, "Эксперт", "🔥"),
            (1000, "Легенда", "💎")
        ]
        
        current_level = levels[0]
        next_level = None
        
        for i, (threshold, name, icon) in enumerate(levels):
            if points >= threshold:
                current_level = (threshold, name, icon)
                if i + 1 < len(levels):
                    next_level = levels[i + 1]
            else:
                break
        
        if next_level:
            progress = ((points - current_level[0]) / (next_level[0] - current_level[0])) * 100
        else:
            progress = 100
        
        return {
            "icon": current_level[2],
            "name": current_level[1],
            "points": points,
            "next_level": next_level[1] if next_level else "Максимум",
            "next_points": next_level[0] if next_level else points,
            "progress": round(progress)
        }
    
    # === МЕТОДЫ ДЛЯ АДМИН-ПАНЕЛИ ===
    
    def is_admin(self, user_id):
        """Проверяет, является ли пользователь администратором."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT is_admin FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result["is_admin"] == 1 if result else False
    
    def set_admin(self, user_id, is_admin=True):
        """Устанавливает или снимает права администратора."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET is_admin = ? WHERE id = ?",
            (1 if is_admin else 0, user_id)
        )
        conn.commit()
        conn.close()
    
    def get_all_users(self):
        """Возвращает всех пользователей для админ-панели."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.id, u.username, u.email, u.points, u.is_admin, u.created_at,
                   (SELECT COUNT(*) FROM completed_tasks ct WHERE ct.user_id = u.id) as tasks_completed
            FROM users u
            ORDER BY u.points DESC
        """)
        users = cursor.fetchall()
        conn.close()
        return users
    
    def delete_user(self, user_id):
        """Удаляет пользователя и все его данные."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM completed_tasks WHERE user_id = ?", (user_id,))
        cursor.execute("DELETE FROM attempts WHERE user_id = ?", (user_id,))
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
    
    def get_platform_stats(self):
        """Возвращает общую статистику платформы."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) as count FROM users")
        total_users = cursor.fetchone()["count"]
        
        cursor.execute("SELECT COUNT(*) as count FROM completed_tasks")
        total_completed = cursor.fetchone()["count"]
        
        cursor.execute("SELECT COUNT(*) as count FROM attempts")
        total_attempts = cursor.fetchone()["count"]
        
        cursor.execute("SELECT COALESCE(SUM(points), 0) as sum FROM users")
        total_points = cursor.fetchone()["sum"]
        
        conn.close()
        
        return {
            "total_users": total_users,
            "total_completed_tasks": total_completed,
            "total_attempts": total_attempts,
            "total_points": total_points
        }


class User(UserMixin):
    """
    Класс пользователя для Flask-Login.
    """
    
    def __init__(self, user_data):
        self.id = user_data["id"]
        self.username = user_data["username"]
        self.email = user_data["email"]
        self.points = user_data["points"]
        self.is_admin = user_data["is_admin"] if "is_admin" in user_data.keys() else 0
        self.created_at = user_data["created_at"]
    
    def get_id(self):
        return str(self.id)