# Swagger User Interface for API Kata


1. Install `drf-yasg`
2. Configure Swagger in `urls.py`
3. Add `drf_yasg` to `INSTALLED_APPS`
4. Explore the Swagger UI

Pre-requisites:

* [REST APIs Kata](kata-rest-apis.md)


## Install `drf-yasg`

Update the `requirements.txt` by adding the `drf-yasg` package to it.


```
# requirements.txt
django
djangorestframework
drf-yasg  # new
pytest
pytest-cov
pytest-django
python-dotenv
```

Reinstall packages:

```bash
pip install -U -r requirements.txt
```

## Configure Swagger in `urls.py`

```python
# django_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="API documentation for the Blog application",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
]
```

## Add `drf_yasg` to `INSTALLED_APPS`

```python
# django_project/settings.py
# .......
INSTALLED_APPS = [
    # ..............
    # 3rd Party
    # ..............
    "drf_yasg",
    # Local
    # ..............
]
```

## Explore the Swagger UI

Run Django server:

```bash
python manage.py runserver
```

Navigate the  browser to http://127.0.0.1:8000/docs/.
