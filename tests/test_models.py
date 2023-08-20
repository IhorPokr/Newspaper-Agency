from django.test import TestCase
from django.contrib.auth import get_user_model
from agency.models import Redactor, Topic, Newspaper


class RedactorModelTest(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create(username="john_doe", years_of_experience=5)

    def test_redactor_str(self):
        self.assertEqual(str(self.redactor), "john_doe")

    def test_redactor_years_of_experience_default(self):
        self.assertEqual(self.redactor.years_of_experience, 5)


class TopicModelTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Politics")

    def test_topic_str(self):
        self.assertEqual(str(self.topic), "Politics")


class NewspaperModelTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Sports")
        self.publisher = get_user_model().objects.create_user(username="publisher1", password="testpassword")
        self.newspaper = Newspaper.objects.create(
            title="Breaking News",
            content="Important news content",
            publisher_date="2023-08-20",
            topic=self.topic
        )
        self.newspaper.publishers.add(self.publisher)

    def test_newspaper_str(self):
        expected_str = "Breaking News Important news content (date: 2023-08-20, topic: Sports)"
        self.assertEqual(str(self.newspaper), expected_str)

    def test_newspaper_publishers(self):
        self.assertEqual(self.newspaper.publishers.count(), 1)
        self.assertEqual(self.newspaper.publishers.first().username, "publisher1")

    def test_newspaper_topic(self):
        self.assertEqual(self.newspaper.topic.name, "Sports")
