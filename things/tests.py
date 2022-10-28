from django.test import TestCase
from django import forms
from things.forms import ThingForm

class ThingFormTestCase(TestCase):
    def setUp(self):
        self.form_input = {
        'name' : 'aleks',
        'description': 'i dont know what im actually doing',
        'quantity' : 1
        }

    def test_valid_user(self):
        form = ThingForm(data = self.form_input)
        self.assertTrue(form.is_valid())
