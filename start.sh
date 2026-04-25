#!/bin/bash
# 构建 + 启动本地服务器
# 用法: bash start.sh [端口]

PORT=${1:-8080}
cd "$(dirname "$0")"

# 杀掉占用端口的进程
if lsof -ti:$PORT > /dev/null 2>&1; then
  echo "⚠️  端口 $PORT 已被占用，正在释放..."
  lsof -ti:$PORT | xargs kill -9 2>/dev/null
  sleep 1
fi

echo "🏗️  构建中..."
python3 build.py
echo ""
echo "🌐 打开浏览器访问: http://localhost:$PORT"
echo "按 Ctrl+C 停止服务"
cd output
python3 -m http.server $PORT
