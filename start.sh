#!/bin/bash
# Portfolio 启动脚本
# 用法: ./start.sh      启动服务
#       ./start.sh stop 停止服务

NAME="portfolio"
PORT=8080
LOG_DIR="./logs"
LOG_FILE="$LOG_DIR/portfolio.log"
PID_FILE="$LOG_DIR/portfolio.pid"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SERVE_SCRIPT="$SCRIPT_DIR/serve.py"

# 查找端口对应的进程 PID
find_pid() {
    lsof -ti :$PORT 2>/dev/null | head -1
}

start() {
    echo "🚀 启动 Portfolio 服务..."
    mkdir -p "$LOG_DIR"

    # 检查端口是否已被占用
    PID=$(find_pid)
    if [ -n "$PID" ]; then
        echo "⚠️  端口 $PORT 已被占用 (PID: $PID)，先停止..."
        kill $PID 2>/dev/null
        sleep 1
    fi

    # 构建项目
    echo "📦 正在构建..."
    python3 "$SCRIPT_DIR/scripts/build.py" > "$LOG_DIR/build.log" 2>&1
    if [ $? -ne 0 ]; then
        echo "❌ 构建失败，详见 logs/build.log"
        cat "$LOG_DIR/build.log"
        exit 1
    fi
    echo "✅ 构建完成"

    # 启动服务（后台运行）
    cd "$SCRIPT_DIR"
    nohup python3 "$SERVE_SCRIPT" > "$LOG_FILE" 2>&1 &
    SERVER_PID=$!
    echo $SERVER_PID > "$PID_FILE"
    sleep 1

    # 检查是否启动成功
    if kill -0 $SERVER_PID 2>/dev/null; then
        echo "✅ 服务已启动"
        echo "   URL: http://localhost:$PORT"
        echo "   PID: $SERVER_PID"
        echo "   日志: $LOG_FILE"
    else
        echo "❌ 启动失败，详见 $LOG_FILE"
        cat "$LOG_FILE"
        exit 1
    fi
}

stop() {
    echo "🛑 停止 Portfolio 服务..."
    PID=$(find_pid)
    if [ -n "$PID" ]; then
        kill $PID 2>/dev/null
        sleep 1
        echo "✅ 已停止 (PID: $PID)"
    else
        echo "⚠️  未找到运行中的服务"
    fi
    rm -f "$PID_FILE"
}

status() {
    PID=$(find_pid)
    if [ -n "$PID" ]; then
        echo "✅ 服务运行中 (PID: $PID)"
    else
        echo "⚠️  服务未运行"
    fi
}

logs() {
    if [ -f "$LOG_FILE" ]; then
        tail -50 "$LOG_FILE"
    else
        echo "⚠️  日志文件不存在"
    fi
}

case "$1" in
    stop)
        stop
        ;;
    status)
        status
        ;;
    logs)
        logs
        ;;
    restart)
        stop
        sleep 1
        start
        ;;
    *)
        start
        ;;
esac
