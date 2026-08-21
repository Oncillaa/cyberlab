#!/usr/bin/env python3
"""
CyberLab - платформа для обучения кибербезопасности
Автор: Oncilla (https://github.com/Oncillaa)
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import Database, User
from rooms_data import get_all_rooms, get_room, get_total_points
from translations import get_translations, get_text
from ctf_files import list_ctf_files, get_ctf_file_path, generate_all_demo_files
from vm_manager import VMManager
from learning_data import get_all_categories, get_category, get_articles_by_category, get_article
from functools import wraps
import secrets
import markdown


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)

db = Database()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Пожалуйста, войдите для доступа к этой странице.'
login_manager.login_message_category = 'error'


@login_manager.user_loader
def load_user(user_id):
    user_data = db.get_user_by_id(int(user_id))
    if user_data:
        return User(dict(user_data))
    return None


def api_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return jsonify({"error": "Требуется авторизация"}), 401
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        if not db.is_admin(current_user.id):
            flash('Доступ запрещён. Требуются права администратора.', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


# === ЯЗЫКОВАЯ ПОДДЕРЖКА ===

def get_current_lang():
    if 'lang' in session:
        return session['lang']
    return 'ru'


@app.context_processor
def inject_translations():
    lang = get_current_lang()
    return {
        't': get_translations(lang),
        'lang': lang
    }


@app.route('/set_lang/<lang>')
def set_lang(lang):
    if lang in ['ru', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('index'))


# === МАРШРУТЫ ===

@app.route('/')
def index():
    rooms = get_all_rooms()
    completed_tasks = []
    if current_user.is_authenticated:
        completed_tasks = db.get_completed_tasks(current_user.id)
    
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
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
        
        success, message = db.create_user(username, email, password)
        
        if success:
            flash('Регистрация успешна! Теперь войдите в систему.', 'success')
            return redirect(url_for('login'))
        else:
            flash(message, 'error')
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
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
    logout_user()
    flash('Вы вышли из системы', 'success')
    return redirect(url_for('index'))


@app.route('/rooms')
def rooms():
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
    room_data = get_room(room_id)
    if not room_data:
        flash('Комната не найдена', 'error')
        return redirect(url_for('rooms'))
    
    completed_tasks = db.get_completed_tasks(current_user.id)
    completed_in_room = [task_id for r_id, task_id in completed_tasks if r_id == room_id]
    
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
    data = request.get_json()
    room_id = data.get('room_id')
    task_id = data.get('task_id')
    answer = data.get('answer', '').strip().lower()
    
    if not room_id or not task_id:
        return jsonify({"correct": False, "message": "Недостаточно данных"})
    
    room_data = get_room(room_id)
    if not room_data:
        return jsonify({"correct": False, "message": "Комната не найдена"})
    
    task = None
    for t in room_data["tasks"]:
        if t["id"] == task_id:
            task = t
            break
    
    if not task:
        return jsonify({"correct": False, "message": "Задание не найдено"})
    
    correct_answer = task["answer"].lower()
    is_correct = answer == correct_answer
    
    db.log_attempt(current_user.id, room_id, task_id, answer, 1 if is_correct else 0)
    
    if is_correct:
        if db.mark_task_completed(current_user.id, room_id, task_id):
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
    leaders = db.get_leaderboard(20)
    return render_template('leaderboard.html', leaders=leaders)


@app.route('/profile')
@login_required
def profile():
    stats = db.get_user_stats(current_user.id)
    completed_tasks = db.get_completed_tasks(current_user.id)
    badges = db.get_user_badges(current_user.id)
    level = db.get_user_level(current_user.id)
    
    return render_template(
        'profile.html',
        stats=stats,
        completed_tasks_count=len(completed_tasks),
        badges=badges,
        level=level
    )


# === АДМИН-ПАНЕЛЬ ===

@app.route('/admin')
@admin_required
def admin_panel():
    stats = db.get_platform_stats()
    users = db.get_all_users()
    return render_template('admin.html', stats=stats, users=users)


@app.route('/admin/delete_user/<int:user_id>', methods=['POST'])
@admin_required
def admin_delete_user(user_id):
    if user_id == current_user.id:
        flash('Нельзя удалить самого себя', 'error')
        return redirect(url_for('admin_panel'))
    
    db.delete_user(user_id)
    flash(f'Пользователь #{user_id} удалён', 'success')
    return redirect(url_for('admin_panel'))


@app.route('/admin/toggle_admin/<int:user_id>', methods=['POST'])
@admin_required
def admin_toggle_admin(user_id):
    if user_id == current_user.id:
        flash('Нельзя изменить свои права', 'error')
        return redirect(url_for('admin_panel'))
    
    user = db.get_user_by_id(user_id)
    if user:
        new_status = not (user["is_admin"] == 1)
        db.set_admin(user_id, new_status)
        status_text = "назначен администратором" if new_status else "снят с администратора"
        flash(f'Пользователь #{user_id} {status_text}', 'success')
    
    return redirect(url_for('admin_panel'))


# === CTF ФАЙЛЫ ===

@app.route('/ctf/files')
@login_required
def ctf_files_list():
    files = list_ctf_files()
    return render_template('ctf_files.html', files=files)


@app.route('/ctf/download/<filename>')
@login_required
def ctf_download(filename):
    filepath = get_ctf_file_path(filename)
    if filepath:
        return send_file(filepath, as_attachment=True)
    flash('Файл не найден', 'error')
    return redirect(url_for('ctf_files_list'))


@app.route('/ctf/generate')
@admin_required
def ctf_generate():
    generate_all_demo_files()
    flash('Демо-файлы созданы!', 'success')
    return redirect(url_for('ctf_files_list'))


# === ВИРТУАЛЬНЫЕ МАШИНЫ ===

@app.route('/vms')
@login_required
def vms_list():
    docker_available = VMManager.check_docker()
    vms = VMManager.get_vm_list_with_status()
    return render_template('vms.html', vms=vms, docker_available=docker_available)


@app.route('/vms/start/<vm_id>', methods=['POST'])
@admin_required
def vm_start(vm_id):
    success, message = VMManager.start_container(vm_id)
    flash(message, 'success' if success else 'error')
    return redirect(url_for('vms_list'))


@app.route('/vms/stop/<vm_id>', methods=['POST'])
@admin_required
def vm_stop(vm_id):
    success, message = VMManager.stop_container(vm_id)
    flash(message, 'success' if success else 'error')
    return redirect(url_for('vms_list'))


# === ОБУЧЕНИЕ ===

@app.route('/learn')
def learn():
    categories = get_all_categories()
    return render_template('learn.html', categories=categories)


@app.route('/learn/<category_id>')
def learn_category(category_id):
    category = get_category(category_id)
    if not category:
        flash('Категория не найдена', 'error')
        return redirect(url_for('learn'))
    
    articles = get_articles_by_category(category_id)
    return render_template('learn_category.html', category=category, articles=articles)


@app.route('/learn/<category_id>/<article_id>')
def learn_article(category_id, article_id):
    article = get_article(article_id)
    if not article or article["category"] != category_id:
        flash('Статья не найдена', 'error')
        return redirect(url_for('learn'))
    
    content_html = markdown.markdown(article["content"], extensions=['tables', 'fenced_code'])
    
    return render_template('learn_article.html', article=article, content_html=content_html)


# === ОБРАБОТКА ОШИБОК ===

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


# === ЗАПУСК ===

if __name__ == '__main__':
    if not os.path.exists('instance'):
        os.makedirs('instance')
    
    if not os.path.exists('ctf_files'):
        os.makedirs('ctf_files')
    
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)