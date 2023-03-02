import unittest
from app import app

class ResRoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass
    
    def test_get_responses(self):
        response = self.app.get('/responses')
        self.assertEqual(response.status_code, 200)
    
    def test_get_response(self):
        response = self.app.get('/response/cb59fcea-205b-4110-8967-0377fccf09e4')
        self.assertEqual(response.status_code, 200)
    
    def test_create_response(self):
        data =  {
            "content": "The word Africa came into existence in the late 17th century. Initially, it was used to only refer to the northern part of the continent. Around that time, the continent had been colonized, and the Europeans ruled over its people as slaves. They influenced the change of identity from Alkebulan to its present name",
            "chat_id": "a2ac3dac-fae1-48e3-a191-98ebc4a07691"
        }
        response = self.app.post('/create_response', json=data)
        self.assertEqual(response.status_code, 200)
    
    def test_update_response(self):
        data =  {
            "content": "The Igbo people are an ethnic group in Nigeria. They are primarily found in Abia, Anambra, Ebonyi, Enugu, and Imo States.",
            "chat_id": "a2ac3dac-fae1-48e3-a191-98ebc4a07691"
        }
        response = self.app.put('/response_update/cb59fcea-205b-4110-8967-0377fccf09e4', json=data)
        self.assertEqual(response.status_code,200)
    
    def test_delete_chat(self):
        response = self.app.delete('/response_delete/55cddfc4-fa6c-439c-b564-844382b23da4')
        self.assertEqual(response.status_code,200)
    

if __name__ == '__main__':
    unittest.main()
