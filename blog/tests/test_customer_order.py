import pytest
from rest_framework.test import APIClient
from blog.models import Customer, Order

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def customer():
    return Customer.objects.create(name='John Doe', code='1234')

@pytest.fixture
def order(customer):
    return Order.objects.create(item='Test Item', amount=100, customer=customer)

@pytest.mark.django_db
def test_create_customer(api_client):
    response = api_client.post('/blog/customers/', {'name': 'Jane Doe','phone_number': '+254745101544', 'code': '5678'})
    assert response.status_code == 201

@pytest.mark.django_db
def test_create_order(api_client, customer):
    response = api_client.post('/blog/orders/', {'item': 'Another Item', 'amount': 50, 'customer': customer.id})
    assert response.status_code == 201