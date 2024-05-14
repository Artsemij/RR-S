import requests

# Параметры для создания устройств
devices_to_create = {
    'device1': {'name': 'Устройство 1', 'type': 'Тип 1'},
    'device2': {'name': 'Устройство 2', 'type': 'Тип 2'},
    # Добавьте остальные устройства здесь
}

# Параметры для запроса информации об устройствах
device_ids = ['device1', 'device2']  # Список идентификаторов устройств

# Параметры для обновления имен устройств
devices_to_update = {
    'device1': {'name': 'Новое имя устройства 1'},
    'device2': {'name': 'Новое имя устройства 2'},
    # Добавьте остальные устройства здесь
}

# Параметры для удаления устройств
devices_to_delete = ['device1', 'device2']  # Список идентификаторов устройств

# URL API
base_url = 'http://api.example.com/devices'

# Создание устройств
for device_id, device_data in devices_to_create.items():
    response = requests.post(f"{base_url}/{device_id}", json=device_data)
    print(f"Создание устройства {device_id}: {response.status_code}")

# Запрос информации об устройствах
for device_id in device_ids:
    response = requests.get(f"{base_url}/{device_id}")
    print(f"Информация об устройстве {device_id}: {response.json()}")

# Обновление имен устройств
for device_id, new_data in devices_to_update.items():
    response = requests.put(f"{base_url}/{device_id}", json=new_data)
    print(f"Обновление имени устройства {device_id}: {response.status_code}")

# Удаление устройств
for device_id in devices_to_delete:
    response = requests.delete(f"{base_url}/{device_id}")
    print(f"Удаление устройства {device_id}: {response.status_code}")