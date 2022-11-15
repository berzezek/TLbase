# TLGROUP TECHNICAL PREVIEW

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)

## Setup

First, clone this repo to your local system. After you clone the repo, make sure
to run the `setup.py` file, so you can install any dependencies you may need. To
run the `setup.py` file, run the following command in your terminal.

```console
pip install -r requirements.txt .
```
change your base.settings.py like this:

```

    INSTALLED_APPS = [
        ...
        'base',
        'rest_framework',
        'corsheaders',
        'django_extensions',
    ]
    


    MIDDLEWARE = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]


    CORS_ORIGIN_ALLOW_ALL = True
    

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cn73530_tlgroup',
        'USER': 'cn73530_tlgroup',
        'PASSWORD': 'Aa20102010',
        'HOST': '188.225.40.227',
        'PORT': '3306',
    }
}
    ...

    REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
    
    ...
    
        
```

2. Include the polls URLconf in your project urls.py like this::

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('base.api.urls')),
]


3. Run ``python manage.py migrate`` 
    (or ``python manage.py migrate`` on macOS or Linux) to create the department and employees models.


4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a department and employee (you'll need the Admin app enabled).


5. Visit http://127.0.0.1:8000/ to view data.


6. Visit https://documenter.getpostman.com/view/16706893/2s8YehVHSC to view API documentation.


This will install all the dependencies listed in the `setup.py` file. Once done
you can use the library wherever you want.

## Usage

Here is a simple example of using the `TLGROUP` library to get data about an employee working in a department.


