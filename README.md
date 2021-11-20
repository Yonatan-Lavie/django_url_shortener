## Local development
#### To run this project in your development machine, follow these steps:
#### 1. Clone repo
    git clone https://github.com/Yonatan-Lavie/django_url_shortener.git

#### 2. Install dependencies:
    pip install -r requirements.txt
#### 3. Create a development database:
    cd app
    python manage.py makemigrations
    python manage.py migrate


#### 4. [additional] You can see urls table in django admin site :
    python manage.py createsuperuser 
    Username: <user-name>
    Email address: <admin@admin.dev>
    Password:
    Password (again):


#### 5. Run Server
    python manage.py runserver

## Open Browser on http://localhost:8000/

## Admin site http://localhost:8000/admin