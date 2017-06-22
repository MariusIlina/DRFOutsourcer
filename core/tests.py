from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from mock import Mock
from models import Country, Company
from rest_framework.test import APIClient


class ApiTests(APITestCase):

    token_a = None
    token_b = None

    def setUp(self):

        # -----------------------------------
        # Create mock country
        # -----------------------------------
        country = Country()
        country.country_name = Mock.country['country_name']
        country.country_code = Mock.country['country_code']
        country.save()

        # -----------------------------------
        # Create and authenticate mock user A
        # -----------------------------------
        self.client.post('/register/', Mock.user_a, format='json')
        auth_a = self.client.post('/token-auth/', Mock.credentials_a, format='json')
        self.__class__.token_a = auth_a.data['token']

        # -----------------------------------
        # Create and authenticate mock user B
        # -----------------------------------
        self.client.post('/register/', Mock.user_b, format='json')
        auth_b = self.client.post('/token-auth/', Mock.credentials_b, format='json')
        self.__class__.token_b = auth_b.data['token']

    def test_user_created(self):
        """
        Ensure that 2 users were created during setUp
        """
        self.assertTrue(User.objects.count(), 2)

    def test_user_authenticated(self):
        """
        Ensure users were authenticated during setUp 
        """
        self.assertTrue(len(self.__class__.token_a) > 0)
        self.assertTrue(len(self.__class__.token_b) > 0)

    def test_create_company(self):
        """
        Ensure user can create a company
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.__class__.token_a)
        response = client.post('/companies/', Mock.company_a, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(response.data['company_name'], Mock.company_a['company_name'])
