import http.server
import socketserver
import logging
import os

# Define the port number to listen on
PORT = 8000

# Define the directory to serve static files from
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

# Set up logging
logging.basicConfig(filename='basic_server.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Create a custom request handler by subclassing SimpleHTTPRequestHandler
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Set the directory to serve static files from
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def do_GET(self):
        """In this example, the server responds with "Custom response" when the path is /custom,
        and falls back to the default handling for other paths."""
        if self.path == '/custom':
            # Send a 200 OK response
            self.send_response(200)
            # Send the Content-type header
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Write the custom response body
            self.wfile.write(b"Custom response")
        else:
            # For all other paths, use the default GET handler
            super().do_GET()

    def do_POST(self):
        """Handle POST requests.
        In this example, the server responds with the received POST data when a POST request is made."""
        # Send a 200 OK response
        self.send_response(200)
        # Send the Content-type header
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Read the length of the data
        content_length = int(self.headers['Content-Length'])
        # Read the POST data
        post_data = self.rfile.read(content_length)
        # Write the response body
        self.wfile.write(b"POST request received: ")
        self.wfile.write(post_data)

    def send_error(self, code, message=None, explain=None):
        """Handle errors by sending a custom error message.
        In this example, the send_error method is overridden to send a custom HTML error message whenever an error occurs."""
        self.send_response(code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        error_message = f"<html><head><title>Error {code}</title></head><body><h1>Error {code}</h1><p>{message}</p></body></html>"
        self.wfile.write(error_message.encode('utf-8'))

    def log_message(self, format, *args):
        """Log messages to a file."""
        logging.info("%s - - [%s] %s\n" % (self.client_address[0], self.log_date_time_string(), format % args))

# Set up the TCP server with the custom handler
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    # Keep the server running to handle requests
    httpd.serve_forever()