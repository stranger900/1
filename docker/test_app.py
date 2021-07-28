
import unittest, requests, os, sys


ip =  sys.argv[1]
port = sys.argv[2]

print(" ")
print("Testing :  " + str(sys.argv[1]) + ":" + str(sys.argv[2]))

response = requests.get("http://" + ip + ":" + port)
ping = os.system("ping -c 1 " + ip)

if (response.status_code == 200):
     print("************************")
     print("  Server responded with status 200")
     print("  Test OK  ")
     print("************************")
else:
     print("ERROR ***** Something wrong") 

if   (ping == 0):
     print("************************")
     print("  Test connection OK ")
     print("************************")
else:
     print("ERROR ***** Something wrong") 

#if __name__ == '__main__':
#     unittest.main()
