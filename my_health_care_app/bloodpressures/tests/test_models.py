import pytest

from my_health_care_app.bloodpressures.models import BloodPressure

pytestmark = pytest.mark.django_db


def test_bloodpressure_get_absolute_url(bloodpressure: BloodPressure):
    assert bloodpressure.get_absolute_url() == f"/bloodpressures/{bloodpressure.id}/"
