
import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

def subtract(x, y):
    return x - y

@pytest.mark.django_db
def test_user_create():
    User = get_user_model()
    User.objects.create_user(
        username='pytopia.ai@gmail.com',
        password='pytopiapassword'
    )
    assert User.objects.count() == 1

def test_subtract():
    assert subtract(3, 2) == 1
