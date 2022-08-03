# Api_testing

REST API Testing Using Python and WordPress

Introduction

This program is REST API testing using python. The programming language 
used is python 3 and the application to test is WordPress.

Requirement

    1. python Python 3.9 or up (https://www.python.org)
    2. OS Windows or Linux
    3. Install the Requirements.txt with the command line:
        "pip install -r requirements.txt" for Windows
        "pip3 install -r requirements.txt" for Linux
    4. Install Xampp and WordPress

Description Program
    
    Were tested the endpoinst for the page feature of WordPress:
    1. Get all pages Request
    2. Get page by id Request
    3. Delete page Request
    4. Edit page Request
    5. Post page Request

Steps Run Program

    1. Install Xampp [https://www.apachefriends.org/es/index.html]
    2. Install WordPress [https://wordpress.org/download/]
    3. Clone or pull the repo.
    4. Inside the project you will need a file called .env (at the same level of the file main.py) with 
    the following format:
        BASE_URI = 'http://<Domain>/<wordpress-project>/wp-json'
        USER_NAME = '<your-username>'
        PASSWORD = '<your-password>'
        AUTHORIZATION=Bearer
        status_code = 1
        dict_response = 0
        json_response = 2
    You must replace the BASE_URI, USER_NAME and PASSWORD according to the project and credentials 
    used in wordpress
    NOTE: the username and pasword are the same of the needed for acced the WordPress page,
    The Domain page in the BASE_URI variable is the domain that you gonna use (localhost if use default)
    The wordpress-project in BASE_URI variable is the name of your project in wordpress

Author
    Amilcar Barriento
    Said Garnica
    Rodrigo Coa
    Freddy Claros
    