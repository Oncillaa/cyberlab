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
        "article_count": 4
    },
    {
        "id": "crypto",
        "title": "🔐 Криптография",
        "description": "Шифрование, хеширование, кодирование: Base64, ROT13, AES, RSA",
        "icon": "🔐",
        "article_count": 5
    },
    {
        "id": "web",
        "title": "🌐 Веб-уязвимости",
        "description": "SQLi, XSS, CSRF, File Inclusion, Directory Traversal",
        "icon": "🌐",
        "article_count": 4
    },
    {
        "id": "network",
        "title": "📡 Сетевые технологии",
        "description": "TCP/IP, DNS, порты, протоколы, OSI модель",
        "icon": "📡",
        "article_count": 3
    },
    {
        "id": "linux",
        "title": "🐧 Linux для хакеров",
        "description": "Команды, права, bash-скрипты, автоматизация",
        "icon": "🐧",
        "article_count": 3
    },
    {
        "id": "steganography",
        "title": "🖼 Стеганография",
        "description": "Скрытие данных в изображениях, аудио, тексте",
        "icon": "🖼",
        "article_count": 2
    },
    {
        "id": "reverse",
        "title": "🔧 Reverse Engineering",
        "description": "Анализ бинарных файлов, дизассемблирование, отладка",
        "icon": "🔧",
        "article_count": 2
    },
    {
        "id": "osint",
        "title": "🔍 OSINT",
        "description": "Поиск информации в открытых источниках",
        "icon": "🔍",
        "article_count": 3
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
# CIA Triad — три кита безопасности

CIA Triad — это три главных принципа информационной безопасности.

| Принцип | Простыми словами |
|---------|-----------------|
| Конфиденциальность | Твой секрет знаешь только ты |
| Целостность | Твои данные никто не подменил |
| Доступность | Твои данные всегда под рукой |

## Конфиденциальность

Данные должны видеть только те, кому разрешено.

**Методы защиты:** шифрование (AES, RSA), двухфакторная аутентификация.

## Целостность

Данные нельзя незаметно изменить.

**Методы защиты:** хеш-суммы (MD5, SHA-256), цифровые подписи.

## Доступность

Данные должны быть доступны, когда нужны.

**Методы защиты:** резервные копии, балансировка нагрузки.

## Практика

Зайди в комнату «Основы кибербезопасности».
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

| Тип | Легальность |
|-----|-------------|
| White Hat | Законно |
| Black Hat | Незаконно |
| Grey Hat | Спорно |

## White Hat

Тестируют системы с разрешения. Баг-баунти охотники, пентестеры.

## Black Hat

Взламывают незаконно. Наказание в РФ — до 10 лет.

## Grey Hat

Взламывают «ради интереса», сообщают владельцу.

## Практика

Зайди в комнату «Основы кибербезопасности».
"""
    },
    "basics_osi_model": {
        "id": "basics_osi_model",
        "category": "basics",
        "title": "Модель OSI — 7 уровней",
        "short_description": "Понимание сетевой модели",
        "reading_time": 8,
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
    "basics_common_ports": {
        "id": "basics_common_ports",
        "category": "basics",
        "title": "Порты, которые должен знать каждый",
        "short_description": "Основные порты",
        "reading_time": 5,
        "difficulty": "Легко",
        "content": """
# Порты

| Порт | Протокол | Назначение |
|------|----------|------------|
| 21 | FTP | Файлы |
| 22 | SSH | Удалённый доступ |
| 80 | HTTP | Веб |
| 443 | HTTPS | Веб с шифрованием |
| 3306 | MySQL | База данных |
| 3389 | RDP | Рабочий стол |

## Проверка порта

Linux: nc -zv localhost 22

Windows: Test-NetConnection localhost -Port 22

## Практика

Пройди комнату «Сетевые технологии».
"""
    },
    "crypto_base64": {
        "id": "crypto_base64",
        "category": "crypto",
        "title": "Base64 — кодирование, не шифрование",
        "short_description": "Как работает Base64",
        "reading_time": 8,
        "difficulty": "Легко",
        "content": """
# Base64

Base64 — способ представить бинарные данные в виде текста.

**Важно:** это КОДИРОВАНИЕ, а НЕ ШИФРОВАНИЕ.

## Примеры

Hello → SGVsbG8=

CyberLab → Q3liZXJMYWI=

## Команды

Linux: echo -n "Hello" | base64

Linux декод: echo "SGVsbG8=" | base64 -d

Windows: [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("Hello"))

Python: import base64; base64.b64encode(b"Hello")

## Практика

Расшифруй: Q3liZXJMYWIgSXMgQXdlc29tZSE=
"""
    },
    "crypto_rot13": {
        "id": "crypto_rot13",
        "category": "crypto",
        "title": "ROT13 — шифр сдвига на 13",
        "short_description": "Простой шифр",
        "reading_time": 5,
        "difficulty": "Легко",
        "content": """
# ROT13

ROT13 заменяет букву на букву через 13 позиций.

## Примеры

Hello → Uryyb

CyberLab → PloreYnO

## Команды

Linux: echo "Uryyb" | tr 'A-Za-z' 'N-ZA-Mn-za-m'

Python: import codecs; codecs.decode("Uryyb", "rot_13")

## Практика

Расшифруй: PloreYnO vf pbby!
"""
    },
    "crypto_hash": {
        "id": "crypto_hash",
        "category": "crypto",
        "title": "Хеширование",
        "short_description": "MD5, SHA-1, SHA-256",
        "reading_time": 9,
        "difficulty": "Средне",
        "content": """
# Хеширование

Хеш — «отпечаток» данных.

| Алгоритм | Безопасность |
|----------|-------------|
| MD5 | Взломан |
| SHA-1 | Взломан |
| SHA-256 | Безопасен |

## Пример

MD5("password") = 5f4dcc3b5aa765d61d8327deb882cf99

## Команды

Linux: echo -n "password" | md5sum

Windows: Get-FileHash -Algorithm SHA256 file.txt

Python: import hashlib; hashlib.md5(b"password").hexdigest()

## Практика

Найди исходную строку для MD5: 5f4dcc3b5aa765d61d8327deb882cf99
"""
    },
    "crypto_caesar": {
        "id": "crypto_caesar",
        "category": "crypto",
        "title": "Шифр Цезаря",
        "short_description": "Классический шифр сдвига",
        "reading_time": 6,
        "difficulty": "Легко",
        "content": """
# Шифр Цезаря

Заменяет букву на букву со сдвигом на N позиций.

## Пример (сдвиг 3)

HELLO → KHOOR

## Команды

Linux: echo "KHOOR" | tr 'A-Za-z' 'X-ZA-Wx-za-w'

## Практика

Расшифруй: iodj{fdhvdu_lv_hdvb} (сдвиг 3)
"""
    },
    "crypto_aes_rsa": {
        "id": "crypto_aes_rsa",
        "category": "crypto",
        "title": "AES и RSA",
        "short_description": "Симметричное и асимметричное",
        "reading_time": 10,
        "difficulty": "Сложно",
        "content": """
# AES и RSA

## AES (симметричное)

Один ключ для шифрования и расшифровки. Быстрый.

## RSA (асимметричное)

Пара ключей: публичный и приватный. Медленный.

## Гибрид

RSA шифрует ключ AES, AES шифрует данные.

## Практика

Пройди комнату «Криптография».
"""
    },
    "web_sqli": {
        "id": "web_sqli",
        "category": "web",
        "title": "SQL Injection",
        "short_description": "Основы SQL-инъекций",
        "reading_time": 8,
        "difficulty": "Средне",
        "content": """
# SQL Injection

SQLi — внедрение SQL-кода в запрос.

## Пример

SELECT * FROM users WHERE id = 1 OR 1=1

## Обход авторизации

' OR '1'='1' --

## Защита

Параметризованные запросы, WAF.

## Практика

DVWA → SQL Injection → 1' OR '1'='1
"""
    },
    "web_xss": {
        "id": "web_xss",
        "category": "web",
        "title": "XSS",
        "short_description": "Межсайтовый скриптинг",
        "reading_time": 7,
        "difficulty": "Средне",
        "content": """
# XSS

Внедрение JavaScript на страницу.

## Типы

| Тип | Описание |
|-----|----------|
| Reflected | Сразу |
| Stored | Сохраняется |
| DOM-based | В JavaScript |

## Пример

<script>alert('XSS')</script>

## Практика

DVWA → XSS (Reflected)
"""
    },
    "web_csrf": {
        "id": "web_csrf",
        "category": "web",
        "title": "CSRF",
        "short_description": "Подделка запросов",
        "reading_time": 6,
        "difficulty": "Средне",
        "content": """
# CSRF

Заставляет пользователя выполнить нежелательное действие.

## Защита

CSRF-токены, SameSite cookie.

## Практика

DVWA → CSRF
"""
    },
    "web_file_upload": {
        "id": "web_file_upload",
        "category": "web",
        "title": "Загрузка файлов",
        "short_description": "Опасная уязвимость",
        "reading_time": 7,
        "difficulty": "Средне",
        "content": """
# Загрузка файлов

Можно загрузить PHP-shell на сервер.

## Защита

Проверять расширение, переименовывать файлы.

## Практика

DVWA → File Upload
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
| 4 | Транспортный | TCP, UDP |
| 3 | Сетевой | IP, ICMP |
| 1 | Физический | USB |

## Практика

Пройди комнату «Сетевые технологии».
"""
    },
    "network_dns": {
        "id": "network_dns",
        "category": "network",
        "title": "DNS",
        "short_description": "Система доменных имён",
        "reading_time": 6,
        "difficulty": "Средне",
        "content": """
# DNS

DNS преобразует домены в IP-адреса.

## Команды

Linux: nslookup google.com

Windows: Resolve-DnsName google.com

## Практика

Пройди комнату «Сетевые технологии».
"""
    },
    "network_tcp_udp": {
        "id": "network_tcp_udp",
        "category": "network",
        "title": "TCP vs UDP",
        "short_description": "Разница протоколов",
        "reading_time": 5,
        "difficulty": "Легко",
        "content": """
# TCP vs UDP

| Свойство | TCP | UDP |
|----------|-----|-----|
| Надёжность | Да | Нет |
| Скорость | Медленнее | Быстрее |
| Соединение | Устанавливает | Нет |

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

sudo command — от root

## Сеть

netstat -tulpn — порты

nmap -sV target — сканирование

## Практика

Пройди комнату «Linux для хакеров».
"""
    },
    "linux_permissions": {
        "id": "linux_permissions",
        "category": "linux",
        "title": "Права доступа",
        "short_description": "chmod, chown, SUID",
        "reading_time": 7,
        "difficulty": "Средне",
        "content": """
# Права доступа Linux

## Числа

| Число | Права |
|-------|-------|
| 7 | rwx |
| 6 | rw- |
| 5 | r-x |
| 4 | r-- |

## Примеры

chmod 777 file — все права всем

chmod 755 script.sh — rwx r-x r-x

## SUID

find / -perm -u=s -type f 2>/dev/null

## Практика

Пройди комнату «Linux для хакеров».
"""
    },
    "linux_scripts": {
        "id": "linux_scripts",
        "category": "linux",
        "title": "Bash-скрипты",
        "short_description": "Автоматизация",
        "reading_time": 7,
        "difficulty": "Средне",
        "content": """
# Bash-скрипты

## Простой скрипт

#!/bin/bash
echo "Hello, CyberLab!"

## Цикл

for i in {1..10}; do echo $i; done

## Условие

if [ -f file.txt ]; then echo "exists"; fi

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

Скрытие данных в наименее значимых битах.

## Инструменты

zsteg image.png

steghide extract -sf image.jpg

## Практика

Скачай CTF-файл и найди флаг.
"""
    },
    "stego_audio": {
        "id": "stego_audio",
        "category": "steganography",
        "title": "Аудио-стеганография",
        "short_description": "Скрытие в звуке",
        "reading_time": 5,
        "difficulty": "Средне",
        "content": """
# Аудио-стеганография

Скрытие данных в аудиофайлах.

## Инструменты

Sonic Visualiser — спектрограмма

Audacity — анализ

## Практика

Пройди комнату «Стеганография».
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

Дизассемблирование, декомпиляция.

## Установка

Скачай с ghidra-sre.org

## Практика

Пройди комнату «Reverse Engineering».
"""
    },
    "reverse_strings": {
        "id": "reverse_strings",
        "category": "reverse",
        "title": "Команда strings",
        "short_description": "Строки в бинарнике",
        "reading_time": 4,
        "difficulty": "Легко",
        "content": """
# Команда strings

Показывает текстовые строки в бинарном файле.

## Linux

strings binary.bin

## Windows

strings.exe binary.bin

## Практика

Скачай CTF-файл flag_binary.bin и найди флаг.
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

Поиск устройств в интернете.

## Фильтры

port:22

country:RU

product:Apache

## Практика

Пройди комнату «OSINT».
"""
    },
    "osint_exiftool": {
        "id": "osint_exiftool",
        "category": "osint",
        "title": "ExifTool — метаданные",
        "short_description": "Анализ метаданных",
        "reading_time": 5,
        "difficulty": "Легко",
        "content": """
# ExifTool

Показывает метаданные изображений.

## Linux

exiftool image.jpg

## Windows

exiftool.exe image.jpg

## Что искать

GPS-координаты, дату, камеру.

## Практика

Скачай CTF-файл и найди метаданные.
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