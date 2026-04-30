#!/bin/bash
clear

echo "Starting TriCore Terminal Engine..."

# Move to project root from scripts folder
cd "$(dirname "$0")/.."

# Compile backend files
echo "Compiling server..."
gcc backend/server.c -o backend/server
if [ $? -ne 0 ]; then
    echo "❌ Server compilation failed"
    exit 1
fi

echo "Compiling client..."
g++ backend/client.cpp -o backend/client
if [ $? -ne 0 ]; then
    echo "❌ Client compilation failed"
    exit 1
fi

echo "✅ Compilation successful"

# Run backend services in background
echo "Starting server..."
./backend/server &
SERVER_PID=$!

echo "Starting client..."
./backend/client &
CLIENT_PID=$!

# Give servers a moment to start
sleep 1

# Launch frontend dashboard (this blocks until closed)
echo "Launching visualizer..."
python3 frontend/visualizer.py

# When visualizer closes, clean up background processes
echo "Shutting down engine..."
kill $SERVER_PID $CLIENT_PID 2>/dev/null
wait $SERVER_PID $CLIENT_PID 2>/dev/null

echo "TriCore Engine stopped."
