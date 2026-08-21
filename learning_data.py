#!/usr/bin/env python3
"""
Данные для раздела обучения CyberLab
Автор: Oncilla (https://github.com/Oncillaa)
"""

LEARNING_CATEGORIES = [
    {
        "id": "basics",
        "title": "🔰 Основы кибербезопасности",
        "description": "Базовые понятия: CIA Triad, типы хакеров, модели угроз",
        "icon": "🔰",
        "article_count": 2
    },
    {
        "id": "crypto",
        "title": "🔐 Криптография",
        "description": "Шифрование, хеширование, кодирование: Base64, ROT13, AES, RSA",
        "icon": "🔐",
        "article_count": 3
    },
    {
        "id": "web",
        "title": "🌐 Веб-уязвимости",
        "description": "SQLi, XSS, CSRF, File Inclusion, Directory Traversal",
        "icon": "🌐",
        "article_count": 2
    },
    {
        "id": "network",
        "title": "📡 Сетевые технологии",
        "description": "TCP/IP, DNS, порты, протоколы, OSI модель",
        "icon": "📡",
        "article_count": 1
    },
    {
        "id": "linux",
        "title": "🐧 Linux для хакеров",
        "description": "Команды, права, bash-скрипты, автоматизация",
        "icon": "🐧",
        "article_count": 1
    },
    {
        "id": "steganography",
        "title": "🖼 Стеганография",
        "description": "Скрытие данных в изображениях, аудио, тексте",
        "icon": "🖼",
        "article_count": 1
    },
    {
        "id": "reverse",
        "title": "🔧 Reverse Engineering",
        "description": "Анализ бинарных файлов, дизассемблирование, отладка",
        "icon": "🔧",
        "article_count": 1
    },
    {
        "id": "osint",
        "title": "🔍 OSINT",
        "description": "Поиск информации в открытых источниках",
        "icon": "🔍",
        "article_count": 2
    }
]

