from django.forms.widgets import DateTimeInput
from django.test import RequestFactory, TestCase, client
from django.urls import reverse
from django.utils import timezone

from my_health_care_app.glucoses.tests.factories import GlucoseFactory
from my_health_care_app.glucoses.views import GlucoseCreateView
from my_health_care_app.users.tests.factories import UserFactory


class TestGlucoseListView(TestCase):
    def setUp(self) -> None:
        self.c = client.Client()

    def test_user_without_measurements(self):
        user = UserFactory()
        self.c.force_login(user)
        response = self.c.get(reverse("glucoses:list"))
        assert "object_list" in response.context
        assert response.context.get("object_list").count() == 0

    def test_user_with_measurements(self):
        glucose = GlucoseFactory()
        self.c.force_login(glucose.user)
        response = self.c.get(reverse("glucoses:list"))
        assert "object_list" in response.context
        assert response.context.get("object_list").count() == 1

    def test_user_checks_other_user_measurements(self):
        user = UserFactory()
        glucose = GlucoseFactory()
        assert glucose.user is not user
        self.c.force_login(user)
        response = self.c.get(reverse("glucoses:list"))
        assert "object_list" in response.context
        assert response.context.get("object_list").count() == 0


class TestGlucoseCreateView(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.view = GlucoseCreateView()

    def test_get_form(self):
        request = self.factory.get(reverse("glucoses:add"))
        self.view.setup(request)
        form = self.view.get_form()
        self.assertIsInstance(form.fields["record_datetime"].widget, DateTimeInput)


class TestGlucoseUpdateView(TestCase):
    def setUp(self) -> None:
        self.glucose = GlucoseFactory()
        self.c = client.Client()
        self.c.force_login(self.glucose.user)

    def test_glucose_update_success(self):
        response = self.c.post(
            reverse("glucoses:update", kwargs={"pk": self.glucose.pk}),
            {"value": 90, "record_datetime": timezone.now(), "notes": "New notes"},
        )
        self.glucose.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.glucose.notes, "New notes")
