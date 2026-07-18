# Django REST API - User Profiles

## Project Overview

This project is a REST API built using Django and Django REST Framework (DRF). It manages user profiles and supports CRUD (Create, Read, Update, Delete) operations. Only authenticated users can access the API, and each user can manage only their own profile.

---

## Technologies Used

- Python 3
- Django 6
- Django REST Framework
- django-filter
- SQLite3

---

## Features

- User Authentication (Session Authentication)
- Create User Profile
- View User Profile
- Update User Profile
- Delete User Profile
- Custom Permission (Users can only access their own profile)
- Filter by Created Date
- Search by Username and Bio
- Order by ID
- Pagination (5 records per page)
- JSON Responses

---

## Project Structure

```
myapi/
│
├── manage.py
├── db.sqlite3
│
├── myapi/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── users/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── permissions.py
    ├── filters.py
    ├── urls.py
    └── admin.py
```

---

## Installation

### Clone or Extract the Project

Move into the project folder.

```bash
cd myapi
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Virtual Environment

Windows

```bash
env\Scripts\activate
```

### Install Required Packages

```bash
pip install django djangorestframework django-filter
```

---

## Database Setup

Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

---

## Run the Project

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## Login

Admin Panel

```
http://127.0.0.1:8000/admin/
```

API Login

```
http://127.0.0.1:8000/api-auth/login/
```

---

## API Endpoints

| Method | Endpoint | Description |
| GET | /api/users/ | View Profile |
| POST | /api/users/ | Create Profile |
| GET | /api/users/<id>/ | View Single Profile |
| PUT | /api/users/<id>/ | Update Profile |
| DELETE | /api/users/<id>/ | Delete Profile |

---

## Search

```
/api/users/?search=Ayush
```

---

## Filter

```
/api/users/?created_at=2026-07-14
```

---

## Ordering

Ascending

```
/api/users/?ordering=id
```

Descending

```
/api/users/?ordering=-id
```

---

## Pagination

The API returns **5 records per page**.

Example:

```
/api/users/?page=2
```

---

## Notes

- Session Authentication is used.
- Each user can create only one profile.
- Users can only view and update their own profile.
- All API responses are returned in JSON format.

---

## Author

Ayush Kumar Choudhary