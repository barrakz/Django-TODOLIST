from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from tasks.models import Category, Task


class TaskAddTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='Pass'
        )
        self.category = Category.objects.create(name='Test Category', user=self.user)
        self.url = reverse('add')

    def test_add_task_logged_in(self):
        self.client.login(username='testuser', password='Pass')
        response = self.client.post(self.url, {'name': 'Test Task', 'category': self.category.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.category, self.category)
        self.assertEqual(task.user, self.user)

    def test_delete_task_logged_in(self):
        self.client.login(username='testuser', password='Pass')
        task = Task.objects.create(name='Test Task', category=self.category, user=self.user)
        response = self.client.post(reverse('delete', args=[task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertEqual(Task.objects.count(), 0)

    def test_edit_task_logged_in(self):
        self.client.login(username='testuser', password='Pass')
        response = self.client.post(self.url, {'name': 'Test Task', 'category': self.category.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.first()
        response = self.client.get(reverse('edit', args=[task.id]))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('edit', args=[task.id]), {'name': 'Updated Task'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)

        task.refresh_from_db()
        self.assertEqual(task.name, 'Updated Task')

    def test_edit_task_name_only(self):
        self.client.login(username='testuser', password='Pass')
        response = self.client.post(self.url, {'name': 'Test Task', 'category': self.category.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.category, self.category)
        self.assertEqual(task.user, self.user)

        url = reverse('edit', kwargs={'pk': task.id})
        response = self.client.post(url, {'name': 'New Test Task'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.name, 'New Test Task')
        self.assertEqual(task.category, self.category)
        self.assertEqual(task.user, self.user)












