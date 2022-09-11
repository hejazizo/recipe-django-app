import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user_with_email_successful():
    """Test creating a new user with an email is successful"""
    username = 'testuser'
    email = 'test@example.com'
    password = 'testpass123'
    user = get_user_model().objects.create_user(
        username=username,
        email=email,
        password=password,
    )

    assert user.username == username
    assert user.email == email
    assert user.check_password(password)


@pytest.mark.django_db
def test_new_user_email_normalized():
    """Test the email for a new user is normalized"""
    email = 'test@EXAMPLE.COM'

    sample_emails = [
        'test1@EXAMPLE.com', 'Test2@Example.com', 'TEST3@EXAMPLE.COM', 'test4@example.COM'
    ]

    for email in sample_emails:
        username, domain = email.split('@')
        normalized_email = f'{username}@{domain.lower()}'
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password='testpass123',
        )

        assert user.email == normalized_email


@pytest.mark.django_db
def test_new_user_invalid_email():
    """Test creating user with no email raises error"""
    with pytest.raises(ValueError):
        get_user_model().objects.create_user(None, 'testpass123')


@pytest.mark.django_db
def test_create_new_superuser():
    """Test creating a new superuser"""
    user = get_user_model().objects.create_superuser(
        username='testuser',
    )

    assert user.is_superuser
    assert user.is_staff
