import pytest
from django.urls import resolve, reverse

from my_health_care_app.glucoses.models import Glucose

pytestmark = pytest.mark.django_db


def test_list():
    assert reverse("glucoses:list") == "/glucoses/"
    assert resolve("/glucoses/").view_name == "glucoses:list"


def test_detail(glucose: Glucose):
    assert (
        reverse("glucoses:detail", kwargs={"pk": glucose.id})
        == f"/glucoses/{glucose.id}/"
    )
    assert resolve(f"/glucoses/{glucose.id}/").view_name == "glucoses:detail"


def test_create():
    assert reverse("glucoses:add") == "/glucoses/add/"
    assert resolve("/glucoses/add/").view_name == "glucoses:add"


def test_update(glucose: Glucose):
    assert (
        reverse("glucoses:update", args=[glucose.id])
        == f"/glucoses/{glucose.id}/update/"
    )
    assert resolve(f"/glucoses/{glucose.id}/update/").view_name == "glucoses:update"


def test_delete(glucose: Glucose):
    assert (
        reverse("glucoses:delete", args=[glucose.id])
        == f"/glucoses/{glucose.id}/delete/"
    )
    assert resolve(f"/glucoses/{glucose.id}/delete/").view_name == "glucoses:delete"
