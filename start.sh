#!/bin/bash
# 构建 + 启动本地服务器
# 用法: bash start.sh [端口]

PORT=${1:-8080}
cd "$(dirname "$0")"
echo "🏗️  构建中..."
python3 build.py
echo ""
echo "🌐 打开浏览器访问: http://localhost:$PORT"
echo "按 Ctrl+C 停止服务"
cd output
python3 -m http.server $PORT
