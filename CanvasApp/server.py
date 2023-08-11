import http.server
import webbrowser
import os

current_script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_directory)


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header(
            "Cache-Control", "no-store, no-cache, must-revalidate, max-age=0"
        )
        http.server.SimpleHTTPRequestHandler.end_headers(self)


PORT = 8000
webbrowser.open("http://localhost:8000", 2)

with http.server.HTTPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
