
# SSH + Serial Terminal Emulation

A comprehensive mult-tabbed terminal emulation application built with Python and Tkinter, supporting serial communication and SSH connectivity with advanced features like window resizing, font adjustment, and terminal history management.

## Features

- **Serial Communication**: Connect to devices over serial ports with customizable settings (baud rate, parity, etc.).
- **PTY Synchronization (SSH)**: Ensure the remote pseudo-terminal (pty) is in sync with the local terminal dimensions.
- **Dynamic Window Resizing**: Responsive terminal grid that adjusts to window size changes.
- **Font Size Management**: Ability to increase or decrease font size, with the terminal grid adapting accordingly.
- **Advanced Rendering**: Utilizes `pyte` for accurate terminal emulation, rendering complex terminal sequences and managing cursor positioning.
- **History Buffer**: Scroll back through the terminal history, capturing the output that has scrolled off the screen.

<div align="center">
  <img src="https://github.com/scottpeterman/securetkterminal/raw/main/screenshots/ssh.png" alt="ssh.png" width="400px">
  <hr><img src="https://github.com/scottpeterman/securetkterminal/raw/main/screenshots/serial.png" alt="serial.png" width="400px">
  <hr><img src="https://github.com/scottpeterman/securetkterminal/raw/main/screenshots/serial_bootup.png" alt="serial_bootup.png" width="400px">
</div>

### Main Components:
1. **MainApplication (Tkinter Window):**
   - Serves as the main window of the application.
   - Initiates the serial connection dialog on startup.
   - Hosts the terminal interface where serial communication is displayed.
   - Centers itself on the screen when started.

2. **SerialConnectionDialog (Tkinter Toplevel):**
   - A modal dialog that prompts the user to enter serial connection parameters (port, baud rate, data bits, stop bits, parity).
   - Positioned relative to the main window (center or custom offset).
   - Validates the user's input and attempts to establish a serial connection.

3. **TerminalSerial (Tkinter Frame):**
   - Displays the serial data received from the connected device.
   - Uses `pyte` library to emulate terminal capabilities, handling escape sequences and terminal behaviors.
   - Supports a history buffer to enable scrollback through the terminal output.
   - Provides a text widget with a scrollbar to view the terminal output.
   - Offers features like copying, pasting, and custom repainting.

4. **KeyHandler:**
   - Handles keypress events and sends the corresponding characters or control sequences to the connected serial device.

### Key Functionalities:
1. **Serial Communication:**
   - Connects to serial devices using user-provided parameters.
   - Displays incoming serial data in real-time.
   - Sends user input to the serial device.

2. **Terminal Emulation:**
   - Uses `pyte` to interpret and display control sequences, providing an experience similar to standard terminals.

3. **User Interaction:**
   - Allows users to interact with the serial device through a text-based interface.
   - Supports text selection, copy-paste operations, and other typical text widget interactions.

4. **Scrollback Buffer:**
   - Maintains a history of terminal output, allowing users to scroll back and view older output.

5. **Resizable Interface:**
   - Adjusts the displayed content when the window is resized.
   - Maintains the aspect ratio and ensures the terminal content is displayed appropriately.

6. **Centering and Positioning:**
   - Centers the main application window and the connection dialog on the screen or positions them based on custom offsets.

This project effectively combines Python's Tkinter for the GUI with serial communication handling and terminal emulation, resulting in a functional SSH + Serial Terminal application that can be used for various purposes, such as debugging, configuring devices, or simply communicating with any serial-enabled hardware.

Certainly! Here's a detailed point of view document discussing the handling of `pyte`, its integration with data streams, and the mapping of its display and history screens to a text-based widget in the context of the Serial and SSH terminal applications:

---

## Integrating Pyte for Terminal Emulation in Serial and SSH Applications

### Overview
`pyte` is a Python library that emulates terminal capabilities, such as interpreting control sequences sent by various devices or systems over a terminal. It's instrumental in applications that require interaction with devices via serial ports or SSH connections, as it provides a way to interpret and display data that includes terminal control sequences.

### Challenges
1. **Data Stream Handling:**
   - **Bidirectional Communication:** Data flows in two directions; user input needs to be sent to the device, and device output needs to be correctly interpreted and displayed.
   - **Control Sequences:** Device output may include control sequences (like color codes, cursor movement) that need to be interpreted rather than displayed as raw text.

2. **Screen Mapping:**
   - **Text Widget Limitations:** Text widgets in GUI frameworks like Tkinter are not natively equipped to handle terminal control sequences.
   - **Display and History Management:** The terminal emulator must display a viewport into a potentially much larger history buffer, and this viewport must update in response to user actions and incoming data.

