import http.server
import json
import socketserver
from typing import Tuple
from http import HTTPStatus

PORT = 8000
#sample data
todos = [
    {"id": 1, "task": "Learn Python", "completed": False},
    {"id": 2, "task": "Build To-Do List", "completed": False},
]
class MyHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
        
    def do_GET(self):
        if self.path == '/todos':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(todos).encode())
        else:
            self.send_response(404)
            self.end_headers()
            
    def do_POST(self):
        if self.path == '/todos':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_todo = json.loads(post_data)
            new_todo['id'] = len(todos) + 1
            new_todo['completed'] = False
            todos.append(new_todo)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(new_todo).encode())
            
        else :
            self.send_response(404)
            self.end_headers()
            
        

    
if __name__ == "__main__":
    PORT = 8000
    # Create an object of the above class
    my_server = socketserver.TCPServer(("0.0.0.0", PORT), MyHandler)
    # Star the server
    print(f"Server started at {PORT}")
    my_server.serve_forever()