import pytest
from django.urls import resolve, reverse

from my_health_care_app.bloodpressures.models import BloodPressure

pytestmark = pytest.mark.django_db


def test_list():
    assert reverse("bloodpressures:list") == "/bloodpressures/"
    assert resolve("/bloodpressures/").view_name == "bloodpressures:list"


def test_detail(bloodpressure: BloodPressure):
    assert (
        reverse("bloodpressures:detail", kwargs={"pk": bloodpressure.id})
        == f"/bloodpressures/{bloodpressure.id}/"
    )
    assert (
        resolve(f"/bloodpressures/{bloodpressure.id}/").view_name
        == "bloodpressures:detail"
    )


def test_create():
    assert reverse("bloodpressures:add") == "/bloodpressures/add/"
    assert resolve("/bloodpressures/add/").view_name == "bloodpressures:add"


def test_update(bloodpressure: BloodPressure):
    assert (
        reverse("bloodpressures:update", args=[bloodpressure.id])
        == f"/bloodpressures/{bloodpressure.id}/update/"
    )
    assert (
        resolve(f"/bloodpressures/{bloodpressure.id}/update/").view_name
        == "bloodpressures:update"
    )


def test_delete(bloodpressure: BloodPressure):
    assert (
        reverse("bloodpressures:delete", args=[bloodpressure.id])
        == f"/bloodpressures/{bloodpressure.id}/delete/"
    )
    assert (
        resolve(f"/bloodpressures/{bloodpressure.id}/delete/").view_name
        == "bloodpressures:delete"
    )
