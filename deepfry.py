import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageFilter, ImageEnhance

#hiding main Tk window
root = tk.Tk()
root.withdraw()

try:

	file_path = filedialog.askopenfilename(
		title = "pick your image",
		filetypes = [("image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
	)


	if file_path:
	
		img = Image.open(file_path)
		
		#edits the image	
		
		img1 = ImageEnhance.Contrast(img).enhance(2.5)		
		img1 = ImageEnhance.Color(img1).enhance(9.5)		
		img1 = ImageEnhance.Sharpness(img1).enhance(18.5)

		img1.show()

	else:	
		print("no file selected, bye!")


except FileNotFoundError:
	print(f"ERROR: the file '{file_path}' was not found")
except IOError:
	print(f"ERROR: could not open or read the file '{file_path}'")
except Exception as e:
	print(f"unexpected error occurred: {e}")
