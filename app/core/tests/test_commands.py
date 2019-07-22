#patch creates a mock object during runtime, then removes it after completion
from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        '''Test waiting for db when db is available'''
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:

            #overrides default behavior, monitors how many times it's called and which calls were made
            gi.return_value = True

            #name of the management client
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    #@patch decorator replaces time.sleep with a mock function that returns True.
    #Used to speed up the test during runtime.
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        '''Test waiting for db'''
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            '''raises the operational errror the first 5 times of gi called, returns True on 6th iteration'''
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
