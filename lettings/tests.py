import pytest
from django.urls import reverse
from .models import Letting, Address


@pytest.mark.django_db
def test_index(client):
    "Tests the index view"
    response = client.get('/lettings/')
    assert response.status_code == 200
    assert 'Lettings' in response.content.decode()


@pytest.mark.django_db
def test_letting_page(client):
    "Tests a letting page"
    address = Address.objects.create(
        number=1,
        street='rue des tests',
        city='test_city',
        state='MO',
        zip_code=56000,
        country_iso_code='FRA'
    )
    letting = Letting.objects.create(
        title='Test',
        address=address
    )
    url = reverse('letting', kwargs={'letting_id': letting.id})
    response = client.get(url)
    assert response.status_code == 200
    assert 'Test' in response.content.decode()
