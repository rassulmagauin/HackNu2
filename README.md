
# HackNu2 Project

This is a Django-based web application focused on courier and order management. The project is structured into several key components, each serving a specific role within the application.

## Key Components

### manage.py

This is the command-line utility for administrative tasks. It contains the main function and uses modules such as `core`, `django`, `environ`, `management`.

### requirements.txt

This file lists all Python libraries that your project depends on. You can install them using pip.

### courier

This directory contains the models, views, serializers, and admin configuration for the courier component of the application. The main model is `Courier` with fields like `company_name`, `name`, `phone_number`, and `order`.

### order

This directory contains the models, views, serializers for the order component of the application. The main models are `Order` and `Address` with various fields.

### egov_delivery

This directory seems to be the main Django application directory. It contains settings for the application in `settings.py`, URL configurations in `urls.py`, and ASGI and WSGI configurations for asynchronous and synchronous servers.

### serviceCenter

This directory seems to be another component of the application but doesn't have much content in it.

### migrations

These directories in `courier` and `order` contain Django database migrations. These are responsible for creating, modifying, or deleting database tables based on the models.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python and pip installed on your machine. You can check if you have these available by running:

```bash
python --version
pip --version
```

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/rassulmagauin/hacknu2.git
```

Navigate to the project directory:

```bash
cd yourrepository
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Now, you can run the server:

```bash
python manage.py runserver
```

Open your web browser and visit `http://127.0.0.1:8000/` to see the application running.

## Running the tests

To run the tests for this system, you can use the following command:

```bash
python manage.py test
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](https://www.django-rest-framework.org/) - Toolkit for building Web APIs.
