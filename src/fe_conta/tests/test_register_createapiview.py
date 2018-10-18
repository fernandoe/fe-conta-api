from django.contrib.auth import get_user_model
from django.urls import reverse
from fe_core.factories import EntityFactory
from rest_framework import status
from rest_framework.test import APITestCase
import uuid


User = get_user_model()


class TestRegisterCreateAPIView(APITestCase):

    def setUp(self):
        self.entity = EntityFactory()
        self.BASE_URL = reverse('register')
        self.DATA_VALID = {
            'email': 'example@example.com',
            'password': 'password',
            'entity': str(self.entity.uuid)
        }

    def test_post_201(self):
        response = self.client.post(self.BASE_URL, self.DATA_VALID)
        # print("STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email=self.DATA_VALID['email'])
        self.assertEqual(self.entity, user.entity)
        self.assertTrue(user.check_password(self.DATA_VALID['password']))

    def test_when_entity_is_not_passed(self):
        del self.DATA_VALID['entity']
        response = self.client.post(self.BASE_URL, self.DATA_VALID)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email=self.DATA_VALID['email'])
        self.assertIsNone(user.entity)
        self.assertTrue(user.check_password(self.DATA_VALID['password']))

    def test_when_entity_does_not_exists(self):
        self.DATA_VALID['entity'] = str(uuid.uuid4())
        response = self.client.post(self.BASE_URL, self.DATA_VALID)
        # print("STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_response_email(self):
        response = self.client.post(self.BASE_URL, self.DATA_VALID)
        # print("STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content))
        self.assertEqual(self.DATA_VALID['email'], response.json()['email'])

    def test_when_email_already_exists(self):
        self.client.post(self.BASE_URL, self.DATA_VALID)
        response = self.client.post(self.BASE_URL, self.DATA_VALID)
        # print("STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_new_users_should_be_inactive(self):
        self.client.post(self.BASE_URL, self.DATA_VALID)
        user = User.objects.get(email=self.DATA_VALID['email'])
        self.assertTrue(user.is_active)
