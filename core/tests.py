from rest_framework.test import APITestCase
from django.test import TransactionTestCase
from django.contrib.auth.models import User
from mock import Mock
from models import Country, Company
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status


class UserTests(APITestCase):

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


class CompanyTest(TransactionTestCase):

    # We need to reset primary key between tests
    reset_sequences = True

    # One API client for all tests
    client = None

    # One token for all tests
    token = None

    # API client for hacker
    h_client = None

    # Token for hacker
    h_token = None

    # Anonymous user API client
    a_client = APIClient()

    def setUp(self):
        """
        Set up class dependencies 
        """
        # Create a user and authenticate him for further use of his token
        User(**Mock.user_a).save()
        current_user = User.objects.first()
        self.__class__.token = Token.objects.create(user=current_user)
        self.__class__.client = APIClient()
        header = 'Token ' + self.__class__.token.key
        self.__class__.client.credentials(HTTP_AUTHORIZATION=header)

        # Create a hacker user and authenticate him for further use of his token
        User(**Mock.user_b).save()
        hacker = User.objects.get(pk=2)
        self.__class__.h_token = Token.objects.create(user=hacker)
        self.__class__.h_client = APIClient()
        hacker_header = 'Token ' + self.__class__.h_token.key
        self.__class__.h_client.credentials(HTTP_AUTHORIZATION=hacker_header)

        # Create a country, needed for its foreign key
        Country(**Mock.country).save()

    def test_create_company(self):
        """
        Ensure users can create companies 
        """
        # Create a company
        self.__class__.client.post('/companies/', Mock.company_a, format='json')
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.first().company_name, Mock.company_a['company_name'])

    def test_update_company(self):
        """
        Ensure users can update companies 
        """
        # Create a company
        company_a = self.__class__.client.post('/companies/', Mock.company_a, format='json')
        uri = '/companies/' + str(company_a.data['id']) + '/'

        # Update the newly created company
        response = self.__class__.client.put(uri, Mock.company_a_edited, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['company_name'], Mock.company_a_edited['company_name'])

        # Hackers should not be able to update companies of other users
        response = self.__class__.h_client.put(uri, Mock.company_a_edited, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Anonymous users should not be able to update any companies
        response = self.__class__.a_client.put(uri, Mock.company_a_edited, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update_company(self):
        """
        Ensure users can partial-update companies 
        """
        # Create a company
        company_a = self.__class__.client.post('/companies/', Mock.company_a, format='json')
        uri = '/companies/' + str(company_a.data['id']) + '/'

        # Partial-update the newly created company
        response = self.__class__.client.patch(uri, Mock.company_a_patched, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['slug_name'], Mock.company_a_patched['slug_name'])

        # Hackers should not be able to partial-update companies of other users
        response = self.__class__.h_client.patch(uri, Mock.company_a_patched, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Anonymous users should not be able to partial-update any companies
        response = self.__class__.a_client.patch(uri, Mock.company_a_patched, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_company(self):
        """
        Ensure users can delete companies 
        """
        # Create a company
        company_a = self.__class__.client.post('/companies/', Mock.company_a, format='json')
        self.assertEqual(Company.objects.count(), 1)
        uri = '/companies/' + str(company_a.data['id']) + '/'

        # Hackers should not be able to delete companies of other users
        response = self.__class__.h_client.delete(uri)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Anonymous users should not be able to partial-update any companies
        response = self.__class__.a_client.delete(uri)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Delete the newly created company
        response = self.__class__.client.delete(uri)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Company.objects.count(), 0)

