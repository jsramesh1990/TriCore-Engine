#!/bin/bash
clear

gcc server.c -o server
g++ client.cpp -o client

./server &
SERVER_PID=$!

./client &
CLIENT_PID=$!

python3 visualizer.py

wait $SERVER_PID
wait $CLIENT_PID
