from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):
  def test_create_user(self):
    user = User.objects.create_user('anas', 'nad@gmail.com', 'anas@123')
    self.assertIsInstance(user, User)
    self.assertFalse(user.is_staff)
    self.assertEqual(user.email, 'nad@gmail.com')

  def test_create_super_user(self):
    user = User.objects.create_superuser('anas', 'nad@gmail.com', 'anas@123')
    self.assertIsInstance(user, User)
    self.assertTrue(user.is_staff)
    self.assertEqual(user.email, 'nad@gmail.com')

  def test_no_username(self):
    self.assertRaises(ValueError, User.objects.create_user,username='',email='nad@gmail.com', password='anas@123')
  
  def test_no_email(self):
    self.assertRaises(ValueError, User.objects.create_user,username='anas',email='', password='anas@123')

  def test_error_msg_no_username(self):
    with self.assertRaisesMessage(ValueError, 'The given username must be set'):
      User.objects.create_user(username='', email='anas@gmail.com', password='Nad@2323')
  
  def test_error_msg_no_email(self):
    with self.assertRaisesMessage(ValueError, 'The given email must be set'):
      User.objects.create_user(username='anasnad', email='', password='Nad@2323')

  def test_superuser_without_staff_status(self):
    with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
      User.objects.create_superuser(username='anasnad', email='nasd@gmal.com', password='Nad@2323', is_staff=False )

  def test_superuser_without_super_status(self):
    with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
      User.objects.create_superuser(username='anasnad', email='nasd@gmal.com', password='Nad@2323', is_superuser=False )

  