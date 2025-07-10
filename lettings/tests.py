import pytest


@pytest.mark.django_db
def test_404_view(client):
    response = client.get('/page_not_found')
    assert response.status_code == 404
