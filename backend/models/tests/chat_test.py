import unittest
from app import app

class ChatRoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass
    
    def test_get_chats(self):
        response = self.app.get('/chats')
        self.assertEqual(response.status_code, 200)
    
    def test_get_chat(self):
        response = self.app.get('/chat/a2ac3dac-fae1-48e3-a191-98ebc4a07691')
        self.assertEqual(response.status_code, 200)
    
    def test_create_chat(self):
        data =  {
            "user_id": "942fa5d4-6b84-4da4-b65c-e178165fcea8"
        }
        response = self.app.post('/create_chat', json=data)
        self.assertEqual(response.status_code, 200)
    
    def test_update_chat(self):
        data =  {
            "user_id": "818716e8-fdf9-46e3-81a9-9c291bbc68ae"
        }
        response = self.app.put('/chat_update/2da7aade-14f0-4d6e-8216-0255f839fb83', json=data)
        self.assertEqual(response.status_code,200)
    
    def test_delete_chat(self):
        response = self.app.delete('/chat_delete/ef935643-81c8-4082-ba7c-f0c7125da168')
        self.assertEqual(response.status_code,200)
    

if __name__ == '__main__':
    unittest.main()
