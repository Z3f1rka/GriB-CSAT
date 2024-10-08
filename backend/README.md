# GribCSAT Backend
*Команды прописаны для **bash** терминалов*

### Запуск проекта

Запускать из папки backend:

Переход в папку backend
```bash
cd backend
```

Создание .env файла(*bash*)
```bash
cp .env.template .env
```

Создание среды
```bash
python -m venv .venv
```

Активация среды(***для Windows***)
```bash
source .venv/Scripts/activate
```

Активация среды(***для Linux***)
```bash
source .venv/bin/activate
```

Установка зависимостей:
```bash
pip install -r requirements.txt
```

Запуск сервера
```bash
python server.py
```