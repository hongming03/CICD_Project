import unittest
import psycopg2
import os
from dotenv import load_dotenv

# Load the .env file at the start of your test module
load_dotenv() 

class URLIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"), # This host name needs to match the service name in docker-compose.yml
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
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
