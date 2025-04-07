""" This program implements an 'eraser' on a canvas.

The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. 
We then create an eraser rectangle which, when dragged around the canvas, sets all of the 
rectangles it is in contact with to white. """

import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser Canvas")
        
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        self.cells = []  # Store cell references
        self.create_grid()

        self.eraser = None
        self.canvas.bind("<Button-1>", self.create_eraser)
        self.canvas.bind("<Motion>", self.move_eraser)

    def create_grid(self):
        """Create a grid of blue cells"""
        num_rows = CANVAS_HEIGHT // CELL_SIZE
        num_cols = CANVAS_WIDTH // CELL_SIZE
        
        for row in range(num_rows):
            for col in range(num_cols):
                left_x = col * CELL_SIZE
                top_y = row * CELL_SIZE
                right_x = left_x + CELL_SIZE
                bottom_y = top_y + CELL_SIZE
                
                cell = self.canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="blue", outline="black")
                self.cells.append(cell)

    def create_eraser(self, event):
        """Create the eraser when the user clicks"""
        if self.eraser is None:
            self.eraser = self.canvas.create_rectangle(
                event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill="pink", outline="black"
            )

    def move_eraser(self, event):
        """Move the eraser and erase overlapping objects"""
        if self.eraser:
            self.canvas.coords(
                self.eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE
            )
            self.erase_objects(event.x, event.y)

    def erase_objects(self, x, y):
        """Erase objects in contact with the eraser"""
        overlapping_objects = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for obj in overlapping_objects:
            if obj != self.eraser:  # Don't erase the eraser itself
                self.canvas.itemconfig(obj, fill="white")

def main():
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
