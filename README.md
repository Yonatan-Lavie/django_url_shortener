# Project desctiption.

>The purpose of this project is to create a more convenient and user-friendly way to access long URLs by generating shorter URLs that redirect to the original website.
>This can be particularly useful for sharing links on social media platforms or messaging apps, where character limits are often imposed. By using this project, 
>users can easily convert a lengthy URL into a concise and memorable link that is easier to share and remember.
## Local deployment
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
