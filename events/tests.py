import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase, override_settings
from django.utils.timezone import utc

from events.models import Event, Tag
from registration.forms import RegistrationForm


@override_settings(
    ACCOUNT_ACTIVATION_DAYS=7,
    REGISTRATION_OPEN=True
    )
class RegistrationTestCase(TestCase):
    """
    Adapted from django-registration.
    Django-registration has it's own set of tests which can be run according to
    the instructions in the documentation for that package.
    
    Base class for test cases, defining valid data for registering a
    user account and looking up the account after creation.

    """

    user_model = get_user_model()

    valid_data = {
        User.USERNAME_FIELD: 'alice',
        'email': 'alice@example.com',
        'password1': 'swordfish',
        'password2': 'swordfish',
    }

    user_lookup_kwargs = {
        User.USERNAME_FIELD: 'alice',
    }


class WorkflowTestCase(RegistrationTestCase):
    """
    Base class for the test cases which exercise the built-in
    workflows, including logic common to all of them (and which needs
    to be tested for each one).

    """
    @override_settings(REGISTRATION_OPEN=True)
    def test_registration_open(self):
        """
        ``REGISTRATION_OPEN``, when ``True``, permits registration.

        """
        resp = self.client.get(reverse('registration_register'))
        self.assertEqual(200, resp.status_code)

    @override_settings(REGISTRATION_OPEN=False)
    def test_registration_closed(self):
        """
        ``REGISTRATION_OPEN``, when ``False``, disallows registration.

        """
        resp = self.client.get(
            reverse('registration_register')
        )
        self.assertRedirects(resp, reverse('registration_disallowed'))

        resp = self.client.post(
            reverse('registration_register'),
            data=self.valid_data
        )
        self.assertRedirects(resp, reverse('registration_disallowed'))

    def test_registration_get(self):
        """
        HTTP ``GET`` to the registration view uses the appropriate
        template and populates a registration form into the context.

        """
        resp = self.client.get(reverse('registration_register'))
        self.assertEqual(200, resp.status_code)
        self.assertTemplateUsed(
            resp, 'registration/registration_form.html'
        )
        self.assertTrue(
            isinstance(
                resp.context['form'], RegistrationForm
            )
        )

    def test_registration(self):
        """
        Registration creates a new account.

        """
        resp = self.client.post(
            reverse('registration_register'),
            data=self.valid_data
        )
        self.assertRedirects(resp, reverse('registration_complete'))

        new_user = self.user_model.objects.get(**self.user_lookup_kwargs)

        self.assertTrue(
            new_user.check_password(
                self.valid_data['password1']
            )
        )
        self.assertEqual(new_user.email, self.valid_data['email'])

    def test_registration_failure(self):
        """
        Registering with invalid data fails.

        """
        data = self.valid_data.copy()
        data.update(password2='notsecret')
        resp = self.client.post(
            reverse('registration_register'),
            data=data
        )
        self.assertEqual(200, resp.status_code)
        self.assertFalse(resp.context['form'].is_valid())


class ActivationTestCase(WorkflowTestCase):
    """
    Base class for testing the built-in workflows which involve an
    activation step.

    """
    # First few methods repeat parent class, but with added checks for
    # is_active status and sending of activation emails.
    def test_registration(self):
        """
        Registration creates a new inactive account and sends an
        activation email.

        """
        super(ActivationTestCase, self).test_registration()
        new_user = self.user_model.objects.get(**self.user_lookup_kwargs)

        # New user must not be active.
        self.assertFalse(new_user.is_active)

        # An activation email was sent.
        self.assertEqual(len(mail.outbox), 1)

    def test_registration_failure(self):
        """
        Registering with invalid data fails.

        """
        super(ActivationTestCase, self).test_registration_failure()

        # Activation email was not sent.
        self.assertEqual(0, len(mail.outbox))

    def test_registration_no_sites(self):
        """
        Registration still functions properly when
        ``django.contrib.sites`` is not installed; the fallback will
        be a ``RequestSite`` instance.

        """
        with self.modify_settings(INSTALLED_APPS={
            'remove': ['django.contrib.sites']
        }):
            resp = self.client.post(
                reverse('registration_register'),
                data=self.valid_data
            )
            self.assertEqual(302, resp.status_code)

            new_user = self.user_model.objects.get(**self.user_lookup_kwargs)

            self.assertTrue(
                new_user.check_password(
                    self.valid_data['password1']
                )
            )
            self.assertEqual(new_user.email, self.valid_data['email'])


class EventTestCase(TestCase):
    """
    Event creation works.
    """
    fixtures = ["events_test_fixture.json", ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Event(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class TagTestCase(TestCase):
    """
    Tag creation works.
    """
    def test_string_representation(self):
        expected = "A Tag"
        c1 = Tag(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class SubscriptionTestCase(TestCase):
    """
    Subscribing to an event works.
    """
    pass


class FrontEndTestCase(TestCase):
    """
    test views provided in the front-end
    """
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
        """
        Only events that are 'published' in the admin view display on the list of games.
        """
        resp = self.client.get('/events/')
        # the content of the rendered response is always a bytestring
        resp_text = resp.content.decode(resp.charset)
        print(resp_text)
        self.assertTrue("Upcoming Games" in resp_text)
        for count in range(1, 11):
            title = "Game %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        """
        Only games that are 'published' in the admin view are reachable.
        """
        for count in range(1, 11):
            title = "Game %d Title" % count
            post = Event.objects.get(title=title)
            resp = self.client.get('/events/%d/' % post.pk)
            print(resp)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)
