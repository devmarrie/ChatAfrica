import unittest
from app import app

class QuesRoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass
    
    def test_get_questions(self):
        response = self.app.get('/questions')
        self.assertEqual(response.status_code, 200)
    
    def test_get_question(self):
        response = self.app.get('/question/1ce96601-5049-4ec6-b6ad-7a3e68a57543')
        self.assertEqual(response.status_code, 200)
    
    def test_create_question(self):
        data =  {
            "que": "What is Africa famous for?",
            "res_id": "a80bee60-4280-4d75-8af7-2e3db80370d1"
        }
        response = self.app.post('/create_question', json=data)
        self.assertEqual(response.status_code, 200)
    
    def test_update_question(self):
        data =  {
            "que": "The famous Africa",
            "res_id": "a80bee60-4280-4d75-8af7-2e3db80370d1"
        }
        response = self.app.put('/question_update/5ae50ae8-ce5a-4631-9452-d9c0aadff2d7', json=data)
        self.assertEqual(response.status_code,200)
    
    def test_delete_chat(self):
        response = self.app.delete('/question_delete/8e5d5d53-7ca9-412f-a8c7-ca94d386cfbc')
        self.assertEqual(response.status_code,200)
    

if __name__ == '__main__':
    unittest.main()
