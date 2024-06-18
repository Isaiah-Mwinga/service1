# Customer Orders API

## Overview
A simple API service to manage customers and orders, built with Django REST Framework and PostgreSQL.

## Features
- REST API for managing customers and orders.
- Authentication and authorization via OpenID connect (auth0 okta).
- SMS alerts using Africa’s Talking SMS gateway.
- Unit tests with coverage checking.
- CI/CD setup with GitHub Actions.

## Setup

### Prerequisites
- Python 3.8+
- PostgreSQL

### accessing the service online
- Go to this path : https://service1-0omv.onrender.com/blog/auth/
- select continue with google and select your account
- after where you will be redirected to swagger UI which has the API endpoints

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Isaiah-Mwinga/service1.git
   ```
   install packages
   ```sh
   pip install -r requirements.txt
   ```
   create .env file and store your database and other variables

   create your postgres database and connect:
    ```
    export DB_NAME = "name'
    export DB_USER = 'db_user'
    export DB_USER_PASSWORD = 'your_password'
    export DB_HOST = localhost
    export DB_DB_PORT = 5432
    ```
    replace those credentials with real db credentials
    to run a virtual environment
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
    

    create the auth0 okta credentials
    ```
    Auth_Domain
    Auth_cliend_ID
    Auth_client_secret
   
