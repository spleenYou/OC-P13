import pytest
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_index(client):
    response = client.get('/profiles/')
    assert response.status_code == 200
    assert 'Profiles' in response.content.decode()


@pytest.mark.django_db
def test_profile_page(client):
    user = User.objects.create(
        is_superuser=False,
        first_name='Super',
        last_name='Test',
        password='mdp_test',
        username='Test'
    )
    profile = Profile.objects.create(
        user=user,
        favorite_city='Test_city'
    )
    url = reverse('profile', kwargs={'username': profile.user.username})
    response = client.get(url)
    assert response.status_code == 200
