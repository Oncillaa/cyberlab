#!/usr/bin/env python3
"""
Данные комнат и заданий для CyberLab
Автор: Oncilla (https://github.com/Oncillaa)
"""


ROOMS = {
    "basics": {
        "id": "basics",
        "title": "Основы кибербезопасности",
        "description": "Первая комната для новичков. Узнай базовые понятия и термины.",
        "difficulty": "Легко",
        "points": 150,
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
            },
            {
                "id": "task6",
                "title": "Самый безопасный пароль",
                "description": "Какой пароль считается самым безопасным? (одно слово)",
                "type": "text",
                "answer": "passphrase",
                "hint": "Длинная фраза вместо короткого слова.",
                "points": 15
            },
            {
                "id": "task7",
                "title": "Двухфакторная аутентификация",
                "description": "Как расшифровывается 2FA?",
                "type": "text",
                "answer": "two factor authentication",
                "hint": "Двух...",
                "points": 15
            },
            {
                "id": "task8",
                "title": "Фишинг",
                "description": "Как называется атака, когда злоумышленник отправляет поддельные письма для кражи данных?",
                "type": "text",
                "answer": "phishing",
                "hint": "Начинается с 'ph'.",
                "points": 10
            },
            {
                "id": "task9",
                "title": "Второй флаг",
                "description": "Расшифруй: RmxhZ3tjeWJlcmxhYl9zZWNvbmR9",
                "type": "flag",
                "answer": "Flag{cyberlab_second}",
                "hint": "Base64.",
                "points": 50
            }
        ]
    },
    
    "crypto": {
        "id": "crypto",
        "title": "Криптография",
        "description": "Научись расшифровывать сообщения разными методами.",
        "difficulty": "Средне",
        "points": 200,
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
            },
            {
                "id": "task6",
                "title": "Base32",
                "description": "Расшифруй Base32: JBSWY3DPEBLW64TMMQQQ====",
                "type": "flag",
                "answer": "Hello World!",
                "hint": "Используй base32 декодер.",
                "points": 30
            },
            {
                "id": "task7",
                "title": "SHA-256",
                "description": "Найди исходную строку для SHA-256: 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
                "type": "flag",
                "answer": "password",
                "hint": "Самый распространённый пароль.",
                "points": 35
            }
        ]
    },
    
    "web": {
        "id": "web",
        "title": "Веб-уязвимости",
        "description": "Изучи основные уязвимости веб-приложений.",
        "difficulty": "Средне",
        "points": 250,
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
            },
            {
                "id": "task7",
                "title": "HTTP методы",
                "description": "Какой HTTP метод используется для отправки данных на сервер?",
                "type": "text",
                "answer": "post",
                "hint": "Противоположность GET.",
                "points": 15
            },
            {
                "id": "task8",
                "title": "Безопасный заголовок",
                "description": "Какой заголовок защищает от XSS?",
                "type": "text",
                "answer": "content security policy",
                "hint": "CSP.",
                "points": 25
            },
            {
                "id": "task9",
                "title": "Второй флаг",
                "description": "Флаг в cookie: flag{cookies_are_yummy}",
                "type": "flag",
                "answer": "flag{cookies_are_yummy}",
                "hint": "Проверь cookie.",
                "points": 50
            }
        ]
    },
    
    "network": {
        "id": "network",
        "title": "Сетевые технологии",
        "description": "Основы сетевого взаимодействия и протоколов.",
        "difficulty": "Средне",
        "points": 200,
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
            },
            {
                "id": "task6",
                "title": "Порт HTTPS",
                "description": "На каком порту работает HTTPS?",
                "type": "text",
                "answer": "443",
                "hint": "HTTP + шифрование.",
                "points": 15
            },
            {
                "id": "task7",
                "title": "Порт DNS",
                "description": "На каком порту работает DNS?",
                "type": "text",
                "answer": "53",
                "hint": "Двузначное число.",
                "points": 15
            },
            {
                "id": "task8",
                "title": "Порт MySQL",
                "description": "На каком порту работает MySQL?",
                "type": "text",
                "answer": "3306",
                "hint": "Четырёхзначное число.",
                "points": 20
            }
        ]
    },
    
    "forensics": {
        "id": "forensics",
        "title": "Форензика",
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
        "title": "Linux для хакеров",
        "description": "Основные команды Linux для пентеста.",
        "difficulty": "Легко",
        "points": 150,
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
            },
            {
                "id": "task6",
                "title": "Просмотр процессов",
                "description": "Какая команда показывает все запущенные процессы?",
                "type": "text",
                "answer": "ps aux",
                "hint": "Process Status.",
                "points": 15
            },
            {
                "id": "task7",
                "title": "Поиск текста",
                "description": "Какая команда ищет текст в файле?",
                "type": "text",
                "answer": "grep",
                "hint": "Global Regular Expression Print.",
                "points": 10
            },
            {
                "id": "task8",
                "title": "Скачивание файла",
                "description": "Какая команда скачивает файл из интернета?",
                "type": "text",
                "answer": "wget",
                "hint": "Начинается с 'w'.",
                "points": 15
            }
        ]
    },
    
    "steganography": {
        "id": "steganography",
        "title": "Стеганография",
        "description": "Искусство скрытой передачи информации в изображениях, аудио и тексте.",
        "difficulty": "Сложно",
        "points": 200,
        "icon": "🖼",
        "tasks": [
            {
                "id": "task1",
                "title": "Что такое стеганография?",
                "description": "Чем стеганография отличается от криптографии?",
                "type": "text",
                "answer": "скрывает сам факт передачи информации",
                "hint": "Криптография шифрует содержимое, а стеганография...",
                "points": 20
            },
            {
                "id": "task2",
                "title": "LSB метод",
                "description": "Как расшифровывается LSB в контексте стеганографии?",
                "type": "text",
                "answer": "least significant bit",
                "hint": "Наименее значимый бит.",
                "points": 25
            },
            {
                "id": "task3",
                "title": "Инструменты",
                "description": "Какой популярный инструмент используется для стеганографии в изображениях?",
                "type": "text",
                "answer": "steghide",
                "hint": "Начинается с 'steg'.",
                "points": 30
            },
            {
                "id": "task4",
                "title": "Скрытый флаг",
                "description": "В изображении спрятан флаг методом LSB. Используй zsteg: flag{lsb_hidden_in_pixels}",
                "type": "flag",
                "answer": "flag{lsb_hidden_in_pixels}",
                "hint": "Проверь наименее значимые биты пикселей.",
                "points": 50
            },
            {
                "id": "task5",
                "title": "Аудио-стеганография",
                "description": "Какой метод скрывает данные в спектре аудиофайла?",
                "type": "text",
                "answer": "spectrogram",
                "hint": "Визуальное представление частот.",
                "points": 35
            }
        ]
    },
    
    "reverse": {
        "id": "reverse",
        "title": "Reverse Engineering",
        "description": "Обратная разработка программного обеспечения.",
        "difficulty": "Сложно",
        "points": 250,
        "icon": "🔧",
        "tasks": [
            {
                "id": "task1",
                "title": "Что такое RE?",
                "description": "Как называется процесс анализа программы без доступа к исходному коду?",
                "type": "text",
                "answer": "reverse engineering",
                "hint": "Обратная разработка.",
                "points": 20
            },
            {
                "id": "task2",
                "title": "Инструменты",
                "description": "Какой бесплатный инструмент от NSA используется для анализа бинарных файлов?",
                "type": "text",
                "answer": "ghidra",
                "hint": "Разработан АНБ.",
                "points": 30
            },
            {
                "id": "task3",
                "title": "Ассемблер",
                "description": "Какая команда в x86 ассемблере используется для вызова функции?",
                "type": "text",
                "answer": "call",
                "hint": "Переводится как 'вызвать'.",
                "points": 25
            },
            {
                "id": "task4",
                "title": "Строки",
                "description": "Какая команда Linux показывает текстовые строки в бинарном файле?",
                "type": "text",
                "answer": "strings",
                "hint": "Переводится как 'строки'.",
                "points": 20
            },
            {
                "id": "task5",
                "title": "Найди флаг",
                "description": "В бинарном файле спрятан флаг. Используй strings: flag{reverse_engineering_is_fun}",
                "type": "flag",
                "answer": "flag{reverse_engineering_is_fun}",
                "hint": "Ищи текстовые строки в файле.",
                "points": 50
            }
        ]
    },
    
    "osint": {
        "id": "osint",
        "title": "OSINT",
        "description": "Поиск информации в открытых источниках.",
        "difficulty": "Средне",
        "points": 200,
        "icon": "🔍",
        "tasks": [
            {
                "id": "task1",
                "title": "Что такое OSINT?",
                "description": "Расшифруй аббревиатуру OSINT.",
                "type": "text",
                "answer": "open source intelligence",
                "hint": "Разведка по открытым источникам.",
                "points": 20
            },
            {
                "id": "task2",
                "title": "Google Dorks",
                "description": "Какой оператор Google ищет только на определённом сайте?",
                "type": "text",
                "answer": "site:",
                "hint": "Оператор для поиска по конкретному домену.",
                "points": 25
            },
            {
                "id": "task3",
                "title": "Shodan",
                "description": "Какой сервис называют 'поисковиком для хакеров'?",
                "type": "text",
                "answer": "shodan",
                "hint": "Ищет устройства, подключённые к интернету.",
                "points": 30
            },
            {
                "id": "task4",
                "title": "Метаданные",
                "description": "Какая команда показывает метаданные изображения?",
                "type": "text",
                "answer": "exiftool",
                "hint": "Начинается с 'exif'.",
                "points": 25
            },
            {
                "id": "task5",
                "title": "Поиск по фото",
                "description": "Как называется техника поиска информации по фотографии?",
                "type": "text",
                "answer": "reverse image search",
                "hint": "Обратный поиск изображения.",
                "points": 30
            },
            {
                "id": "task6",
                "title": "Найди флаг",
                "description": "Используй Google Dorks для поиска: flag{osint_master}",
                "type": "flag",
                "answer": "flag{osint_master}",
                "hint": "Попробуй поискать этот флаг в интернете.",
                "points": 50
            },
            {
                "id": "task7",
                "title": "WHOIS",
                "description": "Какая команда показывает информацию о домене?",
                "type": "text",
                "answer": "whois",
                "hint": "Кто владелец домена?",
                "points": 20
            },
            {
                "id": "task8",
                "title": "Архив сайтов",
                "description": "Какой сервис показывает старые версии сайтов?",
                "type": "text",
                "answer": "wayback machine",
                "hint": "Машина времени для сайтов.",
                "points": 25
            }
        ]
    }
}


def get_all_rooms():
    return list(ROOMS.values())


def get_room(room_id):
    return ROOMS.get(room_id)


def get_total_points(room_id):
    room = get_room(room_id)
    if not room:
        return 0
    return sum(task["points"] for task in room["tasks"])