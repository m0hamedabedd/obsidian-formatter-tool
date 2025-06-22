import tkinter as tk
from tkinter import scrolledtext
import re # Regular expression library

def convert_text():
    """Gets text from input, performs conversions, and puts it in output."""
    input_text = input_widget.get("1.0", tk.END) # Get all text from input box

    # 1. Replace (i) with (2) - Do this first to avoid interfering with math delimiters
    converted_text = input_text.replace('(i)', '(2)')

    # 2. Replace block math delimiters \[ ... \] with $$ ... $$ and add spacing
    # Use re.DOTALL so '.' matches newline characters for multi-line equations
    def replace_block_math(match):
        content = match.group(1).strip()  # Remove leading/trailing whitespace from equation
        return f'\n\n$${content}$$\n\n'
    
    converted_text = re.sub(r'\\\[(.*?)\\\]', replace_block_math, converted_text, flags=re.DOTALL)

    # 3. Replace inline math delimiters \( ... \) with $ ... $ and add minimal spacing
    def replace_inline_math(match):
        content = match.group(1).strip()  # Remove leading/trailing whitespace from equation
        return f' ${content}$ '
    
    converted_text = re.sub(r'\\\((.*?)\\\)', replace_inline_math, converted_text, flags=re.DOTALL)

    # 4. Clean up excessive whitespace
    # Remove multiple consecutive newlines (more than 2) and replace with double newline
    converted_text = re.sub(r'\n{3,}', '\n\n', converted_text)
    
    # Remove trailing whitespace from each line
    converted_text = re.sub(r'[ \t]+$', '', converted_text, flags=re.MULTILINE)
    
    # Remove leading/trailing whitespace from the entire text
    converted_text = converted_text.strip()

    # Update the output box
    output_widget.configure(state='normal') # Allow editing/inserting
    output_widget.delete("1.0", tk.END)     # Clear previous output
    output_widget.insert(tk.END, converted_text) # Insert new text
    output_widget.configure(state='disabled') # Make read-only again

# --- GUI Setup ---

# Create the main window
window = tk.Tk()
window.title("Obsidian Math Formatter")
window.geometry("700x500") # Set initial window size

# Input Area Label
input_label = tk.Label(window, text="Input Text:")
input_label.pack(pady=(10, 0)) # Add some padding above

# Input Text Widget (with scrollbars)
input_widget = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10)
input_widget.pack(pady=5, padx=10, fill="both", expand=True)

# Convert Button
convert_button = tk.Button(window, text="Convert for Obsidian", command=convert_text)
convert_button.pack(pady=5)

# Output Area Label
output_label = tk.Label(window, text="Output Text (Obsidian Ready):")
output_label.pack(pady=(5, 0))

# Output Text Widget (with scrollbars, initially disabled)
output_widget = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10, state='disabled')
output_widget.pack(pady=5, padx=10, fill="both", expand=True)

# Start the GUI event loop
window.mainloop()