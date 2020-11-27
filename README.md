# Employee Management System

This repository consists of the basic functionalities for a SAAS EMS using Django.

## Deployment

### Setup
```bash
pip install -r requirements.txt
```

### Run in dev
```bash
virtualenv venv
source venv/bin/activate
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver