from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.views import login_view, logout_confirm


class AuthViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='test12345')

    def test_login_view_get(self):  # Тест GET на login - должен вернуть форму
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post_success(self):  # Тест успешного логина
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'test12345'})
        self.assertEqual(response.status_code, 302)  # редирект после логина
        self.assertTrue(self.client.session.get('_auth_user_id'))  # сессия с юзером

    def test_login_view_post_fail(self):  # Тест неудачного логина
        response = self.client.post(reverse('login'), {'username': 'wrong', 'password': 'testwrong'})
        self.assertEqual(response.status_code, 200)  # остаётся на странице

    def test_logout_view(self):  # Тест логаута
        self.client.login(username='testuser', password='test12345')  # логин для теста
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
