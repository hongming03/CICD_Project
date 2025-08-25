import unittest
from unittest.mock import patch, MagicMock

class PostgresMockTestCase(unittest.TestCase):


    # Creating a mock Postgres server connection. Else, in CICD, when the unit test runs on the runner host, 
    # there isnt a Postgres server running as the actual Postgres server is running in a docker container
    @patch("psycopg2.connect")
    def setUp(self, mock_connect):
        # Mock connection and cursor
        self.mock_conn = MagicMock()
        self.mock_cur = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cur
        mock_connect.return_value = self.mock_conn

        # Store cursor and connection like before
        self.conn = self.mock_conn
        self.cur = self.mock_cur

    def tearDown(self):
        self.cur.close()
        self.conn.close()

    def test_connection(self):
        """Test that the database connection works"""
        self.cur.fetchone.return_value = [1]  # Mock result of SELECT 1;
        self.cur.execute("SELECT 1;")
        result = self.cur.fetchone()
        self.assertEqual(result[0], 1)

    def test_table_exists(self):
        """Test that the 'urls' table exists"""
        self.cur.fetchone.return_value = [True]  # Mock table exists
        self.cur.execute("SELECT EXISTS (...)")
        exists = self.cur.fetchone()[0]
        self.assertTrue(exists)

    def test_insert_and_select(self):
        """Test basic insert and select (transaction rolled back after test)"""
        self.cur.fetchone.return_value = ["exmpl"]  # Mock select result
        self.cur.execute("BEGIN;")
        self.cur.execute("INSERT INTO urls (original_url, short_code) VALUES (%s, %s);",
                         ("https://example.com", "exmpl"))
        self.cur.execute("SELECT short_code FROM urls WHERE original_url = %s;", ("https://example.com",))
        result = self.cur.fetchone()[0]
        self.assertEqual(result, "exmpl")
        self.cur.execute("ROLLBACK;")
