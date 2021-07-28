import requests, sys, os

def test_status():
    r = requests.get('http://' + sys.argv[2] + ':' + sys.argv[3])
    assert r.status_code == 200

def test_connection():
    ping = os.system("ping -c 1" + sys.argv[2])
    assert ping == 512
