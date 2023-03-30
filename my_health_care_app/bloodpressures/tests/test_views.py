import pytest
from django.forms.widgets import DateTimeInput
from django.test import RequestFactory, TestCase, client
from django.urls import reverse
from django.utils import timezone

from my_health_care_app.bloodpressures.tests.factories import BloodPressureFactory
from my_health_care_app.bloodpressures.views import BloodPressureCreateView


@pytest.mark.django_db
class TestBloodPressureListView:
    def test_user_without_measurements(self, user):
        c = client.Client()
        c.force_login(user)
        response = c.get(reverse("bloodpressures:list"))
        assert "object_list" in response.context
        assert response.context.get("object_list").count() == 0

    def test_user_with_measurements(self, bloodpressure):
        c = client.Client()
        c.force_login(bloodpressure.user)
        response = c.get(reverse("bloodpressures:list"))
        assert "object_list" in response.context
        assert response.context.get("object_list").count() == 1

    def test_user_checks_other_user_measurements(self, bloodpressure, user):
        assert bloodpressure.user is not user
        c = client.Client()
        c.force_login(user)
        response = c.get(reverse("bloodpressures:list"))
        assert "object_list" in response.context
        assert response.context.get("object_list").count() == 0


class TestBloodPressureCreateView(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.view = BloodPressureCreateView()

    def test_get_form(self):
        request = self.factory.get(reverse("bloodpressures:add"))
        self.view.setup(request)
        form = self.view.get_form()
        self.assertIsInstance(form.fields["examination_datetime"].widget, DateTimeInput)


class TestBloodPressureUpdateView(TestCase):
    def setUp(self) -> None:
        self.bloodpressure = BloodPressureFactory()
        self.c = client.Client()
        self.c.force_login(self.bloodpressure.user)

    def test_bloodpressure_update_success(self):
        response = self.c.post(
            reverse("bloodpressures:update", kwargs={"pk": self.bloodpressure.pk}),
            {
                "systlic": 130,
                "diastolic": 75,
                "pulse": 70,
                "examination_datetime": timezone.now(),
                "notes": "New notes",
            },
        )
        self.bloodpressure.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.bloodpressure.notes, "New notes")
