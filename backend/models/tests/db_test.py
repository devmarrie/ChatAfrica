import unittest
import pymysql.cursors


class DBTestCase(unittest.TestCase):
    def setUp(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='!deng_23',
            db='chat_africa',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def teaDown(self):
        self.connection.close()

    def test_connectivity(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            result = cursor.fetchone()
            self.assertEqual(result['1'], 1)
if __name__ == '__main__':
    unittest.main()

    
