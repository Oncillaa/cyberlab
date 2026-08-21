#!/usr/bin/env python3
"""
CyberLab - платформа для обучения кибербезопасности
Автор: Oncilla (https://github.com/Oncillaa)
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import Database, User
from rooms_data import get_all_rooms, get_room, get_total_points
from functools import wraps
import secrets


# Инициализация приложения
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)

# Инициализация базы данных
db = Database()

# Инициализация Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Пожалуйста, войдите для доступа к этой странице.'
login_manager.login_message_category = 'error'


@login_manager.user_loader
def load_user(user_id):
    """Загружает пользователя по ID для Flask-Login."""
    user_data = db.get_user_by_id(int(user_id))
    if user_data:
        return User(dict(user_data))
    return None


# Декоратор для проверки авторизации через API
def api_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return jsonify({"error": "Требуется авторизация"}), 401
        return f(*args, **kwargs)
    return decorated_function


# === МАРШРУТЫ ===

@app.route('/')
def index():
    """Главная страница."""
    rooms = get_all_rooms()
    
    # Если пользователь авторизован, получаем его прогресс
    completed_tasks = []
    if current_user.is_authenticated:
        completed_tasks = db.get_completed_tasks(current_user.id)
    
    # Считаем прогресс для каждой комнаты
    rooms_with_progress = []
    for room in rooms:
        total_tasks = len(room["tasks"])
        completed_count = sum(1 for ct in completed_tasks if ct[0] == room["id"])
        progress = (completed_count / total_tasks * 100) if total_tasks > 0 else 0
        rooms_with_progress.append({
            **room,
            "progress": round(progress),
            "completed_tasks": completed_count,
            "total_tasks": total_tasks
        })
    
    return render_template('index.html', rooms=rooms_with_progress)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Регистрация нового пользователя."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        # Валидация
        if not username or not email or not password:
            flash('Все поля обязательны для заполнения', 'error')
            return render_template('register.html')
        
        if len(username) < 3:
            flash('Имя пользователя должно быть не менее 3 символов', 'error')
            return render_template('register.html')
        
        if len(password) < 6:
            flash('Пароль должен быть не менее 6 символов', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Пароли не совпадают', 'error')
            return render_template('register.html')
        
        if '@' not in email or '.' not in email:
            flash('Введите корректный email', 'error')
            return render_template('register.html')
        
        # Создаём пользователя
        success, message = db.create_user(username, email, password)
        
        if success:
            flash('Регистрация успешна! Теперь войдите в систему.', 'success')
            return redirect(url_for('login'))
        else:
            flash(message, 'error')
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Вход в систему."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember') == 'on'
        
        user_data = db.verify_password(username, password)
        
        if user_data:
            user = User(dict(user_data))
            login_user(user, remember=remember)
            db.update_last_login(user.id)
            flash(f'Добро пожаловать, {username}!', 'success')
            
            # Перенаправляем на страницу, с которой пришли
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for('index'))
        else:
            flash('Неверное имя пользователя или пароль', 'error')
    
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    """Выход из системы."""
    logout_user()
    flash('Вы вышли из системы', 'success')
    return redirect(url_for('index'))


@app.route('/rooms')
def rooms():
    """Список всех комнат."""
    all_rooms = get_all_rooms()
    
    completed_tasks = []
    if current_user.is_authenticated:
        completed_tasks = db.get_completed_tasks(current_user.id)
    
    rooms_with_progress = []
    for room in all_rooms:
        total_tasks = len(room["tasks"])
        completed_count = sum(1 for ct in completed_tasks if ct[0] == room["id"])
        progress = (completed_count / total_tasks * 100) if total_tasks > 0 else 0
        rooms_with_progress.append({
            **room,
            "progress": round(progress),
            "completed_tasks": completed_count,
            "total_tasks": total_tasks
        })
    
    return render_template('rooms.html', rooms=rooms_with_progress)


@app.route('/room/<room_id>')
@login_required
def room(room_id):
    """Страница комнаты с заданиями."""
    room_data = get_room(room_id)
    if not room_data:
        flash('Комната не найдена', 'error')
        return redirect(url_for('rooms'))
    
    completed_tasks = db.get_completed_tasks(current_user.id)
    completed_in_room = [task_id for r_id, task_id in completed_tasks if r_id == room_id]
    
    # Добавляем статус выполнения к заданиям
    tasks_with_status = []
    for task in room_data["tasks"]:
        is_completed = task["id"] in completed_in_room
        tasks_with_status.append({
            **task,
            "completed": is_completed
        })
    
    total_tasks = len(room_data["tasks"])
    completed_count = len(completed_in_room)
    progress = (completed_count / total_tasks * 100) if total_tasks > 0 else 0
    
    return render_template(
        'room.html',
        room=room_data,
        tasks=tasks_with_status,
        progress=round(progress),
        completed_count=completed_count,
        total_tasks=total_tasks,
        total_points=get_total_points(room_id)
    )


@app.route('/api/check_answer', methods=['POST'])
@api_login_required
def check_answer():
    """Проверяет ответ на задание."""
    data = request.get_json()
    
    room_id = data.get('room_id')
    task_id = data.get('task_id')
    answer = data.get('answer', '').strip().lower()
    
    if not room_id or not task_id:
        return jsonify({"correct": False, "message": "Недостаточно данных"})
    
    room_data = get_room(room_id)
    if not room_data:
        return jsonify({"correct": False, "message": "Комната не найдена"})
    
    # Ищем задание
    task = None
    for t in room_data["tasks"]:
        if t["id"] == task_id:
            task = t
            break
    
    if not task:
        return jsonify({"correct": False, "message": "Задание не найдено"})
    
    # Проверяем ответ
    correct_answer = task["answer"].lower()
    is_correct = answer == correct_answer
    
    # Логируем попытку
    db.log_attempt(current_user.id, room_id, task_id, answer, 1 if is_correct else 0)
    
    if is_correct:
        # Проверяем, не выполнено ли уже
        if db.mark_task_completed(current_user.id, room_id, task_id):
            # Начисляем очки
            db.add_points(current_user.id, task["points"])
            return jsonify({
                "correct": True,
                "message": f"Правильно! +{task['points']} очков!",
                "points_awarded": task["points"]
            })
        else:
            return jsonify({
                "correct": True,
                "message": "Задание уже было выполнено!",
                "points_awarded": 0
            })
    else:
        return jsonify({
            "correct": False,
            "message": "Неправильный ответ. Попробуй ещё раз!"
        })


@app.route('/api/get_hint', methods=['POST'])
@api_login_required
def get_hint():
    """Возвращает подсказку для задания."""
    data = request.get_json()
    
    room_id = data.get('room_id')
    task_id = data.get('task_id')
    
    room_data = get_room(room_id)
    if not room_data:
        return jsonify({"hint": "Комната не найдена"})
    
    task = None
    for t in room_data["tasks"]:
        if t["id"] == task_id:
            task = t
            break
    
    if not task:
        return jsonify({"hint": "Задание не найдено"})
    
    return jsonify({"hint": task.get("hint", "Подсказка недоступна")})


@app.route('/leaderboard')
def leaderboard():
    """Таблица лидеров."""
    leaders = db.get_leaderboard(20)
    return render_template('leaderboard.html', leaders=leaders)


@app.route('/profile')
@login_required
def profile():
    """Профиль пользователя."""
    stats = db.get_user_stats(current_user.id)
    completed_tasks = db.get_completed_tasks(current_user.id)
    
    return render_template(
        'profile.html',
        stats=stats,
        completed_tasks_count=len(completed_tasks)
    )


# === ОБРАБОТКА ОШИБОК ===

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


# === ЗАПУСК ===

if __name__ == '__main__':
    # Создаём папку instance, если её нет
    if not os.path.exists('instance'):
        os.makedirs('instance')
    
    # Запускаем приложение
    # use_reloader=False отключает watchdog, который вызывает перезагрузку
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)