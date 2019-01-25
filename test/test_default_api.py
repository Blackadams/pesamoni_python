# coding: utf-8

"""
    Pesaway Pesamoni API Documentation

"""


from __future__ import absolute_import

import unittest

import pesamoni_python
from pesamoni_python.api.default_api import DefaultApi  # noqa: E501
from pesamoni_python.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = pesamoni_python.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_transactions_post(self):
        """Test case for transactions_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
