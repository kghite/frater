from unittest import TestCase

from frater.core.activity.activity_factory import *
from ..mocks import MOCKS


class TestActivityFactory(TestCase):
    def test_json_to_activity(self):
        activity = MOCKS.frater.activity
        activity_json = MOCKS.json.activity

        assert json_to_activity(activity_json) == activity

    def test_activity_to_json(self):
        activity = MOCKS.frater.activity
        activity_json = MOCKS.json.activity

        assert activity_to_json(activity) == activity_json
