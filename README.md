# 🍼 Family – Django REST API for Moms Support Platform

**Family** — это веб-платформа, созданная для поддержки молодых матерей, невесток и девушек в вопросах ухода за ребенком, питания, первой медицинской помощи и организации личных данных.  
Этот репозиторий содержит **backend**-часть проекта, реализованную на Django + DRF с JWT-авторизацией, социальными входами и полноценной документацией Swagger.

## 🚀 Основные возможности API

- 🔐 Регистрация и авторизация (в т.ч. через Google и Facebook)
- 👶 Тесты для оценки развития ребенка
- 📄 Загрузка и хранение личных и медицинских документов
- 🍽️ Раздел с рецептами и видеоуроками по питанию
- 🆘 Информация по оказанию первой помощи
- 💬 Связь между матерями и врачами
- 🧑‍⚕️ Кабинеты врачей и администраторов
- 📑 Полная автогенерация Swagger-документации

## ⚙️ Технологии

- **Backend**: Django 5.1.7 + Django REST Framework
- **Auth**: JWT + dj-rest-auth + django-allauth
- **Документация API**: drf-spectacular (Swagger / Redoc)
- **БД**: SQLite (для dev), PostgreSQL (на проде)
- **Фронтенд**: React (отдельный репозиторий или Netlify)
- **Деплой**: PythonAnywhere + Netlify
- **Email**: SMTP с подтверждением почты

## 🧠 Архитектура

- `custom_auth` — кастомная модель пользователя с email-логином
- `profile` — модели и эндпоинты для хранения информации о матерях и детях
- `blogs` — статьи и рекомендации для родителей
- `media/` — хранилище файлов и документов
- Поддержка CORS, CSRF, HTTPS и безопасной передачи данных

## 🛡️ Безопасность

- JWT токены с обновлением и blacklist
- Верификация email при регистрации
- Защита от XSS и SQL-инъекций
- Поддержка CORS + доверенные фронтенд-источники

## 📸 Swagger UI

[Посмотреть Swagger UI](https://family1pro.pythonanywhere.com/api/schema/docs)  

## 🏁 Быстрый старт

```bash
git clone https://github.com/yourusername/family-backend.git
cd family-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Настрой .env файл
python manage.py migrate
python manage.py runserver
```

##🧪 Тесты
Тесты можно запускать с помощью:

```bash
python manage.py test
```

📬 Контакты
Разработчик: Shavkat Kurbanov
Telegram: https://t.me/shava_007
Почта: shavkatkurbanov065@gmail.com

