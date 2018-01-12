from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from . import utils

UserModel = get_user_model()


class ViewsTestCase(TestCase):
    def test_password_specs(self):
        url = reverse('password-specs')

        # Attempt without the username parameter
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 400)
        self.assertIn('error', resp.json())

        # Attempt with a non-existent username
        resp = self.client.get(url + '?username=non-existent')
        self.assertEqual(resp.status_code, 404)
        self.assertIn('error', resp.json())

        # Create a user
        user = UserModel(username='username')
        user.set_password('test')
        user.save()

        # Attempt with the good username
        resp = self.client.get('{}?username={}'.format(url, user.username))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {
            'user': utils.get_user_password_hash_specs(user),
            'required': utils.get_required_password_hash_specs(),
        })
