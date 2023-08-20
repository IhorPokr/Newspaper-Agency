from django.test import TestCase
from agency.forms import RedactorCreationForm


class FormsTest(TestCase):
    def test_redactor_creat_with_years_of_experience_first_and_last_name(self):
        form_data = {
            "username": "new_user",
            "password1": "user12345test",
            "password2": "user12345test",
            "years_of_experience": 3,
            "first_name": "Top",
            "last_name": "Brown",
        }
        form = RedactorCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, form_data)
