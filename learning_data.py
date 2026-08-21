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
        "reading_time": 5,
        "difficulty": "Легко",
        "content": """
# CIA Triad

CIA Triad — фундаментальная модель информационной безопасности.

| Принцип | Описание |
|---------|----------|
| Конфиденциальность | Данные доступны только тем, у кого есть права |
| Целостность | Данные не изменены несанкционированно |
| Доступность | Данные доступны, когда они нужны |

## Конфиденциальность

Защита данных от несанкционированного доступа.

**Методы:** Шифрование, контроль доступа, классификация данных.

## Целостность

Гарантия, что данные не были изменены.

**Методы:** Хеш-суммы, цифровые подписи, контроль версий.

## Доступность

Обеспечение доступа к данным, когда они нужны.

**Методы:** Резервное копирование, балансировка нагрузки.

## Практика

Пройди комнату «Основы кибербезопасности».
"""
    },
    "basics_hackers": {
        "id": "basics_hackers",
        "category": "basics",
        "title": "Типы хакеров",
        "short_description": "White Hat, Black Hat, Grey Hat",
        "reading_time": 4,
        "difficulty": "Легко",
        "content": """
# Типы хакеров

| Тип | Описание |
|-----|----------|
| White Hat | Этичные хакеры, работают легально |
| Black Hat | Неэтичные, взламывают ради выгоды |
| Grey Hat | На грани, без злого умысла |

## White Hat

Работают в компаниях или как баг-баунти охотники.

## Black Hat

Действуют незаконно, крадут данные.

## Grey Hat

Находят уязвимости и сообщают о них.

## Практика

Пройди комнату «Основы кибербезопасности».
"""
    },
    "crypto_base64": {
        "id": "crypto_base64",
        "category": "crypto",
        "title": "Base64 — кодирование, не шифрование",
        "short_description": "Как работает Base64",
        "reading_time": 5,
        "difficulty": "Легко",
        "content": """
# Base64

Base64 — способ представления бинарных данных в текстовом виде.

Важно: это КОДИРОВАНИЕ, а не ШИФРОВАНИЕ.

## Примеры

Hello -> SGVsbG8=
CyberLab -> Q3liZXJMYWI=

## Декодирование

echo "SGVsbG8=" | base64 -d

## Практика

Расшифруй: Q3liZXJMYWIgSXMgQXdlc29tZSE=
"""
    },
    "crypto_rot13": {
        "id": "crypto_rot13",
        "category": "crypto",
        "title": "ROT13 — шифр сдвига",
        "short_description": "Простой шифр",
        "reading_time": 3,
        "difficulty": "Легко",
        "content": """
# ROT13

Шифр, заменяющий каждую букву на букву через 13 позиций.

## Примеры

Hello -> Uryyb
CyberLab -> PloreYnO

## Расшифровка

echo "Uryyb" | tr 'A-Za-z' 'N-ZA-Mn-za-m'

## Практика

Расшифруй: PloreYnO vf pbby!
"""
    },
    "crypto_hash": {
        "id": "crypto_hash",
        "category": "crypto",
        "title": "Хеширование",
        "short_description": "MD5, SHA-1, SHA-256",
        "reading_time": 6,
        "difficulty": "Средне",
        "content": """
# Хеширование

Хеш — результат работы хеш-функции.

| Алгоритм | Длина | Безопасность |
|----------|-------|-------------|
| MD5 | 32 hex | Взломан |
| SHA-1 | 40 hex | Взломан |
| SHA-256 | 64 hex | Безопасен |

## Пример

MD5("password") = 5f4dcc3b5aa765d61d8327deb882cf99

## Практика

Найди исходную строку для MD5: 5f4dcc3b5aa765d61d8327deb882cf99
"""
    },
    "web_sqli": {
        "id": "web_sqli",
        "category": "web",
        "title": "SQL Injection",
        "short_description": "Основы SQL-инъекций",
        "reading_time": 7,
        "difficulty": "Средне",
        "content": """
# SQL Injection

Уязвимость, позволяющая внедрить SQL-код в запрос.

## Пример

SELECT * FROM users WHERE id = 1 OR 1=1

## Атаки

Обход авторизации: ' OR '1'='1' --
Вывод данных: ' UNION SELECT username, password FROM users --

## Защита

Параметризованные запросы, экранирование, WAF.

## Практика

DVWA → SQL Injection → 1' OR '1'='1
"""
    },
    "web_xss": {
        "id": "web_xss",
        "category": "web",
        "title": "XSS",
        "short_description": "Межсайтовый скриптинг",
        "reading_time": 6,
        "difficulty": "Средне",
        "content": """
# XSS

Уязвимость, позволяющая внедрить JavaScript на страницу.

## Типы

| Тип | Описание |
|-----|----------|
| Reflected | Выполняется сразу |
| Stored | Сохраняется на сервере |
| DOM-based | В JavaScript |

## Пример

<script>alert('XSS')</script>

## Практика

DVWA → XSS (Reflected) → <script>alert('XSS')</script>
"""
    },
    "network_osi": {
        "id": "network_osi",
        "category": "network",
        "title": "Модель OSI",
        "short_description": "7 уровней",
        "reading_time": 6,
        "difficulty": "Средне",
        "content": """
# Модель OSI

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
        "title": "Команды Linux",
        "short_description": "Основные команды",
        "reading_time": 8,
        "difficulty": "Легко",
        "content": """
# Команды Linux

## Навигация

pwd — текущая директория
ls -la — список файлов
cd /path — перейти

## Файлы

cat file.txt — показать
grep "text" file — поиск
find / -name "*.txt" — найти

## Права

chmod 777 file — все права
chmod +x script.sh — исполняемый
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
        "title": "LSB стеганография",
        "short_description": "Скрытие в изображениях",
        "reading_time": 5,
        "difficulty": "Средне",
        "content": """
# LSB стеганография

Скрытие данных в наименее значимых битах пикселей.

## Инструменты

zsteg image.png
steghide extract -sf image.jpg

## Практика

Скачай CTF-файл и найди флаг.
"""
    },
    "reverse_ghidra": {
        "id": "reverse_ghidra",
        "category": "reverse",
        "title": "Ghidra",
        "short_description": "Инструмент для RE",
        "reading_time": 5,
        "difficulty": "Средне",
        "content": """
# Ghidra

Бесплатный фреймворк для обратной разработки от NSA.

## Возможности

Дизассемблирование, декомпиляция, анализ.

## Установка

Скачай с https://ghidra-sre.org/

## Практика

Пройди комнату «Reverse Engineering».
"""
    },
    "osint_google_dorks": {
        "id": "osint_google_dorks",
        "category": "osint",
        "title": "Google Dorks",
        "short_description": "Продвинутый поиск",
        "reading_time": 5,
        "difficulty": "Средне",
        "content": """
# Google Dorks

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
        "title": "Shodan",
        "short_description": "Поисковик устройств",
        "reading_time": 5,
        "difficulty": "Средне",
        "content": """
# Shodan

Поисковая система для устройств в интернете.

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