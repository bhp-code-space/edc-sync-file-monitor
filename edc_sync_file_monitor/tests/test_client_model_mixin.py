from unittest import mock

from django.test import TestCase
from paramiko.ssh_exception import AuthenticationException

from ..models import Client


class TestClientModelMixin(TestCase):

    def setUp(self):
        self.sftp_url = 'test_url'
        self.sftp_user = 'test_user'
        self.sftp_pass = 'test_pass'
        self.remote_files = ['test1.json', 'test2.json']
        self.remote_dirname = 'test_dir'

        self.model = Client()
        self.model.sftp_url = self.sftp_url
        self.model.sftp_user = self.sftp_user
        self.model.sftp_pass = self.sftp_pass
        self.model.remote_dirname = self.remote_dirname
        self.model.active = True

    def test_ping_remote_client_active(self):
        with mock.patch('os.system', return_value=0):
            self.assertTrue(self.model.ping_remote_client)

    def test_ping_remote_client_inactive(self):
        self.model.active = False
        self.assertFalse(self.model.ping_remote_client)
