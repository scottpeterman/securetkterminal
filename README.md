
# Serial Terminal Emulation

A comprehensive terminal emulation application built with Python and Tkinter, supporting serial communication and SSH connectivity with advanced features like window resizing, font adjustment, and terminal history management.

## Features

- **Serial Communication**: Connect to devices over serial ports with customizable settings (baud rate, parity, etc.).
- **PTY Synchronization (SSH)**: Ensure the remote pseudo-terminal (pty) is in sync with the local terminal dimensions.
- **Dynamic Window Resizing**: Responsive terminal grid that adjusts to window size changes.
- **Font Size Management**: Ability to increase or decrease font size, with the terminal grid adapting accordingly.
- **Advanced Rendering**: Utilizes `pyte` for accurate terminal emulation, rendering complex terminal sequences and managing cursor positioning.
- **History Buffer**: Scroll back through the terminal history, capturing the output that has scrolled off the screen.

## Installation

Describe the steps to install the application:

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd serial-terminal-emulation

# (Optional) Setup a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the required dependencies
pip install -r requirements.txt
