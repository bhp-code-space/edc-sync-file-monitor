import os
import socket

import paramiko
from django.db import models
from paramiko.ssh_exception import (AuthenticationException, BadHostKeyException,
                                    SSHException)


class ClientModelMixin(models.Model):

    @property
    def remote_files(self):
        """Returns a list of remote files for a given directory.
        """
        files = []
        if self.ping and self.active:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(
                    self.sftp_url, username=self.sftp_user, password=self.sftp_pass)
            except (ConnectionRefusedError, socket.timeout, socket.gaierror,
                    AuthenticationException, BadHostKeyException, ConnectionResetError,
                    SSHException, OSError) as e:
                files.append(e)
            else:
                _ftp = None
                with ssh.open_sftp() as _ftp:
                    if self.remote_dirname:
                        _ftp.chdir(self.remote_dirname)
                    files = _ftp.listdir()
                    files = [file for file in files if file.endswith('.json')]
        #                     ftp.close()
        return files

    @property
    def ping_remote_client(self):
        """Return True if remote machine is up.
        """
        if self.active:
            return True if os.system("ping -c 1 " + self.sftp_url) == 0 else False
        return False

    class Meta:
        abstract = True
