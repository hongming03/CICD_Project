import unittest
import psycopg2
import os

class PostgresTestCase(unittest.TestCase):

    def setUp(self):
        # Connect to the database using environment variables
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        self.cur = self.conn.cursor()

    def tearDown(self):
        # Close cursor and connection after each test
        self.cur.close()
        self.conn.close()

    def test_connection(self):
        """Test that the database connection works"""
        self.cur.execute("SELECT 1;")
        result = self.cur.fetchone()
        self.assertEqual(result[0], 1)

    def test_table_exists(self):
        """Test that the 'urls' table exists"""
        self.cur.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'urls'
            );
        """)
        exists = self.cur.fetchone()[0]
        self.assertTrue(exists)

    def test_insert_and_select(self):
        """Test basic insert and select (transaction rolled back after test)"""
        self.cur.execute("BEGIN;")  # Start transaction
        self.cur.execute("INSERT INTO urls (original_url, short_code) VALUES (%s, %s);",
                         ("https://example.com", "exmpl"))
        self.cur.execute("SELECT short_code FROM urls WHERE original_url = %s;", ("https://example.com",))
        result = self.cur.fetchone()[0]
        self.assertEqual(result, "exmpl")
        self.cur.execute("ROLLBACK;")  # Roll back to avoid modifying real data
