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
        
        conn.commit()
        conn.close()
    
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
        
        # Проверяем, не выполнено ли уже
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


class User(UserMixin):
    """
    Класс пользователя для Flask-Login.
    """
    
    def __init__(self, user_data):
        self.id = user_data["id"]
        self.username = user_data["username"]
        self.email = user_data["email"]
        self.points = user_data["points"]
        self.created_at = user_data["created_at"]
    
    def get_id(self):
        return str(self.id)