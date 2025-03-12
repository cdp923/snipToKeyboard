import tkinter as tk
from PIL import ImageGrab, Image
import numpy as np
import pytesseract
import keyboard
import os

class screen_capture:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.3)
        self.root.configure(bg='black')
        
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None
        self.rect = None
        self.canvas = tk.Canvas(self.root, cursor="cross", bg="grey11")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.canvas.bind("<ButtonPress-3>", self.on_right_click)
        self.root.bind("<space>", self.cancel_capture)
        self.root.bind("<Escape>", self.cancel_capture)
        
    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red', width=3, fill="white", stipple="gray75")
        
    def on_mouse_drag(self, event):
        self.current_x = event.x
        self.current_y = event.y
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.current_x, self.current_y)
        
    def on_button_release(self, event):
        if self.start_x is not None and self.start_y is not None and self.current_x is not None and self.current_y is not None:
            self.root.attributes("-fullscreen", False)
            self.root.destroy()
            
            x1 = min(self.start_x, self.current_x)
            y1 = min(self.start_y, self.current_y)
            x2 = max(self.start_x, self.current_x)
            y2 = max(self.start_y, self.current_y)
            
            self.snip_image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            #self.snip_image.show()
            text = pytesseract.image_to_string(self.snip_image)
            text = " ".join(text.splitlines())
            print(text)
            clip = 'echo '+text+'| clip'
            os.system(clip)
        #self.snip_image.save("snip.png")
    def on_right_click(self, event):
        # Reset the selection rectangle and allow the user to try again
        if self.rect:
            self.canvas.delete(self.rect)  # Delete the existing rectangle
            self.rect = None
            self.start_x = None
            self.start_y = None
            self.current_x = None
            self.current_y = None
    def cancel_capture(self, event=None):
        # Close the application without capturing anything
        self.root.attributes("-fullscreen", False)
        self.root.destroy() 
        

def start_screen_capture():
    snipper = screen_capture()
    snipper.root.mainloop()

# Set the hotkey ("win+shift") to trigger the screen capture
keyboard.add_hotkey("win+shift", start_screen_capture)


# Keep the script running and waiting for the hotkey
keyboard.wait('left+right')