import unittest
from app import app

class UserRoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
    
    def test_get_user(self):
        response = self.app.get('/user/42d6da94-5af4-4bb2-8d22-ba71cb94ead6')
        self.assertEqual(response.status_code, 200)
    
    def test_create_user(self):
        data =  {
            "username": "tracie",
            "email": "tracie@gmail.com"
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 200)
    
    def test_update_user(self):
        data =  {
            "username": "aliko",
            "email": "aliko@gmail.com"
        }
        response = self.app.put('/user_update/42d6da94-5af4-4bb2-8d22-ba71cb94ead6', json=data)
        self.assertEqual(response.status_code,200)
    
    def test_delete_user(self):
        response = self.app.delete('/user_delete/b7ff23be-c6ea-4016-80c5-0c246d8be83d')
        self.assertEqual(response.status_code,200)
    

if __name__ == '__main__':
    unittest.main()
