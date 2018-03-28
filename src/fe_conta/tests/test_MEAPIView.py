from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from .factories import UserFactory

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class TestMEAPIView(APITestCase):

    def test_get_401(self):
        response = self.client.get(reverse('me'))
        # print("STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEquals(response.data['detail'], 'Authentication credentials were not provided.')

    def test_get_full(self):
        user = UserFactory()
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.get(reverse('me'))
        # print("STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, {
            'email': user.email,
            'entity': str(user.entity.pk),
        })

    def test_get_just_email(self):
        user = UserFactory(entity=None)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.get(reverse('me'))
        # print("STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, {
            'email': user.email
        })
