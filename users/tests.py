from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='julle',
            email="test2@test.com",
            password='testpass123'
        )
        self.assertEqual(user.username, 'julle')
        self.assertEqual(user.email, 'test2@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superjulle',
            email="supertest2@test.com",
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superjulle')
        self.assertEqual(admin_user.email, 'supertest2@test.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        self.user = get_user_model().objects.create_user(self.username, self.email)
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'This should not be here')

    def test_signup_form(self):
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


class EditProfilePageTests(TestCase):
    firstname = 'new'
    lastname = 'user'

    def setUp(self):
        user = get_user_model()
        self.user = user.objects.create_user(
            username='julle',
            email="test2@test.com",
            password='testpass123'
        )
        url = reverse('user_edit', args=(self.user.id,))
        self.response = self.client.get(url)

    def test_userprofile_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'users/customuser_form.html')
        self.assertContains(self.response, 'Edit Profile')
        self.assertNotContains(self.response, 'This should not be here')

    def test_userprofile_update(self):
        # Update users profile info
        user_profile = get_user_model().objects.get(id=self.user.id)
        user_profile.first_name = 'Julle'
        user_profile.last_name = 'Julgran'
        user_profile.save()

        user_profile.refresh_from_db()

        self.assertEqual(user_profile.first_name, 'Julle')
        self.assertEqual(user_profile.last_name, 'Julgran')
