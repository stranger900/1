import unittest, requests, os
from app import app, variables

class PageLoadTest(unittest.TestCase):
    def test_stat(self):
        response = requests.get('http://192.168.1.15:5000')
        assert response.status_code == 200

    def test_status(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    def test_var(self):
        self.assertEqual(os.environ['LOGIN'], 'andriy')

if __name__ == '__main__':
    unittest.main()
