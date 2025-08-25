import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    # Creates a test/mock client. Else, in CICD, when the unit test runs on the runner host, 
    # there isnt a Flask server running as the actual Flask server is running in a docker container
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
