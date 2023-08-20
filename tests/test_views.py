from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

TOPIC_URL = reverse("agency:topic-list")
REDACTOR_CREATE_URL = reverse("agency:redactor-list-create")


class PublicTopicTests(TestCase):
    def test_login_required(self):
        response = self.client.get(TOPIC_URL)

        self.assertNotEquals(response.status_code, 200)


class PublicRedactorTests(TestCase):
    def test_login_required_for_create_new_redactor(self):
        response = self.client.get(REDACTOR_CREATE_URL)

        self.assertEquals(response.status_code, 302)


class PrivateRedactorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123456",
            years_of_experience=7
        )
        self.client.force_login(self.user)

    def test_create_redactor(self):
        form_data = {
            "username": "alex",
            "password1": "4474Odkoasjd",
            "password2": "4474Odkoasjd",
            "years_of_experience": 2,
            "first_name": "John",
            "last_name": "Black",
        }
        self.client.post(REDACTOR_CREATE_URL, data=form_data)
        new_redactor = get_user_model().objects.get(
            username=form_data["username"]
        )

        self.assertEquals(new_redactor.first_name, form_data["first_name"])
        self.assertEquals(new_redactor.last_name, form_data["last_name"])
        self.assertEquals(
            new_redactor.years_of_experience,
            form_data["years_of_experience"]
        )
