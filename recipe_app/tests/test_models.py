from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        """Test creating a new user with email and password is successful"""
        email = 'xyz@gmail.com'
        password = 'abcde123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_for_the_normalize_email(self):
        """Test if the email entered has been normalized"""
        email = 'xyz@GMAIL.COM'
        user = get_user_model().objects.create_user(email=email, password='password')

        self.assertEqual(user.email, email.lower())

    def test_check_email_validation(self):
        """Test users creating email without providing email address raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password')

    def test_check_if_user_is_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'abc@gmail.com',
            'password'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
