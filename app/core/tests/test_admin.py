import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse


@pytest.fixture
def admin_user():
    return get_user_model().objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='testpass123'
    )

@pytest.fixture
def user():
    return get_user_model().objects.create_user(
        username='testuser',
        email='user@example.com',
        password='testpass123'
    )

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db
def test_list_users(admin_user, client):
    client.force_login(admin_user)
    url = reverse('admin:core_user_changelist')
    res = client.get(url)

    assert res.status_code == 200
