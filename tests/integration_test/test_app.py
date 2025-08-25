import unittest
import psycopg2
import os
import sys
from dotenv import load_dotenv
# Add parent of integration_tests (i.e., 'tests' folder parent) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from connect_postgres import get_connection

# Load the .env file at the start of your test module
load_dotenv() 

class URLIntegrationTest(unittest.TestCase):

    def setUp(self):
        # Use your get_connection() function, so table gets created
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def tearDown(self):
        self.cur.close()
        self.conn.close()

    def test_insert_and_retrieve_url(self):
        # Start transaction so we don't affect real data
        self.cur.execute("BEGIN;")
        self.cur.execute(
            "INSERT INTO urls (original_url, short_code) VALUES (%s, %s);",
            ("https://example.com", "exmpl")
        )
        self.cur.execute(
            "SELECT short_code FROM urls WHERE original_url=%s;",
            ("https://example.com",)
        )
        result = self.cur.fetchone()[0]
        self.assertEqual(result, "exmpl")
        self.cur.execute("ROLLBACK;")
