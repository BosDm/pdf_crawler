System requirements
===================

- Python = 2.7
- PostgreSQL = 9.4

Install development database
==========================

### PostgreSQL
     psql -h localhost -p 5432 postgres -c "CREATE DATABASE pdf_crawler;"
     psql -h localhost -p 5432 -d pdf_crawler -c "CREATE USER root_comeet WITH PASSWORD 'password123';"

     psql -h localhost -p 5432 -d pdf_crawler -c "ALTER ROLE root_comeet SET client_encoding TO 'utf8';"
     psql -h localhost -p 5432 -d pdf_crawler -c "ALTER ROLE root_comeet SET default_transaction_isolation TO 'read committed';"
     psql -h localhost -p 5432 -d pdf_crawler -c "ALTER ROLE root_comeet SET timezone TO 'UTC';"
     psql -h localhost -p 5432 -d pdf_crawler -c "GRANT ALL PRIVILEGES ON DATABASE pdf_crawler TO root_comeet;"

Install development server
==========================

### Obtain the code

    git clone git@gitlab.mgroupweb.com:python/cyberi.git cyberi
    cd cyberi

### Virtualenv

    http://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation
    or
    https://virtualenv.pypa.io/en/stable/installation/

Note: For creating virtualenv for python3 you should use -p flag. Example $ virtualenv -p python3 env_name

### Install python dependencies

Note: you should have your virtualenv or virtualenvwrapper already activated from step above. We also assume the start point here is the top directory of project.
Notr: http://joxi.ru/ZrJqeLGCPKlGAj # brew install libtiff libjpeg webp littlecms 

    pip install -r requirements.txt;

### Init DB

    python manage.py migrate

### Create first admin user

Note: Please use email - ad@ad.com and password - admin123 for compatibility.

    python manage.py createsuperuser

### Start project

    python manage.py runserver
