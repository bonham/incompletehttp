import socketserver
from time import sleep

class MyTCPHandler(socketserver.StreamRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
      # self.rfile is a file-like object created by the handler;
      # we can now use e.g. readline() instead of raw recv() calls
      self.data = self.rfile.readline().strip()
      print("{} wrote:".format(self.client_address[0]))
      print(self.data)
      # Likewise, self.wfile is a file-like object used to write back
      # to the client
      #self.wfile.write(self.data.upper())

      with open('response-1.txt', 'r+b') as f:
          content = f.read()
      print("----")
      print(type(content))
      print(len(content))
      # sleep(5)
      self.wfile.write(content)

if __name__ == "__main__":
    HOST, PORT = "localhost", 8844

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()  