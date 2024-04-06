from django.contrib.auth import get_user
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RegisterTestCase(TestCase):

    def test_register_success(self):
        self.client.post(
            reverse('users:register'),
            data={
                "username": "asadbek",
                "first_name": "Asadbek",
                "last_name": "Sotvoldiyev",
                "email": "asadbek@mail.ru",
                "password": "1234",
                "password_confirm": "1234"
            }
        )

        user_count = User.objects.count()

        user = User.objects.get(username="asadbek")

        self.assertEqual(user_count, 1)
        self.assertEqual(user.first_name, "Asadbek")
        self.assertEqual(user.last_name, "Sotvoldiyev")
        self.assertEqual(user.email, "asadbek@mail.ru")
        self.assertNotEqual(user.password, "1234")
        self.assertTrue(user.check_password("1234"))


    def test_username_field(self):

        response = self.client.post(
            reverse('users:register'),
            data={
                "username": "root",
                "first_name": "Asadbek",
                "last_name": "Sotvoldiyev",
                "email": "asadbek@mail.ru",
                "password": "1234",
                "password_confirm": "1234"
            }
        )

        form = response.context['form']


        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertTrue(form.errors)
        self.assertIn("username", form.errors.keys())
        self.assertEqual(form.errors['username'], ["username 5 va 30 orasida bo'lishi lozim"])

    def test_password_field(self):

        response = self.client.post(
            reverse('users:register'),
            data={
                "username": "asadbek",
                "first_name": "Asadbek",
                "last_name": "Sotvoldiyev",
                "email": "asadbek@mail.ru",
                "password": "1234121212",
                "password_confirm": "1234"
            }
        )

        form = response.context['form']

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertTrue(form.errors)
        self.assertIn("password_confirm", form.errors.keys())
        self.assertEqual(form.errors['password_confirm'], ["Passwordlar bir biriga mos emas"])

    #email ni test qilish uyga vazifa
    #username allqachon mavjud ekanligiga tekshirish

class LoginTestCase(TestCase):

    def test_login_success(self):
        user = User.objects.create(username='asadbek', first_name='Asadbek', last_name='Sotvoldiyev')
        user.set_password('1234')

        user.save()

        self.client.post(
            reverse('users:login'),
            data={
                "username": "asadbek",
                "password": "1234"
            }
        )

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)



    #username fieldni test qilish
    #logout ekanligiga test yozish