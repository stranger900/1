import unittest, requests, os, sys
#from sys import argv
class PageLoadTest(unittest.TestCase):

    def test_stat(self):
        print(sys.argv[0])
        print(str(sys.argv[1]))
        response = requests.get('http://192.168.1.15:5010')
        assert response.status_code == 200

if __name__ == '__main__':
     unittest.main()

