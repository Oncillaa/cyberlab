#!/usr/bin/env python3
"""
Модуль для работы с CTF-файлами
Автор: Oncilla (https://github.com/Oncillaa)
"""

import os
import base64
import hashlib
from pathlib import Path


CTF_FILES_DIR = Path("ctf_files")


def ensure_ctf_dir():
    """Создаёт директорию для CTF-файлов."""
    CTF_FILES_DIR.mkdir(exist_ok=True)


def generate_ctf_file(filename, content, encoding="utf-8"):
    """
    Генерирует CTF-файл с заданным содержимым.
    """
    ensure_ctf_dir()
    filepath = CTF_FILES_DIR / filename
    with open(filepath, 'w', encoding=encoding) as f:
        f.write(content)
    return filepath


def generate_base64_flag_file(flag, filename="flag_base64.txt"):
    """Создаёт файл с base64-закодированным флагом."""
    encoded = base64.b64encode(flag.encode()).decode()
    return generate_ctf_file(filename, encoded)


def generate_hex_flag_file(flag, filename="flag_hex.txt"):
    """Создаёт файл с hex-закодированным флагом."""
    encoded = flag.encode().hex()
    return generate_ctf_file(filename, encoded)


def generate_rot13_flag_file(flag, filename="flag_rot13.txt"):
    """Создаёт файл с ROT13-закодированным флагом."""
    result = []
    for char in flag:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return generate_ctf_file(filename, ''.join(result))


def generate_hash_flag_file(flag, filename="flag_hash.txt"):
    """Создаёт файл с MD5-хешем флага."""
    md5_hash = hashlib.md5(flag.encode()).hexdigest()
    return generate_ctf_file(filename, md5_hash)


def generate_binary_flag_file(flag, filename="flag_binary.bin"):
    """Создаёт бинарный файл с флагом внутри случайных данных."""
    ensure_ctf_dir()
    filepath = CTF_FILES_DIR / filename
    
    random_data = os.urandom(200)
    flag_bytes = flag.encode()
    marker = b"\x00\x00FLAG_START\x00\x00"
    marker_end = b"\x00\x00FLAG_END\x00\x00"
    
    with open(filepath, 'wb') as f:
        f.write(random_data)
        f.write(marker)
        f.write(flag_bytes)
        f.write(marker_end)
        f.write(os.urandom(100))
    
    return filepath


def generate_pcap_hint_file(flag, filename="network_capture_hint.txt"):
    """Создаёт файл с подсказкой о pcap-файле."""
    content = f"""
    Подсказка по анализу сетевого трафика:
    
    1. Открой pcap-файл в Wireshark
    2. Ищи HTTP-запросы
    3. Следуй за TCP-потоком (Follow TCP Stream)
    4. Флаг находится в одном из HTTP-ответов
    
    Ожидаемый формат флага: flag{{...}}
    """
    return generate_ctf_file(filename, content)


def generate_all_demo_files():
    """Создаёт все демонстрационные CTF-файлы."""
    ensure_ctf_dir()
    
    files_created = []
    
    files_created.append(generate_base64_flag_file("flag{base64_demo_flag}"))
    files_created.append(generate_hex_flag_file("flag{hex_demo_flag}"))
    files_created.append(generate_rot13_flag_file("flag{rot13_demo_flag}"))
    files_created.append(generate_hash_flag_file("password"))
    files_created.append(generate_binary_flag_file("flag{binary_demo_flag}"))
    files_created.append(generate_pcap_hint_file("flag{pcap_demo_flag}"))
    
    return files_created


def list_ctf_files():
    """Возвращает список всех CTF-файлов."""
    ensure_ctf_dir()
    files = []
    if CTF_FILES_DIR.exists():
        for f in CTF_FILES_DIR.iterdir():
            if f.is_file():
                files.append({
                    "name": f.name,
                    "size": f.stat().st_size,
                    "modified": f.stat().st_mtime
                })
    return sorted(files, key=lambda x: x["name"])


def get_ctf_file_path(filename):
    """Возвращает путь к CTF-файлу."""
    ensure_ctf_dir()
    filepath = CTF_FILES_DIR / filename
    if filepath.exists() and filepath.is_file():
        return filepath
    return None


if __name__ == "__main__":
    files = generate_all_demo_files()
    print("Созданы CTF-файлы:")
    for f in files:
        print(f"  - {f}")