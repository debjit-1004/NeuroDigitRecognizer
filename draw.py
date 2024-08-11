import tkinter as tk
from PIL import Image, ImageDraw

class PixelDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("28x28 Pixel Drawing App")
        
        # Canvas setup
        self.canvas_size = 28
        self.pixel_size = 20  # Each pixel will be 20x20 on the canvas
        self.canvas = tk.Canvas(root, width=self.canvas_size * self.pixel_size, height=self.canvas_size * self.pixel_size, bg='white')
        self.canvas.pack()
        
        # Create a 28x28 grayscale image
        self.image = Image.new('L', (self.canvas_size, self.canvas_size), color=255)  # 'L' mode for grayscale, 255 is white
        self.draw = ImageDraw.Draw(self.image)
        
        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.paint)
        
        # Save button
        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack()

    def paint(self, event):
        # Calculate pixel position
        x = event.x // self.pixel_size
        y = event.y // self.pixel_size
        
        # Draw pixel on canvas
        self.canvas.create_rectangle(x*self.pixel_size, y*self.pixel_size, (x+1)*self.pixel_size, (y+1)*self.pixel_size, fill='black', outline='black')
        
        # Draw pixel on grayscale image
        self.draw.point((x, y), fill=0)  # 0 is black in grayscale

    def save_image(self):
        # Save the image
        file_path = "drawing_grayscale.png"
        self.image.save(file_path)
        print(f"Image saved as {file_path}")

# Create the main window
root = tk.Tk()
app = PixelDrawingApp(root)
root.mainloop()
