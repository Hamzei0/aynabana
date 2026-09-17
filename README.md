# Aynabana Django Project

این پروژه با **Django 5.2.8** توسعه داده شده است.

این راهنما مراحل راه‌اندازی پروژه پس از Clone کردن Repository را توضیح می‌دهد.

---

## Requirements

قبل از شروع، موارد زیر باید روی سیستم نصب باشند:

* Python
* Git
* pip

> در محیط توسعه فعلی، به‌جای PostgreSQL از SQLite استفاده شده است؛ بنابراین برای اجرای لوکال پروژه نیازی به نصب PostgreSQL نیست.

---

## 1. Clone کردن پروژه

ابتدا Repository را Clone کنید:

```bash
git clone <YOUR_REPOSITORY_URL>
```

و وارد پوشه پروژه شوید:

```bash
cd aynabana
```

---

## 2. ساخت Virtual Environment

برای ساخت محیط مجازی Python:

```bash
python -m venv venv
```

در صورت نیاز می‌توانید از `python3` نیز استفاده کنید:

```bash
python3 -m venv venv
```

---

## 3. فعال کردن Virtual Environment

در Linux:

```bash
source venv/bin/activate
```

بعد از فعال شدن، باید چیزی شبیه این در ابتدای Terminal نمایش داده شود:

```text
(venv)
```

---

## 4. نصب Dependencyها

برای استفاده از تنظیمات پروژه، پکیج‌های زیر مورد نیاز هستند:

```bash
pip install django
pip install python-decouple
pip install python-dotenv
```

همچنین پروژه از پکیج‌های دیگری مانند موارد زیر استفاده می‌کند:

* django-jalali
* django-allauth
* django-ckeditor
* django-rosetta
* psycopg

در صورت وجود فایل `requirements.txt`، روش پیشنهادی نصب تمام Dependencyها:

```bash
pip install -r requirements.txt
```

---

## 5. ساخت فایل `.env`

فایل `.env` به دلیل داشتن اطلاعات حساس در Git Repository قرار نمی‌گیرد.

در ریشه پروژه یک فایل با نام زیر ایجاد کنید:

```text
.env
```

نمونه تنظیمات مورد نیاز:

```env
SECRET_KEY=django-insecure-local-development-key

DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True

DB_ENGINE=django.db.backends.postgresql
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432

DJANGO_ZARINPAL_MERCHANT_ID=
```

> مقادیر واقعی Secret Key، رمز عبور ایمیل، اطلاعات دیتابیس و Merchant ID نباید در GitHub قرار بگیرند.

---

# Local Development with SQLite

در محیط توسعه لوکال، برای جلوگیری از نیاز به PostgreSQL، تنظیمات Database به SQLite تغییر داده شده است.

در فایل:

```text
config/settings.py
```

تنظیمات PostgreSQL:

```python
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="5432"),
    }
}
```

با تنظیمات SQLite جایگزین می‌شود:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

در این حالت Django دیتابیس را در فایل زیر ایجاد می‌کند:

```text
db.sqlite3
```

---

## 6. تنظیم HTTPS برای محیط Local

تنظیمات پروژه در محیط Production برای HTTPS فعال هستند، اما Django development server به صورت پیش‌فرض HTTPS را پشتیبانی نمی‌کند.

برای اجرای پروژه به صورت Local، در:

```text
config/settings.py
```

تنظیمات زیر باید به شکل زیر باشند:

```python
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
```

سپس پروژه را با HTTP اجرا کنید:

```text
http://127.0.0.1:8000/
```

> این تنظیمات فقط برای محیط Development هستند. در Production نباید HTTPS غیرفعال شود.

---

## 7. اجرای Migrationها

بعد از تنظیم Database، Migrationها را اجرا کنید:

```bash
python manage.py migrate
```

اگر Migrationها با موفقیت اجرا شوند، فایل SQLite ساخته خواهد شد:

```text
db.sqlite3
```

---

## 8. اجرای Development Server

برای اجرای پروژه:

```bash
python manage.py runserver
```

در صورت موفقیت، خروجی مشابه زیر مشاهده می‌شود:

```text
Starting development server at http://127.0.0.1:8000/
```

سپس در مرورگر باز کنید:

```text
http://127.0.0.1:8000/
```

---

# Project Structure

ساختار کلی پروژه شامل Django Apps مختلف است:

```text
aynabana/
│
├── config/
├── accounts/
├── pages/
├── shop/
├── cart/
├── persian_translate/
├── articles/
├── orders/
├── services/
├── payment/
├── templates/
├── static/
├── manage.py
├── db.sqlite3
└── venv/
```

---

# Important Notes

### `.env`

فایل `.env` نباید Commit شود.

در `.gitignore` باید موارد زیر وجود داشته باشند:

```gitignore
venv/
.env
__pycache__/
*.pyc
db.sqlite3
```

---

### Virtual Environment

پوشه `venv` نیز نباید داخل Git قرار بگیرد.

هر توسعه‌دهنده باید بعد از Clone کردن Repository، Virtual Environment خودش را ایجاد کند:

```bash
python -m venv venv
```

---

### SQLite

`db.sqlite3` برای Development مناسب است.

اگر پروژه در Production با PostgreSQL اجرا می‌شود، تنظیمات Production باید از PostgreSQL استفاده کنند.

---

# Common Commands

فعال کردن Virtual Environment:

```bash
source venv/bin/activate
```

اجرای Migration:

```bash
python manage.py migrate
```

ساخت Superuser:

```bash
python manage.py createsuperuser
```

اجرای Development Server:

```bash
python manage.py runserver
```

غیرفعال کردن Virtual Environment:

```bash
deactivate
```

---

# Development Workflow

برای راه‌اندازی مجدد پروژه بعد از Clone:

```bash
git clone <YOUR_REPOSITORY_URL>
cd aynabana

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

سپس:

```text
http://127.0.0.1:8000/
```

را در مرورگر باز کنید.
