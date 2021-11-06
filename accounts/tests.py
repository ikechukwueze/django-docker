from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class UserAccountTests(TestCase):

    def test_create_user(self):
        UserAccount = get_user_model()
        new_user = UserAccount.objects.create_user(
            username='michael',
            email='michael@email.com',
            password='testpass123'
        )

        self.assertEqual(new_user.username, 'michael')
        self.assertEqual(new_user.email, 'michael@email.com')
        self.assertTrue(new_user.is_active)
        self.assertFalse(new_user.is_staff)
        self.assertFalse(new_user.is_superuser)
    
    def test_create_superuser(self):
        UserAccount = get_user_model()
        admin_user = UserAccount.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)