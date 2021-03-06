import tkinter as tk

class Example(tk.Frame):
    '''Illustrate how to drag items on a Tkinter canvas'''

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create a canvas
        self.canvas = tk.Canvas(width=400, height=400)
        self.canvas.pack(fill="both", expand=True)

        # this data is used to keep track of an 
        # item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        # create a couple of movable objects
        self._create_token((100, 100), "red")
        self._create_token((200, 100), "black")

        # add bindings for clicking, dragging and releasing over
        # any object with the "token" tag
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.on_token_press)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.on_token_release)
        self.canvas.tag_bind("token", "<B1-Motion>", self.on_token_motion)
#-----------------------------------------------------------------------------
        self.canvas.button2 = tk.Button(self.canvas, text="Button Test",
                                 command=self.button_move)
        self.canvas.button2.config(bg="cyan",fg="black")
        self.canvas.button2.pack(side='top')

        self.canvas.button3 = tk.Button(self.canvas, text="Button Test 2",
                            command=self.button_move2)
        self.canvas.button3.config(bg="cyan",fg="black")
        self.canvas.button3.pack(side='top')

        self.canvas.tag_bind("button2", "<ButtonPress-1>", self.button_move)
#-----------------------------------------------------------------------------
    def _create_token(self, coord, color):
        '''Create a token at the given coordinate in the given color'''
        (x,y) = coord
        self.canvas.create_oval(x-25, y-25, x+25, y+25, 
                                outline=color, fill=color, tags="token")

    def on_token_press(self, event):
        '''Begining drag of an object'''
        # record the item and its location
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def on_token_release(self, event):
        '''End drag of an object'''
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def on_token_motion(self, event):
        '''Handle dragging of an object'''
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
#-----------------------------------------------------------------------------
    def button_move(self, event=None):
        '''Handle dragging of an object'''
        # set movement amount
        delta_x = 15
        delta_y = 15
        # move the object the appropriate amount
        #self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        #self.canvas.move(self._drag_data[1], delta_x, delta_y)
        self.canvas.move(1, delta_x, delta_y) # moves item 1, when cursor is over token
        # record the new position
        #self._drag_data["x"] = event.x
        #self._drag_data["y"] = event.y

    def button_move2(self, event=None):
        items = self.canvas.find_withtag('token')
        print(items.__len__())
        self.canvas.move(items[0], 15, 15)

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()