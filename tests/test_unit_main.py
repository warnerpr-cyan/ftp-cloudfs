import unittest
from ftpcloudfs import main
from mock import Mock

MOD_NAME = 'ftpcloudfs.main.'

class Test_parse_configuration(unittest.TestCase):
    def test_with_passive_ports(self):
        main.Main().parse_configuration

class Test_parse_arguments(unittest.TestCase):
    def test_with_passive_ports(self):
        _main = main.Main()
        _main.parse_configuration()
        _main.parse_arguments(['--bind-address', '1234-5678',
                               '--auth-url', 'http://foo.bar:123',
                               ])
        self.assertEqual(_main.options.bind_address, '1234-5678')

if __name__ == '__main__':
    unittest.main
