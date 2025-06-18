import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

# Function Definitions
def search_youtube():
    query = entry.get().strip()
    if query:
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)

def search_google():
    query = entry.get().strip()
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

def search_instagram():
    username = entry.get().strip().replace('@', '')
    if username:
        url = f"https://www.instagram.com/{username}/"
        webbrowser.open(url)

# Main Window
root = tk.Tk()
root.title("AI Assistant")
root.configure(bg="#2c3e50")
root.geometry("600x400")

# Styling Options
label_style = {"bg": "#2c3e50", "fg": "#ecf0f1", "font": ("Arial", 14)}
entry_style = {"bg": "#ecf0f1", "fg": "#2c3e50", "font": ("Arial", 12), "relief": "flat"}
button_style = {"bg": "#3498db", "fg": "white", "activebackground": "#2980b9", "font": ("Arial", 12), "width": 30, "relief": "flat"}

# Widgets
Label(root, text="Enter your command:", **label_style).pack(pady=20)

entry = Entry(root, **entry_style, width=50)
entry.pack(pady=10)

Button(root, text="Search on YouTube", command=search_youtube, **button_style).pack(pady=5)
Button(root, text="Search on Google", command=search_google, **button_style).pack(pady=5)
Button(root, text="Search on Instagram", command=search_instagram, **button_style).pack(pady=5)

root.mainloop()
