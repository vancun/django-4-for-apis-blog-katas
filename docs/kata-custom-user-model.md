

```bash
# Revert admin migrations - admin will depend on accounts
python manage.py migrate admin zero
```


```bash
python manage.py startapp accounts
```

```python
# django_project/settings.py
INSTALLED_APPS = [
    # .........
    # 3rd Party
    'rest_framework',
    # Local
    "accounts.apps.AccountsConfig", # new
]
```


```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
```



```python
# django_project/settings.py
AUTH_USER_MODEL = "accounts.CustomUser" 
```


```bash
python manage.py makemigrations
# Apply migrations
python manage.py migrate
# Create superuser
python manage.py createsuperuser
```


Navigate the browser to the admin interface http://127.0.0.1:8000/admin/.

We cannot see the user model.

## Register User Model in Admin

```python
# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("name",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

```

We are using the default `UserCreationForm` and `UserChangeForm` classes.


```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "name",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
```

We defined `username` to be the first column in the list as it is to link to the user details. If we used `email`, the link would not be avialable in case the email is not provided.

Now user model is available.





