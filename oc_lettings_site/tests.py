import pytest


@pytest.mark.django_db
def test_index(client):
    "Tests the index view"
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_404_view(client):
    "Tests the 404 view"
    response = client.get('/page_not_found')
    assert response.status_code == 404
