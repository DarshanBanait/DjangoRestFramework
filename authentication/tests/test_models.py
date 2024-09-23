from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

    def test_creates_user(self):
        user=User.objects.create_user('testuser', 'test@gmail.com', 'testpassword@123')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'test@gmail.com')

    def test_creates_super_user(self):
        user=User.objects.create_superuser('testuser', 'test@gmail.com', 'testpassword@123')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'test@gmail.com')

    def test_raises_error_when_no_username(self):
        self.assertRaises(ValueError, User.objects.create_user,username= '', email= 'test@gmail.com',password= 'testpassword@123')
        
    def test_raises_error_when_no_email(self):
        self.assertRaises(ValueError, User.objects.create_user,username= 'testuser', email= '',password= 'testpassword@123')

    def test_creates_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='testuser', email='test@gmail.com', password='testpassword@123', is_staff=False)

    def test_creates_super_user_with_is_staff_status_as_true(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='testuser', email='test@gmail.com', password='testpassword@123', is_superuser=False)
        