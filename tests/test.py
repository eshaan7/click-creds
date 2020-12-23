# system imports
from unittest import TestCase
from click.testing import CliRunner

# lib imports
import click_creds
from example_project.main import cli


class TestLibrary(TestCase):
    def test_singelton(self):
        a = click_creds.NetrcStore("test_singelton")
        b = click_creds.NetrcStore("test_singelton")
        self.assertIs(a, b)

    def test_default_mapping(self):
        obj = click_creds.NetrcStore("test_mapping")
        default = click_creds.defaults.DEFAULT_MAPPING
        self.assertDictEqual(default, obj.mapping)

    def test_custom_mapping(self):
        mapp = {"login": "username", "password": "api_key", "account": "url"}
        obj = click_creds.NetrcStore("test_custom_mapping", mapping=mapp)
        self.assertDictEqual(obj.mapping, mapp)


class TestBasic(TestCase):
    def setUp(self):
        self.runner: CliRunner = CliRunner()

    def test_cli(self):
        result = self.runner.invoke(cli)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Usage", result.output)


class TestConfig(TestCase):
    def setUp(self):
        self.runner: CliRunner = CliRunner()

    def test_config_help(self):
        result = self.runner.invoke(cli, ["config", "--help"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Usage", result.output)

    def test_config_get(self):
        result = self.runner.invoke(cli, ["config", "get"])
        self.assertEqual(result.exit_code, 0)

    def test_config_get_default_mapping(self):
        result = self.runner.invoke(cli, ["config", "get", "-m"])
        self.assertEqual(result.exit_code, 0)

    def test_config_set_and_get(self):
        # step 1
        mapp = {
            "username": "test",
            "api_key": "hax0r",
            "url": "localhost",
        }
        result = self.runner.invoke(
            cli,
            [
                "config",
                "set",
                "--username",
                "test",
                "--api_key",
                "hax0r",
                "--url",
                "localhost",
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(
            result.output.strip("\n"), "Successfully saved config variables!"
        )
        # step 2
        obj = click_creds.NetrcStore("myawesomeapp")
        self.assertDictEqual(mapp, obj.host_with_mapping)

    def test_config_echo(self):
        result = self.runner.invoke(cli, ["config", "echo"])
        self.assertEqual(result.exit_code, 0)
