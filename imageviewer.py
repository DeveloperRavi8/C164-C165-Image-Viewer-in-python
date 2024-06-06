from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Image Viewer")
root.geometry("500x500")
root.configure(bg="black")

img_path = ""
img = None  # Global reference to the image to prevent garbage collection

def openImg():
    global img_path, img
    img_path = filedialog.askopenfilename(title="Open Image", filetypes=[("Image files", "*.jpg *.gif *.png *.jpeg")])
    if img_path:  # Check if an image was selected
        im = Image.open(img_path)
        img = ImageTk.PhotoImage(im)
        img_label['image'] = img
        im.close()  # Close the PIL Image object

def rotateImg():
    global img_path, img
    if img_path:  # Check if an image is loaded
        im = Image.open(img_path)
        rotated_im = im.rotate(180)
        img = ImageTk.PhotoImage(rotated_im)
        img_label['image'] = img
        im.close()  # Close the PIL Image object

img_label = Label(root, background="green", highlightthickness=5, relief="solid", borderwidth=2)
img_label.place(relx=0.5, rely=0.5, anchor=CENTER)

openButton = Button(root, text="Open Image", font=("Bahnschrift Light SemiCondensed", 14, "bold"), command=openImg, padx=2, pady=2, bg="darkgray", borderwidth=0, foreground="white")
openButton.place(relx=0.5, rely=0.2, anchor=CENTER)

rotateButton = Button(root, text="Rotate Image", font=("Bahnschrift Light SemiCondensed", 14, "bold"), command=rotateImg, padx=2, pady=2, bg="darkgray", borderwidth=0, foreground="white")
rotateButton.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