ARTICLES = {
    "basics_cia_triad": {
        "id": "basics_cia_triad",
        "category": "basics",
        "title": "CIA Triad — три кита безопасности",
        "short_description": "Конфиденциальность, целостность, доступность",
        "reading_time": 7,
        "difficulty": "Легко",
        "content": """
# CIA Triad

CIA Triad — это три главных принципа информационной безопасности.

| Принцип | Простыми словами |
|---------|-----------------|
| Конфиденциальность | Твой секрет знаешь только ты |
| Целостность | Твои данные никто не подменил |
| Доступность | Твои данные всегда под рукой |

## Конфиденциальность

Данные должны видеть только те, кому разрешено.

**Методы защиты:** шифрование (AES, RSA), двухфакторная аутентификация, права доступа.

## Целостность

Данные нельзя незаметно изменить.

**Методы защиты:** хеш-суммы (MD5, SHA-256), цифровые подписи.

## Доступность

Данные должны быть доступны, когда нужны.

**Методы защиты:** резервные копии, балансировка нагрузки.

## Практика

Зайди в комнату «Основы кибербезопасности» и ответь на вопрос.
"""
    },
    "basics_hackers": {
        "id": "basics_hackers",
        "category": "basics",
        "title": "Типы хакеров",
        "short_description": "White Hat, Black Hat, Grey Hat",
        "reading_time": 6,
        "difficulty": "Легко",
        "content": """
# Типы хакеров

| Тип | Кто это |
|-----|---------|
| White Hat | Этичные, работают легально |
| Black Hat | Неэтичные, взламывают незаконно |
| Grey Hat | На грани, без злого умысла |

## White Hat

Тестируют сайты на уязвимости, ищут баги за деньги, помогают компаниям.

## Black Hat

Крадут данные, шантажируют, продают доступы. Наказание в РФ — до 10 лет.

## Grey Hat

Взламывают «ради интереса», сообщают владельцу о проблеме.

## Практика

Зайди в комнату «Основы кибербезопасности».
"""
    },
    "crypto_base64": {
        "id": "crypto_base64",
        "category": "crypto",
        "title": "Base64 — кодирование, не шифрование",
        "short_description": "Как работает Base64 и почему это НЕ шифрование",
        "reading_time": 8,
        "difficulty": "Легко",
        "content": """
# Base64 — кодирование, не шифрование

Base64 — способ представить бинарные данные в виде текста.

**Важно:** Base64 — это КОДИРОВАНИЕ, а НЕ ШИФРОВАНИЕ.

## Примеры

Hello → SGVsbG8=

CyberLab → Q3liZXJMYWI=

flag{test} → ZmxhZ3t0ZXN0fQ==

## Команды Linux

Кодировать: echo -n "Hello" | base64

Декодировать: echo "SGVsbG8=" | base64 -d

## Команды Windows PowerShell

Кодировать: [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("Hello"))

Декодировать: [System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("SGVsbG8="))

## Практика

Расшифруй: Q3liZXJMYWIgSXMgQXdlc29tZSE=
"""
    },
    "crypto_rot13": {
        "id": "crypto_rot13",
        "category": "crypto",
        "title": "ROT13 — шифр сдвига на 13",
        "short_description": "Простой шифр, который можно расшифровать в голове",
        "reading_time": 6,
        "difficulty": "Легко",
        "content": """
# ROT13 — шифр сдвига на 13

ROT13 заменяет каждую букву на букву через 13 позиций.

**Особенность:** Применение ROT13 дважды возвращает исходный текст.

## Примеры

Hello → Uryyb

CyberLab → PloreYnO

flag → synt

## Команды Linux

Расшифровать: echo "Uryyb" | tr 'A-Za-z' 'N-ZA-Mn-za-m'

## Windows PowerShell

Используй онлайн: https://rot13.com

## Практика

Расшифруй: PloreYnO vf pbby!
"""
    },
    "crypto_hash": {
        "id": "crypto_hash",
        "category": "crypto",
        "title": "Хеширование: MD5, SHA-1, SHA-256",
        "short_description": "Что такое хеш, как его вычислить и взломать",
        "reading_time": 9,
        "difficulty": "Средне",
        "content": """
# Хеширование: MD5, SHA-1, SHA-256

Хеш — это «отпечаток» данных. Любой текст → строка фиксированной длины.

## Популярные алгоритмы

| Алгоритм | Длина | Безопасность |
|----------|-------|-------------|
| MD5 | 32 hex | Взломан |
| SHA-1 | 40 hex | Взломан |
| SHA-256 | 64 hex | Безопасен |

## Примеры

MD5("password") = 5f4dcc3b5aa765d61d8327deb882cf99

## Команды Linux

Вычислить MD5: echo -n "password" | md5sum

Вычислить SHA-256: echo -n "password" | sha256sum

## Команды Windows PowerShell

Вычислить хеш файла: Get-FileHash -Algorithm SHA256 file.txt

## Практика

Найди исходную строку для MD5: 5f4dcc3b5aa765d61d8327deb882cf99
"""
    },
    "web_sqli": {
        "id": "web_sqli",
        "category": "web",
        "title": "SQL Injection — основы",
        "short_description": "Как работает SQL-инъекция",
        "reading_time": 8,
        "difficulty": "Средне",
        "content": """
# SQL Injection — основы

SQL Injection — это уязвимость, позволяющая внедрить SQL-код в запрос к базе данных.

## Пример атаки

Легитимный запрос: SELECT * FROM users WHERE id = 1

Атакующий запрос: SELECT * FROM users WHERE id = 1 OR 1=1

Результат: вернутся ВСЕ записи, потому что 1=1 всегда истинно.

## Примеры атак

Обход авторизации: ' OR '1'='1' --

Вывод всех пользователей: ' UNION SELECT username, password FROM users --

## Защита

Параметризованные запросы (Prepared Statements), экранирование ввода, WAF.

## Практика

Открой DVWA → SQL Injection → введи 1' OR '1'='1
"""
    },
    "web_xss": {
        "id": "web_xss",
        "category": "web",
        "title": "XSS — межсайтовый скриптинг",
        "short_description": "Типы XSS и как они работают",
        "reading_time": 7,
        "difficulty": "Средне",
        "content": """
# XSS — межсайтовый скриптинг

XSS — уязвимость, позволяющая внедрить JavaScript на страницу.

## Типы XSS

| Тип | Описание |
|-----|----------|
| Reflected | Выполняется сразу |
| Stored | Сохраняется на сервере |
| DOM-based | Уязвимость в JavaScript |

## Пример атаки

<script>alert('XSS')</script>

## Защита

Экранирование HTML, Content Security Policy, HttpOnly cookie.

## Практика

В DVWA → XSS (Reflected) введи: <script>alert('XSS')</script>
"""
    },
    "network_osi": {
        "id": "network_osi",
        "category": "network",
        "title": "Модель OSI — 7 уровней",
        "short_description": "Понимание сетевой модели",
        "reading_time": 6,
        "difficulty": "Средне",
        "content": """
# Модель OSI — 7 уровней

OSI — эталонная модель, описывающая передачу данных по сети.

| # | Уровень | Протоколы |
|---|---------|-----------|
| 7 | Прикладной | HTTP, DNS |
| 6 | Представления | SSL, TLS |
| 5 | Сеансовый | NetBIOS |
| 4 | Транспортный | TCP, UDP |
| 3 | Сетевой | IP, ICMP |
| 2 | Канальный | Ethernet |
| 1 | Физический | USB |

## Практика

Пройди комнату «Сетевые технологии».
"""
    },
    "linux_commands": {
        "id": "linux_commands",
        "category": "linux",
        "title": "Команды Linux для хакера",
        "short_description": "ls, cd, cat, grep, find, chmod",
        "reading_time": 8,
        "difficulty": "Легко",
        "content": """
# Команды Linux для хакера

## Навигация

pwd — текущая директория

ls -la — список файлов с правами

cd /path — перейти

## Работа с файлами

cat file.txt — показать содержимое

grep "text" file — поиск

find / -name "*.txt" — найти файл

strings binary.bin — строки в бинарнике

## Права доступа

chmod 777 file — все права

chmod +x script.sh — сделать исполняемым

sudo command — от root

## Сеть

netstat -tulpn — порты

nmap -sV target — сканирование

## Практика

Пройди комнату «Linux для хакеров».
"""
    },
    "stego_lsb": {
        "id": "stego_lsb",
        "category": "steganography",
        "title": "LSB — скрытие данных в изображениях",
        "short_description": "Метод наименее значимого бита",
        "reading_time": 5,
        "difficulty": "Средне",
        "content": """
# LSB — скрытие данных в изображениях

LSB (Least Significant Bit) — метод скрытия данных в наименее значимых битах пикселей.

## Инструменты

zsteg image.png — для PNG

steghide extract -sf image.jpg — для JPEG

## Практика

Скачай CTF-файл и найди скрытый флаг.
"""
    },
    "reverse_ghidra": {
        "id": "reverse_ghidra",
        "category": "reverse",
        "title": "Ghidra — инструмент для RE",
        "short_description": "Знакомство с Ghidra от NSA",
        "reading_time": 5,
        "difficulty": "Средне",
        "content": """
# Ghidra — инструмент для RE

Ghidra — бесплатный фреймворк для обратной разработки от NSA.

## Возможности

Дизассемблирование, декомпиляция, анализ бинарных файлов.

## Установка

Скачай с https://ghidra-sre.org/

## Практика

Пройди комнату «Reverse Engineering».
"""
    },
    "osint_google_dorks": {
        "id": "osint_google_dorks",
        "category": "osint",
        "title": "Google Dorks — продвинутый поиск",
        "short_description": "Операторы Google для OSINT",
        "reading_time": 5,
        "difficulty": "Средне",
        "content": """
# Google Dorks — продвинутый поиск

Операторы для продвинутого поиска.

| Оператор | Пример |
|----------|--------|
| site: | site:github.com "password" |
| filetype: | filetype:pdf "confidential" |
| intitle: | intitle:"index of" |
| inurl: | inurl:admin |

## Практика

Пройди комнату «OSINT».
"""
    },
    "osint_shodan": {
        "id": "osint_shodan",
        "category": "osint",
        "title": "Shodan — поисковик устройств",
        "short_description": "Поиск устройств в интернете",
        "reading_time": 5,
        "difficulty": "Средне",
        "content": """
# Shodan — поисковик устройств

Shodan — поисковая система для устройств в интернете.

## Фильтры

port:22

country:RU

product:Apache

## Практика

Пройди комнату «OSINT».
"""
    }
}


def get_all_categories():
    return LEARNING_CATEGORIES


def get_category(category_id):
    for cat in LEARNING_CATEGORIES:
        if cat["id"] == category_id:
            return cat
    return None


def get_articles_by_category(category_id):
    articles = []
    for article in ARTICLES.values():
        if article["category"] == category_id:
            articles.append(article)
    return articles


def get_article(article_id):
    return ARTICLES.get(article_id)


def get_reading_time_text(minutes):
    if minutes == 1:
        return "1 минута"
    elif 2 <= minutes <= 4:
        return f"{minutes} минуты"
    else:
        return f"{minutes} минут"