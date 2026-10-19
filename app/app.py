"""DevOps student application.

Prints the student's information and serves it over HTTP on port 8080.
Values come from environment variables, with defaults as a fallback.
"""
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

NAME = os.getenv("STUDENT_NAME", "Dias")
SURNAME = os.getenv("STUDENT_SURNAME", "Abdullayev")
GROUP = os.getenv("STUDENT_GROUP", "IT2-2313SE")
STUDENT_ID = os.getenv("STUDENT_ID", "37240")
PORT = int(os.getenv("APP_PORT", "8080"))


def banner():
    return (
        "================================\n"
        "DevOps Student Application\n"
        "================================\n"
        "\n"
        f"Name: {NAME}\n"
        f"Surname: {SURNAME}\n"
        f"Group: {GROUP}\n"
        f"Student ID: {STUDENT_ID}\n"
        "\n"
        "Application is running successfully!\n"
    )


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = banner().encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(banner(), flush=True)
    print(f"Listening on port {PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
