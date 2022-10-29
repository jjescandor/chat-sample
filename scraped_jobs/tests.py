from turtle import position
from django.test import TestCase

from django.contrib.auth import get_user_model

from .models import Active_job


class Active_jobTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='test_user', password='pass')
        test_user.save()

        test_thing = Active_job.objects.create(position="bartender", location="remote", company="Acme", url="physical work")
        test_thing.save()

    def test_things_model(self):
        thing = Active_job.objects.get(id=1)
        actual_position = str(thing.position)
        actual_location = str(thing.location)
        actual_company = str(thing.company)
        actual_url = str(thing.url)
        self.assertEqual(actual_position, "bartender")
        self.assertEqual(actual_location, "remote")
        self.assertEqual(actual_company, "Acme")
        self.assertEqual(actual_url, "physical work")
