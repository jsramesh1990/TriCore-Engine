
# TriCore Terminal Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![C](https://img.shields.io/badge/C-00599C?logo=c&logoColor=white)](https://en.wikipedia.org/wiki/C_(programming_language))
[![C++](https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white)](https://isocpp.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20WSL-blue)](https://ubuntu.com/)

A multi-language demonstration project that integrates **C**, **C++**, and **Python** into a single application with a graphical dashboard.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Calculator Guide](#calculator-guide)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview

TriCore Terminal Engine demonstrates how three different programming languages can work together:
- **C Server** - Backend logic and data processing
- **C++ Client** - Client-side operations and messaging
- **Python GUI** - User interface with Tkinter

All components launch from a single bash script and run simultaneously.

## Features

- 🎯 **One-Command Launch** - Single script compiles and runs everything
- 🧮 **Built-in Calculator** - Full arithmetic operations with advanced functions
- 📊 **Real-time Monitoring** - Live server and client logs
- 🎨 **Modern Dark Theme** - Professional-looking interface
- 🔄 **Automatic Cleanup** - Proper process termination on exit

## Project Structure

```
TriCore-Engine/
│
├── backend/
│   ├── server.c          # C server (ticks every 2 seconds)
│   └── client.cpp        # C++ client (messages every second)
│
├── frontend/
│   └── visualizer.py     # Python Tkinter dashboard
│
├── scripts/
│   └── run.sh            # Orchestration script
│
└── README.md
```

## Installation

### Prerequisites

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install gcc g++ python3 python3-tk
```

**macOS:**
```bash
brew install gcc python3
brew install python-tk
```

**Arch Linux:**
```bash
sudo pacman -S gcc python python-tkinter
```

### Setup

1. **Clone or download** the project to your machine

2. **Make the script executable:**
```bash
chmod +x scripts/run.sh
```

3. **Run the engine:**
```bash
./scripts/run.sh
```

## Usage

When you run the engine, three things happen automatically:

1. **Compilation** - `server.c` and `client.cpp` are compiled
2. **Execution** - Server and client start in the background
3. **GUI Launch** - Python dashboard opens with three tabs:

### Tab 1: Calculator
Perform mathematical calculations (see guide below)

### Tab 2: Server Monitor
View real-time server logs and connection status

### Tab 3: Client Monitor
View client messages and activity logs

### Shutting Down
Click the **"Shutdown Engine"** button to close all processes cleanly.

## Calculator Guide

### Basic Operations

| Button | Function | Example | Result |
|--------|----------|---------|--------|
| `+` | Addition | `25+75` | `100` |
| `-` | Subtraction | `100-45` | `55` |
| `*` | Multiplication | `15*6` | `90` |
| `/` | Division | `100/4` | `25` |
| `=` | Calculate | Shows result | - |

### Advanced Functions

| Button | Function | Example | Result |
|--------|----------|---------|--------|
| `C` | Clear all | Clears display | - |
| `←` | Clear last character | Removes one digit | - |
| `√` | Square root | Type `16` then `√` | `4` |
| `x²` | Square | Type `5` then `x²` | `25` |
| `^` | Power | `2^3` | `8` |

### Tips
- Use parentheses for complex expressions: `(10+5)*2`
- Calculator handles decimals: `10.5 * 2`
- Modulo operator works: `15%4` returns `3`

## Troubleshooting

### Common Issues

**Problem:** `gcc: command not found`
```bash
# Solution: Install build tools
sudo apt install build-essential
```

**Problem:** `No module named 'tkinter'`
```bash
# Solution: Install Tkinter
sudo apt install python3-tk
```

**Problem:** `Permission denied`
```bash
# Solution: Make script executable
chmod +x scripts/run.sh
```

**Problem:** Python syntax error about strings
```bash
# Solution: Make sure visualizer.py uses triple quotes for multi-line strings
# Correct: """text"""
# Wrong: "text
```

### Running Components Individually

For debugging, run each component separately:

```bash
# Run server alone
gcc backend/server.c -o backend/server && ./backend/server

# Run client alone
g++ backend/client.cpp -o backend/client && ./backend/client

# Run GUI alone
python3 frontend/visualizer.py
```

## How It Works

### Process Flow

```
User runs ./scripts/run.sh
         ↓
Script changes to project root
         ↓
Compiles server.c → backend/server
Compiles client.cpp → backend/client
         ↓
Launches server (background process)
Launches client (background process)
         ↓
Launches Python GUI (foreground)
         ↓
User interacts with dashboard
         ↓
Click "Shutdown Engine" → GUI closes
         ↓
Script kills server & client processes
```

### Key Script Logic

The `run.sh` script uses:
- `cd "$(dirname "$0")/.."` - Always finds correct paths
- `&` - Runs processes in background
- `wait` - Waits for GUI to close
- `kill` - Terminates background processes on exit

## Development

### Modifying the Server

Edit `backend/server.c`:
```c
// Change tick speed
sleep(2);  // Change to sleep(1) for faster ticks
```

### Modifying the Client

Edit `backend/client.cpp`:
```cpp
// Change message frequency
std::this_thread::sleep_for(std::chrono::seconds(1));
```

### Modifying the GUI

Edit `frontend/visualizer.py`:
```python
# Change window size
root.geometry("1000x700")

# Change colors
root.configure(bg="#1e1e1e")
```

## License

This project is licensed under the MIT License - see below:

```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, subject to the following conditions...

Full license text: https://opensource.org/licenses/MIT
```



