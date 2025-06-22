# Obsidian Math Formatter

A simple GUI-based Python tool for converting math expressions into **Obsidian-ready** format. This application helps transform mathematical expressions written in `\( ... \)` and `\[ ... \]` formats into the syntax that Obsidian's markdown renderer understands.

## Features

- Converts inline math expressions `\( ... \)` into `$ ... $`
- Converts block math expressions `\[ ... \]` into `$$ ... $$`
- Replaces `(i)` with `(2)` to avoid conflicts with formatting
- Cleans up excessive whitespace for a better markdown experience
- Provides a **simple GUI** using `tkinter` for easy text input and conversion

## Requirements

Ensure you have Python installed along with `tkinter` (pre-installed in standard Python distributions).

## Installation & Usage

1. Clone or download the repository:
   ```sh
   git clone https://github.com/YOUR_USERNAME/obsidian-math-formatter.git
   ```
2. Run the Python script:
   ```sh
   main.py
   ```
3. Enter your mathematical text into the input box.
4. Click **"Convert for Obsidian"** to transform the format.
5. Copy the processed text from the output box and paste it into **Obsidian**.

## Contributing

Feel free to fork the repository and open a **pull request** with improvements or additional features!