### Solutions
1. **Pyte Integration:**
   - **Stream and Screen Objects:** `pyte` provides `Stream` and `Screen` objects. The `Stream` object interprets incoming data and applies changes to the `Screen` object, which represents the terminal screen state.
   - **Control Sequence Interpretation:** `pyte` handles various control sequences internally, updating the `Screen` object to reflect changes caused by these sequences (like cursor movement, text color changes, etc.).

2. **Mapping to Text Widget:**
   - **Redrawing Mechanism:** A mechanism is implemented to regularly redraw the contents of the text widget based on the current state of the `pyte` `Screen` object. This redrawing accounts for changes in the terminal state, user scrolling, and window resizing.
   - **History Buffer Management:** The history of terminal output is maintained, allowing users to scroll back and view previous output. This involves keeping a buffer of lines that have scrolled out of view and managing this buffer's size.

3. **User Interaction:**
   - **Key Handling:** User keypresses are intercepted, and corresponding actions are determined. Regular characters are sent directly to the device, while special keys (like arrow keys) are translated into appropriate control sequences.
   - **Copy-Paste Support:** Text selection and clipboard operations are handled to provide a native text manipulation experience within the terminal output.

### Implementation Details
1. **Data Stream Handling:**
   - The application reads from the serial or SSH connection in a separate thread to avoid blocking the GUI.
   - Incoming data is decoded (e.g., from bytes to a UTF-8 string) and fed into the `pyte` `Stream` object.
   - The `Stream` object updates the `Screen` object based on the interpreted control sequences.

2. **Screen Mapping and Redrawing:**
   - The application periodically triggers a redraw of the text widget.
   - During redraw, the text widget is updated to reflect the current state of the `pyte` `Screen`, including visible lines and cursor position.
   - Scrollback functionality is implemented by storing lines that scroll out of view and allowing the user to navigate this history.

3. **Handling Resize:**
   - When the window is resized, the `Screen` object's dimensions are updated, and the content is reflowed to match the new size.
   - The text widget and scrollbar are adjusted to ensure consistent user experience.

### Mapping Pyte's Display to a Text Widget: A Detailed Walkthrough

#### Introduction
In terminal emulation, representing the terminal's state in a GUI-based text widget can be complex. This document walks through the process of mapping `pyte`, a Python terminal emulator, to a text widget, focusing on how the terminal's grid of characters is translated to the linear structure of a text widget. 

#### Pyte's Screen Model
`pyte` maintains the terminal's state in a grid-like structure where each cell represents a character position on the screen. For example, a terminal screen of size 3x3 (rows x columns) looks like this:

```
+---+---+---+
| A | B | C |
+---+---+---+
| D | E | F |
+---+---+---+
| G | H | I |
+---+---+---+
```

#### Text Widget Structure
A text widget, on the other hand, represents content in a linear fashion, like a single string of text. The newline character (`\n`) is used to break lines. The equivalent representation of the terminal in a text widget would be:

```
A B C
D E F
G H I
```

#### Mapping Process
The process of mapping the `pyte` screen to the text widget involves two main steps: reading the grid and writing to the widget.

1. **Reading from Pyte's Screen:**
   Each row and column in `pyte`'s screen is read and concatenated into a string, with special handling for control characters like newlines.

   For the 3x3 grid, the process would be:
   ```
   Read Row 1: "A B C"
   Read Row 2: "D E F"
   Read Row 3: "G H I"
   ```

2. **Writing to the Text Widget:**
   The strings are then written to the text widget, with newlines inserted at the end of each row to maintain the grid structure.
   
   ```
   Text Widget Content:
   "A B C\nD E F\nG H I"
   ```

#### Handling Special Cases
1. **Cursor Position:**
   The cursor's position in `pyte` needs to be mapped to the text widget. This is done by calculating the cursor's linear position based on its row and column in the grid.

   For example, if the cursor is at position (2, 2) in a 3x3 grid, its position in the text widget would be after the 7th character (counting newlines).

   ```
   A B C
   D E[F]G H I
      ^
      Cursor
   ```

2. **Control Sequences:**
   `pyte` handles various control sequences (like color codes, cursor movement). When these sequences affect how text is displayed (like changing color), corresponding tags or styling need to be applied in the text widget.

3. **Scrollback Buffer:**
   To implement a scrollback buffer, lines that scroll out of view are stored in a separate buffer. The text widget's content is then a combination of this scrollback buffer and the current `pyte` screen.

   For instance, if the scrollback buffer contains two lines (`"J K L", "M N O"`) and the screen is as above, the text widget content would be:

   ```
   J K L
   M N O
   A B C
   D E F
   G H I
   ```

#### Conclusion
- Mapping `pyte`'s screen to a text widget involves carefully translating the grid structure into a linear format suitable for the text widget, handling special cases like cursor positioning and control sequences, and managing additional features like a scrollback buffer. With this approach, complex terminal interactions can be accurately represented within a GUI application.

### Build
`pip install wheel setuptools `
`python setup.py sdist bdist_wheel`