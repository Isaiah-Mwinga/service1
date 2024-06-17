from django.shortcuts import render, redirect
import jwt.algorithms
import requests
import os
from dotenv import load_dotenv
load_dotenv()
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from .tasks import send_order_alert

import json
import jwt


auth0_domain = os.environ.get('AUTH0_DOMAIN')
client_id = os.environ.get('AUTH0_CLIENT_ID')
client_secret = os.environ.get('AUTH0_CLIENT_SECRET')
redirect_uri = "https://github.com/Isaiah-Mwinga"
issuer = f"https://{auth0_domain}/"


def oidc_authenticate(request):
  auth0_authorization_url = f"http://{auth0_domain}/authorize"
  params = {
      "response_type": "code",
      "client_id": client_id,
      "redirect_uri": redirect_uri,
      "scope": "openid profile email",
  }

  return redirect( f"{auth0_authorization_url}?{'&'.join([f'{key}={value}' for key, value in params.items()])}" )


def oidc_callback(request):
  jwks_endpoint = os.environ.get('AUTH0_JWKS_ENDPOINT')
  authorization_code = request.GET.get("code")

  # exchanging code for token
  token_url = f'https://{auth0_domain}/oauth/token'
  token_data = {
      "grant_type": "authorization_code",
      "client_id": client_id,
      "client_secret": client_secret,
      "code": authorization_code,
      "redirect_uri": redirect_uri
  }

  token_response = requests.post(token_url, data=token_data)
  token_response_data = token_response.json()

  print("token response: ", token_response_data)

  id_token = token_response_data['id_token']

  ## token validation
  id_token_jwt_header = jwt.get_unverified_header(id_token)
  jwks = requests.get(jwks_endpoint).json()
  public_key = None
  for jwk in jwks['keys']:
    if jwk['kid'] == id_token_jwt_header['kid']:
      public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
  if public_key is None:
    raise Exception("Public key not found")
  
  try:
    decoded_data = jwt.decode(id_token, public_key, audience=client_id, issuer=issuer, algorithms=['RS256'])
    return JsonResponse(decoded_data)
  except jwt.exceptions.DecodeError as e:
    print("Invalid Token: ", e)
    #return JsonResponse({"error": "Invalid Token"})

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.save()
        send_order_alert(order.customer, order)
