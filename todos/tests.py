from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from todos.models import Todo
# Create your tests here.
class TestListCreatTodos(APITestCase):
  def authenticate(self):
    authen_data = {"username":"username","email":"email@gmail.com","password":"password@123"}
    self.client.post(reverse('register'), authen_data)
    response = self.client.post(reverse('login'), {"email":"email@gmail.com","password":"password@123"} )
    self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")

  def test_creates_without_token_todo(self):
    sample_todo = {"title":"Yo you!", "desc":"Yes you."}
    response = self.client.post(reverse('todos'), sample_todo)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
  
  def test_creates_with_token_todo(self):
    tot_todo_item = Todo.objects.all().count()
    self.authenticate()
    sample_todo = {"title":"Yo you!", "desc":"Yes you."}
    response = self.client.post(reverse('todos'), sample_todo)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Todo.objects.all().count(),tot_todo_item+1)
    self.assertEqual(response.data['title'], 'Yo you!')
    self.assertEqual(response.data['desc'], 'Yes you.')

  def retrieve_all_todos(self):
    self.authenticate()
    response = self.client.get(reverse('todos'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIsInstance(response.data['results'], list)
