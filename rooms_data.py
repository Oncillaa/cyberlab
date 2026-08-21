#!/usr/bin/env python3
"""
Данные комнат и заданий для CyberLab
Автор: Oncilla (https://github.com/Oncillaa)
"""


# Список комнат с заданиями
ROOMS = {
    "basics": {
        "id": "basics",
        "title": "🔰 Основы кибербезопасности",
        "description": "Первая комната для новичков. Узнай базовые понятия и термины.",
        "difficulty": "Легко",
        "points": 100,
        "icon": "🔰",
        "tasks": [
            {
                "id": "task1",
                "title": "Что такое CIA Triad?",
                "description": "CIA Triad — это три основных принципа информационной безопасности. Расшифруй аббревиатуру CIA.",
                "type": "text",
                "answer": "confidentiality integrity availability",
                "hint": "Конфиденциальность, целостность и...",
                "points": 10
            },
            {
                "id": "task2",
                "title": "Типы хакеров",
                "description": "Как называются хакеры, которые работают на компании и помогают находить уязвимости законно?",
                "type": "text",
                "answer": "white hat",
                "hint": "Они носят 'белую шляпу'.",
                "points": 15
            },
            {
                "id": "task3",
                "title": "Самый распространённый пароль",
                "description": "Какой пароль чаще всего встречается в утечках данных? (одно слово, без цифр)",
                "type": "text",
                "answer": "password",
                "hint": "Это слово переводится как 'пароль'.",
                "points": 10
            },
            {
                "id": "task4",
                "title": "OSI Model",
                "description": "Сколько уровней в модели OSI?",
                "type": "text",
                "answer": "7",
                "hint": "Физический, канальный, сетевой, транспортный, сеансовый, представления, прикладной.",
                "points": 15
            },
            {
                "id": "task5",
                "title": "Первый флаг",
                "description": "Найди флаг в этой строке: ZmxhZ3tjeWJlcmxhYl9zdGFydH0=",
                "type": "flag",
                "answer": "flag{cyberlab_start}",
                "hint": "Это base64. Расшифруй.",
                "points": 50
            }
        ]
    },
    
    "crypto": {
        "id": "crypto",
        "title": "🔐 Криптография",
        "description": "Научись расшифровывать сообщения разными методами.",
        "difficulty": "Средне",
        "points": 150,
        "icon": "🔐",
        "tasks": [
            {
                "id": "task1",
                "title": "Base64",
                "description": "Расшифруй: SGVsbG8gQ3liZXJMYWIh",
                "type": "flag",
                "answer": "Hello CyberLab!",
                "hint": "Используй base64 декодер.",
                "points": 20
            },
            {
                "id": "task2",
                "title": "ROT13",
                "description": "Расшифруй ROT13: PloreYnO vf pbby!",
                "type": "flag",
                "answer": "CyberLab is cool!",
                "hint": "Сдвиг на 13 символов в алфавите.",
                "points": 25
            },
            {
                "id": "task3",
                "title": "Hex",
                "description": "Расшифруй hex: 666c61677b6865785f69735f66756e7d",
                "type": "flag",
                "answer": "flag{hex_is_fun}",
                "hint": "Конвертируй из шестнадцатеричной системы.",
                "points": 30
            },
            {
                "id": "task4",
                "title": "MD5 Hash",
                "description": "Найди исходную строку для MD5 хеша: 5f4dcc3b5aa765d61d8327deb882cf99",
                "type": "flag",
                "answer": "password",
                "hint": "Это самый распространённый пароль.",
                "points": 35
            },
            {
                "id": "task5",
                "title": "Caesar Cipher",
                "description": "Расшифруй шифр Цезаря (сдвиг 3): iodj{fdhvdu_lv_hdvb}",
                "type": "flag",
                "answer": "flag{caesar_is_easy}",
                "hint": "Сдвинь каждую букву на 3 назад.",
                "points": 40
            }
        ]
    },
    
    "web": {
        "id": "web",
        "title": "🌐 Веб-уязвимости",
        "description": "Изучи основные уязвимости веб-приложений.",
        "difficulty": "Средне",
        "points": 200,
        "icon": "🌐",
        "tasks": [
            {
                "id": "task1",
                "title": "SQL Injection",
                "description": "Какой символ часто используется для комментария в SQL? (один символ)",
                "type": "text",
                "answer": "-",
                "hint": "Двойной дефис.",
                "points": 20
            },
            {
                "id": "task2",
                "title": "XSS",
                "description": "Расшифруй аббревиатуру XSS.",
                "type": "text",
                "answer": "cross site scripting",
                "hint": "Межсайтовый...",
                "points": 25
            },
            {
                "id": "task3",
                "title": "HTTP Status",
                "description": "Какой HTTP код означает 'Forbidden' (доступ запрещён)?",
                "type": "text",
                "answer": "403",
                "hint": "4xx — ошибки клиента.",
                "points": 15
            },
            {
                "id": "task4",
                "title": "Directory Traversal",
                "description": "Какой файл обычно пытаются прочитать при directory traversal на Linux?",
                "type": "text",
                "answer": "etc/passwd",
                "hint": "Содержит информацию о пользователях системы.",
                "points": 30
            },
            {
                "id": "task5",
                "title": "Найди флаг в HTML",
                "description": "Посмотри на исходный код страницы и найди флаг: <!-- flag{html_comments_are_visible} -->",
                "type": "flag",
                "answer": "flag{html_comments_are_visible}",
                "hint": "Флаг спрятан в HTML комментарии.",
                "points": 50
            },
            {
                "id": "task6",
                "title": "Cookies",
                "description": "Что используется для хранения сессии пользователя на стороне клиента?",
                "type": "text",
                "answer": "cookies",
                "hint": "Маленькие файлы в браузере.",
                "points": 20
            }
        ]
    },
    
    "network": {
        "id": "network",
        "title": "📡 Сетевые технологии",
        "description": "Основы сетевого взаимодействия и протоколов.",
        "difficulty": "Средне",
        "points": 180,
        "icon": "📡",
        "tasks": [
            {
                "id": "task1",
                "title": "Порт SSH",
                "description": "На каком порту работает SSH по умолчанию?",
                "type": "text",
                "answer": "22",
                "hint": "Один из самых известных портов.",
                "points": 20
            },
            {
                "id": "task2",
                "title": "Порт HTTP",
                "description": "На каком порту работает HTTP?",
                "type": "text",
                "answer": "80",
                "hint": "Стандартный порт для веб-сайтов без шифрования.",
                "points": 15
            },
            {
                "id": "task3",
                "title": "DNS",
                "description": "Что делает DNS?",
                "type": "text",
                "answer": "resolves domain names to ip addresses",
                "hint": "Преобразует доменные имена в IP-адреса.",
                "points": 25
            },
            {
                "id": "task4",
                "title": "TCP vs UDP",
                "description": "Какой протокол быстрее, но менее надёжный: TCP или UDP?",
                "type": "text",
                "answer": "udp",
                "hint": "Три буквы.",
                "points": 20
            },
            {
                "id": "task5",
                "title": "Ping",
                "description": "Какой протокол использует команда ping?",
                "type": "text",
                "answer": "icmp",
                "hint": "Internet Control Message Protocol.",
                "points": 30
            }
        ]
    },
    
    "forensics": {
        "id": "forensics",
        "title": "🔍 Форензика",
        "description": "Цифровая криминалистика и анализ данных.",
        "difficulty": "Сложно",
        "points": 250,
        "icon": "🔍",
        "tasks": [
            {
                "id": "task1",
                "title": "Файловые сигнатуры",
                "description": "Какая сигнатура (magic bytes) у JPEG файла? (hex, без пробелов)",
                "type": "text",
                "answer": "ffd8ffe0",
                "hint": "Начинается с FF D8.",
                "points": 30
            },
            {
                "id": "task2",
                "title": "Найди флаг в бинарном файле",
                "description": "В бинарном файле спрятан флаг. Используй команду strings: flag{strings_command_is_useful}",
                "type": "flag",
                "answer": "flag{strings_command_is_useful}",
                "hint": "Команда strings показывает текстовые строки в бинарных файлах.",
                "points": 50
            },
            {
                "id": "task3",
                "title": "Метаданные изображений",
                "description": "Какая команда Linux показывает метаданные изображений?",
                "type": "text",
                "answer": "exiftool",
                "hint": "Начинается с 'exif'.",
                "points": 40
            },
            {
                "id": "task4",
                "title": "Steganography",
                "description": "Что скрывает текст внутри изображений?",
                "type": "text",
                "answer": "steganography",
                "hint": "Искусство скрытой передачи информации.",
                "points": 35
            }
        ]
    },
    
    "linux": {
        "id": "linux",
        "title": "🐧 Linux для хакеров",
        "description": "Основные команды Linux для пентеста.",
        "difficulty": "Легко",
        "points": 120,
        "icon": "🐧",
        "tasks": [
            {
                "id": "task1",
                "title": "Список файлов",
                "description": "Какая команда показывает список файлов в директории?",
                "type": "text",
                "answer": "ls",
                "hint": "Две буквы.",
                "points": 10
            },
            {
                "id": "task2",
                "title": "Права доступа",
                "description": "Какая команда изменяет права доступа к файлу?",
                "type": "text",
                "answer": "chmod",
                "hint": "Изменение mode.",
                "points": 20
            },
            {
                "id": "task3",
                "title": "Поиск файлов",
                "description": "Какая команда ищет файлы в системе?",
                "type": "text",
                "answer": "find",
                "hint": "Переводится как 'найти'.",
                "points": 15
            },
            {
                "id": "task4",
                "title": "Просмотр логов",
                "description": "Какая команда показывает последние строки файла?",
                "type": "text",
                "answer": "tail",
                "hint": "Противоположность head.",
                "points": 15
            },
            {
                "id": "task5",
                "title": "Суперпользователь",
                "description": "Какая команда запускает программы от имени root?",
                "type": "text",
                "answer": "sudo",
                "hint": "SuperUser DO.",
                "points": 20
            }
        ]
    }
}


def get_all_rooms():
    """Возвращает список всех комнат."""
    return list(ROOMS.values())


def get_room(room_id):
    """Возвращает комнату по ID."""
    return ROOMS.get(room_id)


def get_total_points(room_id):
    """Возвращает общее количество очков за комнату."""
    room = get_room(room_id)
    if not room:
        return 0
    return sum(task["points"] for task in room["tasks"])