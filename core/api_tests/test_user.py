from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from core.mock import Mock


class UserTest(APITestCase):

    def setUp(self):
        """
        Set up class dependencies 
        """
        self.client.post('/register/', Mock.user_a, format='json')

    def test_create_user(self):
        """
        Ensure users can be created
        """
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, Mock.user_a['username'])

    def test_auth_user(self):
        """
        Ensure users can be authenticated 
        """
        response = self.client.post('/token-auth/', Mock.credentials_a, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data['token']) > 0)
