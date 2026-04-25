#!/usr/bin/env python3
"""
Portfolio 开发服务器
服务 output/ 目录（构建产物）
"""
import http.server
import socketserver
import sys
from pathlib import Path

PORT = 8080
OUTPUT_DIR = Path(__file__).parent / "output"


class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(OUTPUT_DIR), **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


if __name__ == "__main__":
    if not OUTPUT_DIR.exists():
        print(f"ERROR: {OUTPUT_DIR} not found. Run: python3 scripts/build.py", file=sys.stderr)
        sys.exit(1)

    print(f"INFO: Portfolio serving {OUTPUT_DIR} on http://localhost:{PORT}", file=sys.stderr)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), SPAHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("INFO: Server stopped", file=sys.stderr)
            sys.exit(0)
