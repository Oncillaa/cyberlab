#!/usr/bin/env python3
"""
Модуль управления виртуальными машинами (Docker-контейнерами)
Автор: Oncilla (https://github.com/Oncillaa)
"""

import subprocess
import json
import os
from datetime import datetime


class VMManager:
    """
    Класс для управления Docker-контейнерами с уязвимыми машинами.
    """
    
    # Описание доступных VM
    # ВАЖНО: container_port — порт ВНУТРИ контейнера, host_port — порт на хосте
    VMS = {
        "dvwa": {
            "id": "dvwa",
            "name": "DVWA",
            "full_name": "Damn Vulnerable Web Application",
            "description": "Уязвимое веб-приложение для тестирования SQLi, XSS, CSRF",
            "image": "vulnerables/web-dvwa",
            "host_port": 8080,
            "container_port": 80,
            "difficulty": "Легко",
            "icon": "🐳"
        },
        "juice-shop": {
            "id": "juice-shop",
            "name": "Juice Shop",
            "full_name": "OWASP Juice Shop",
            "description": "Современное уязвимое веб-приложение с множеством заданий",
            "image": "bkimminich/juice-shop",
            "host_port": 3000,
            "container_port": 3000,
            "difficulty": "Средне",
            "icon": "🧃"
        },
        "webgoat": {
            "id": "webgoat",
            "name": "WebGoat",
            "full_name": "OWASP WebGoat",
            "description": "Обучающее приложение по веб-уязвимостям",
            "image": "webgoat/webgoat-8.0",
            "host_port": 8081,
            "container_port": 8080,
            "difficulty": "Средне",
            "icon": "🐐"
        }
    }
    
    @staticmethod
    def check_docker():
        """Проверяет, установлен ли Docker."""
        try:
            result = subprocess.run(
                ["docker", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False
        except Exception:
            return False
    
    @staticmethod
    def list_running_containers():
        """Возвращает список запущенных контейнеров."""
        try:
            result = subprocess.run(
                ["docker", "ps", "--format", "{{json .}}"],
                capture_output=True,
                text=True,
                timeout=10
            )
            containers = []
            for line in result.stdout.strip().split('\n'):
                if line:
                    containers.append(json.loads(line))
            return containers
        except Exception:
            return []
    
    @staticmethod
    def start_container(vm_id):
        """Запускает контейнер VM."""
        vm = VMManager.VMS.get(vm_id)
        if not vm:
            return (False, "VM не найдена")
        
        try:
            container_name = f"cyberlab-{vm_id}"
            
            # Проверяем, существует ли контейнер
            result = subprocess.run(
                ["docker", "ps", "-a", "--filter", f"name={container_name}", "--format", "{{.Names}}"],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if container_name in result.stdout:
                # Контейнер существует — проверяем статус
                status_result = subprocess.run(
                    ["docker", "ps", "--filter", f"name={container_name}", "--format", "{{.Names}}"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                if container_name in status_result.stdout:
                    return (False, f"{vm['name']} уже запущена")
                else:
                    # Запускаем существующий контейнер
                    start_result = subprocess.run(
                        ["docker", "start", container_name],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    if start_result.returncode == 0:
                        return (True, f"{vm['name']} запущена на порту {vm['host_port']}. Подожди 30 секунд для загрузки.")
                    else:
                        return (False, f"Ошибка запуска: {start_result.stderr[:200]}")
            
            # Запускаем новый контейнер
            result = subprocess.run(
                [
                    "docker", "run", "-d",
                    "--name", container_name,
                    "-p", f"{vm['host_port']}:{vm['container_port']}",
                    "--restart", "unless-stopped",
                    vm["image"]
                ],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                return (True, f"{vm['name']} запущена на порту {vm['host_port']}. Подожди 30 секунд для загрузки.")
            else:
                return (False, f"Ошибка запуска: {result.stderr[:200]}")
        
        except subprocess.TimeoutExpired:
            return (False, "Превышено время ожидания (120 секунд)")
        except Exception as e:
            return (False, f"Ошибка: {str(e)[:200]}")
    
    @staticmethod
    def stop_container(vm_id):
        """Останавливает контейнер VM."""
        try:
            container_name = f"cyberlab-{vm_id}"
            
            result = subprocess.run(
                ["docker", "stop", container_name],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                return (True, "VM остановлена")
            else:
                return (False, f"Ошибка остановки: {result.stderr[:200]}")
        
        except Exception as e:
            return (False, f"Ошибка: {str(e)[:200]}")
    
    @staticmethod
    def get_container_status(vm_id):
        """Возвращает статус контейнера."""
        try:
            result = subprocess.run(
                ["docker", "ps", "--filter", f"name=cyberlab-{vm_id}", "--format", "{{.Status}}"],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip() if result.stdout.strip() else None
        except Exception:
            return None
    
    @staticmethod
    def get_vm_list_with_status():
        """Возвращает список VM с их статусом."""
        vms = []
        for vm_id, vm in VMManager.VMS.items():
            status = VMManager.get_container_status(vm_id)
            vms.append({
                **vm,
                "status": "running" if status else "stopped",
                "status_text": status if status else "Остановлена"
            })
        return vms