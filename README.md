# snipToKeyboard

snipToKeyboard is a python script for Windows that stays active when ran.


Pressing the windows key and shift together activates the snipping function. Left click the mouse and drag it to capture a rectangle. This rectangle is converted to text using pytesseract. The text is then copied to the keyboard. To cancel the capture screen, press escape or the space bar. Press the left and right arrow key at the same time to terminate the program.


Imports:

 - pytesseract: pip install pytesseract
  
 - keyboard: pip install keyboard



Convert to taskbar shortcut:

 - Go to file location -> right click -> show more -> create shortcut
  
 - Right click on shortcut -> properties -> change target to "C:\Path\To\Python\python.exe" "C:\Path\To\Your\Script\run.py"
  
 - Right click on shortcut -> show more -> pin to taskbar
