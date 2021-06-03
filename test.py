import unittest, time
import server
import client

DEBUG = False

host = 'localhost'
port = 7777
message = 'hello'

class ServerTestCase(unittest.TestCase):

##############################################


    def test_server(self):
        server.main(host, port)
        client.main(host, port, message)

        time.sleep(0.1)

        self.my_print(server.received_message[0])
        self.my_print(message)

        self.assertEqual(message, server.received_message[0])


    def my_print(self, msg='***'):
        if DEBUG == True:
            print(msg)


##############################################

if __name__ == '__main__':
    unittest.main()