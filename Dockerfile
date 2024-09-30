# استفاده از تصویر پایه Python
FROM python:3.12

# تنظیم دایرکتوری کاری
WORKDIR D:\all project\tamrin\BookStore

# کپی فایل‌های مورد نیاز
COPY requirements.txt .

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# کپی بقیه فایل‌های پروژه
COPY . .

# تنظیم متغیر محیطی
ENV PYTHONUNBUFFERED 1

# فرمان برای اجرای برنامه
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
