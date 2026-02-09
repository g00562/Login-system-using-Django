# Django Login System

A simple **Django-based Login & Task Management System** that allows users to register, log in, and manage personal tasks. This project demonstrates authentication, CRUD operations, and basic frontend styling using Django.

---

## 🚀 Features

* User registration and login system
* Secure authentication using Django auth
* Dashboard for logged-in users
* Create, update, and delete tasks
* Password validation with Django security rules
* Clean UI with custom CSS
* CSRF protection enabled

---

## 🛠 Tech Stack

* Python 3
* Django 5.x
* SQLite (default database)
* HTML + CSS

---

## 📂 Project Structure

```
login_system/
│
├── login/              # Main app
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── urls.py
│
├── login_system/       # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/g00562/Login-system-using-Django.git
cd Login-system-using-Django
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run migrations

```
python manage.py migrate
```

### 5. Start development server

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000
```

---

## 🔐 Usage

1. Register a new account
2. Log in with credentials
3. Add tasks from dashboard
4. Edit or delete tasks
5. Logout securely

---

## 📌 Notes

* This project is for learning and demonstration purposes.
* SQLite is used by default but can be replaced with other databases.
* Static files are stored inside the app for simplicity.
