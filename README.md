# CareerHub – Job Portal Backend

CareerHub is a job portal backend developed using Python, Django, and Django REST Framework. It helps users register, log in, view jobs, and apply for jobs.

## Technologies Used
- Python
- Django
- Django REST Framework
- SQLite
- JWT Authentication
- Postman
- Git and GitHub

## Features
- User registration and login.
- JWT-based authentication.
- Create, view, update, and delete job listings.
- Apply for jobs.
- View submitted job applications.
- Prevent duplicate job applications.
- Store data using SQLite and Django ORM.
- Test APIs using Postman.

## Installation and Setup

**1. Clone the repository**
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd CareerHub
```

**2. Create a virtual environment**
```bash
python -m venv env
```

**3. Activate the environment (Windows)**
```powershell
.\env\Scripts\Activate.ps1
```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

**5. Apply migrations**
```bash
python manage.py migrate
```

**6. Run the server**
```bash
python manage.py runserver
```

The server will run at `http://127.0.0.1:8000/`.

## API Testing
Use Postman to test registration, authentication, job management, and job application APIs.

## Author
Satya Pavani

GitHub: https://github.com/satyamadavarapu07-hue
