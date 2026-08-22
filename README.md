# 🔐 CyberLab — Платформа обучения кибербезопасности

![Version](https://img.shields.io/badge/Version-1.5-blue.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**CyberLab** — интерактивная веб-платформа для изучения кибербезопасности в стиле TryHackMe. Решай задания, читай статьи, практикуйся на виртуальных машинах!

---

## ✨ Возможности

### 📚 Обучение
- 8 категорий: основы, криптография, веб, сети, Linux, стеганография, RE, OSINT
- 26+ статей с командами для Linux и Windows
- Кнопки копирования команд в один клик
- Markdown-рендеринг с таблицами и блоками кода

### 🎯 Комнаты
- 9 тематических комнат
- 63 задания разной сложности
- Система очков и подсказок
- Прогресс выполнения

### 👤 Пользователи
- Регистрация и авторизация
- Бейджи за достижения
- Уровни и опыт
- Таблица лидеров

### 👑 Админ-панель
- Управление пользователями
- Назначение администраторов
- Статистика платформы

### 📁 CTF-файлы
- Генерация демо-файлов
- Base64, Hex, ROT13, бинарные файлы
- Скачивание для анализа

### 🐳 Виртуальные машины
- DVWA, Juice Shop, WebGoat
- Docker-контейнеры
- Запуск/остановка через веб

### 🌐 Дополнительно
- Мультиязычность (RU/EN)
- Тёмная тема
- Адаптивный дизайн
- Всплывающие уведомления

---

## 🚀 Быстрый старт

\`\`\`bash
# Клонируем
git clone https://github.com/Oncillaa/cyberlab.git
cd cyberlab

# Устанавливаем
pip install -r requirements.txt

# Запускаем
python app.py
\`\`\`

Открой: **http://127.0.0.1:5000**

---

## 📁 Структура

\`\`\`
cyberlab/
├── app.py              # Основное приложение
├── database.py         # База данных
├── rooms_data.py       # Комнаты и задания
├── learning_data.py    # Статьи обучения
├── translations.py     # Переводы RU/EN
├── ctf_files.py        # Генератор CTF
├── vm_manager.py       # Docker VM
├── static/
│   ├── style.css       # Стили
│   └── favicon.svg
├── templates/          # HTML-шаблоны
└── requirements.txt
\`\`\`

---

## 🎯 Как стать админом

\`\`\`bash
python -c "from database import Database; db = Database(); conn = db.get_connection(); cursor = conn.cursor(); cursor.execute('UPDATE users SET is_admin = 1 WHERE username = ?', ('ТВОЙ_ЛОГИН',)); conn.commit(); conn.close(); print('Готово!')"
\`\`\`

---

## 🛠 Технологии

| Технология | Назначение |
|------------|------------|
| Python 3.11 | Язык |
| Flask 3.1 | Веб-фреймворк |
| SQLite | База данных |
| Markdown | Рендеринг статей |
| Docker | Виртуальные машины |

---

## 👤 Автор

**Oncilla**
- GitHub: [@Oncillaa](https://github.com/Oncillaa)
- Email: graevartem0@gmail.com

---

## 📄 Лицензия

MIT License

---

## ⚠️ Дисклеймер

Проект создан исключительно в образовательных целях.
