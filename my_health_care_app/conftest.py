import pytest

from my_health_care_app.bloodpressures.models import BloodPressure
from my_health_care_app.bloodpressures.tests.factories import BloodPressureFactory
from my_health_care_app.glucoses.models import Glucose
from my_health_care_app.glucoses.tests.factories import GlucoseFactory
from my_health_care_app.users.models import User
from my_health_care_app.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def glucose() -> Glucose:
    return GlucoseFactory()


@pytest.fixture
def bloodpressure() -> BloodPressure:
    return BloodPressureFactory()
