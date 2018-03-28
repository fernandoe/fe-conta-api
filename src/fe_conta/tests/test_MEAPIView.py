from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

# from .factories import UserFactory
# from ..models import Cliente

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



class TestMEAPIView(APITestCase):
    def test_get(self):
        response = self.client.get(reverse('me'))
        print("STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertIsNotNone(Cliente.objects.get(pk=response.data.get('uuid')))
