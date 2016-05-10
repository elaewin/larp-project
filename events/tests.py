import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils.timezone import utc
from events.models import Event, Tag


class EventTestCase(TestCase):
    fixtures = ["events_test_fixture.json", ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Event(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class TagTestCase(TestCase):

    def test_string_representation(self):
        expected = "A Tag"
        c1 = Tag(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""
    fixtures = ['events_test_fixture.json', ]

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Event(title="Game %d Title" % count,
                         description="foo",
                         creator=author)
            if count < 6:
                # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        resp = self.client.get('/')
        # the content of the rendered response is always a bytestring
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("Upcoming Games" in resp_text)
        for count in range(1, 11):
            title = "Game %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        for count in range(1, 11):
            title = "Game %d Title" % count
            post = Event.objects.get(title=title)
            resp = self.client.get('/events/%d/' % post.pk)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)
