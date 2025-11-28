import unittest
import json
import sys
import os

# Add the parent directory to the path so we can import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_ask_endpoint_returns_200(self):
        """Test that /ask endpoint responds with 200 OK"""
        response = self.app.post('/ask', 
                                data=json.dumps({'question': 'Hello'}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_ask_endpoint_returns_json_with_answer(self):
        """Test that /ask endpoint returns JSON with answer field"""
        response = self.app.post('/ask',
                                data=json.dumps({'question': 'What is your name?'}),
                                content_type='application/json')
        self.assertEqual(response.content_type, 'application/json')
        
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('answer', data)
        self.assertIsInstance(data['answer'], str)

    def test_ask_endpoint_answer_not_empty(self):
        """Test that /ask endpoint returns non-empty answer"""
        response = self.app.post('/ask',
                                data=json.dumps({'question': 'Tell me something'}),
                                content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        
        self.assertIn('answer', data)
        self.assertGreater(len(data['answer']), 0)
        self.assertNotEqual(data['answer'], '')

    def test_ask_endpoint_missing_question(self):
        """Test that /ask endpoint handles missing question"""
        response = self.app.post('/ask',
                                data=json.dumps({}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', data)

    def test_ask_endpoint_empty_question(self):
        """Test that /ask endpoint handles empty question"""
        response = self.app.post('/ask',
                                data=json.dumps({'question': ''}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', data)

    def test_home_endpoint(self):
        """Test that home endpoint works"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

if __name__ == '__main__':
    unittest.main()