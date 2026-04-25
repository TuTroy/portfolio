#!/usr/bin/env python3
"""
Portfolio 开发服务器
直接服务 output/ 目录（构建产物）
"""
import http.server
import socketserver
import os
import sys
from pathlib import Path

PORT = 8080
SCRIPT_DIR = Path(__file__).parent.resolve()
OUTPUT_DIR = SCRIPT_DIR / "output"


class SPAHandler(http.server.SimpleHTTPRequestHandler):
    """支持 SPA 的静态文件服务"""
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
        print("❌ output/ 目录不存在，请先运行: python3 scripts/build.py")
        sys.exit(1)

    print(f"✅ Portfolio 已启动: http://localhost:{PORT}")
    print(f"📂 服务目录: {OUTPUT_DIR}")
    print(f"🔨 构建命令: python3 scripts/build.py")
    print(f"\n按 Ctrl+C 停止服务")
    try:
        with socketserver.TCPServer(("", PORT), SPAHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 服务已停止")
        sys.exit(0)
