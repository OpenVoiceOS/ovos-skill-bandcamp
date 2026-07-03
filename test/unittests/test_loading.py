import unittest

from ovos_plugin_manager.skills import find_skill_plugins


class TestPlugin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill_id = "skill-ovos-bandcamp.openvoiceos"

    def test_find_plugin(self):
        plugins = find_skill_plugins()
        self.assertIn(self.skill_id, list(plugins))
