import random
import tkinter as tk
import tkinter.messagebox as mb
from PIL import Image, ImageTk

MAX_BOARD_SIZE = 500

class Application(tk.Frame):

    def __init__(self, image, board_grid=3):
        tk.Frame.__init__(self)
        self.grid()
        self.board_grid = board_grid if board_grid > 2 else 3
        self.load_image(image)
        self.steps = 0
        self.create_widgets()
        self.create_events()
        self.create_board()
        self.show()

    def load_image(self, image):
        image = Image.open(image)
        board_size = min(image.size)
        if image.size[0] != image.size[1]:
            image = image.crop((0, 0, board_size, board_size))
        if board_size > MAX_BOARD_SIZE:
            board_size = MAX_BOARD_SIZE
            image = image.resize((board_size, board_size), Image.ANTIALIAS)
        self.image = image
        self.board_size = board_size
        self.piece_size = self.board_size / self.board_grid

    def create_widgets(self):
        args = dict(width=self.board_size, height=self.board_size)
        self.canvas = tk.Canvas(self, **args)
        self.canvas.grid()

    def create_events(self):
        self.canvas.bind_all('<KeyPress-Up>', self.slide)
        self.canvas.bind_all('<KeyPress-Down>', self.slide)
        self.canvas.bind_all('<KeyPress-Left>', self.slide)
        self.canvas.bind_all('<KeyPress-Right>', self.slide)

    def slide(self, event):
        pieces = self.get_pieces_around()
        if event.keysym in ('Up') and pieces['bottom']:
            self._slide(pieces['bottom'], pieces['center'], 
                        (0, -self.piece_size))
        if event.keysym in ('Down') and pieces['top']:
            self._slide(pieces['top'], pieces['center'],
                        (0, self.piece_size))
        if event.keysym in ('Left') and pieces['right']:
            self._slide(pieces['right'], pieces['center'],
                        (-self.piece_size, 0))
        if event.keysym in ('Right') and pieces['left']:
            self._slide(pieces['left'], pieces['center'],
                        (self.piece_size, 0))
        self.check_status()

    def _slide(self, from_, to, coord):
        self.canvas.move(from_['id'], *coord)
        to['pos_a'], from_['pos_a'] = from_['pos_a'], to['pos_a']
        self.steps += 1

    def get_pieces_around(self):
        pieces = {'center': None,
                  'right' : None,
                  'left'  : None,
                  'top'   : None,
                  'bottom': None}
        for piece in self.board:
            if not piece['visible']:
                pieces['center'] = piece
                break
        x0, y0 = pieces['center']['pos_a']
        for piece in self.board:
            x1, y1 = piece['pos_a']
            if y0 == y1 and x1 == x0 + 1:
                pieces['right'] = piece
            if y0 == y1 and x1 == x0 - 1:
                pieces['left'] = piece
            if x0 == x1 and y1 == y0 - 1:
                pieces['top'] = piece
            if x0 == x1 and y1 == y0 + 1:
                pieces['bottom'] = piece
        return pieces

    def create_board(self):
        self.board = []
        for x in range(self.board_grid):
            for y in range(self.board_grid):
                x0 = x * self.piece_size
                y0 = y * self.piece_size
                x1 = x0 + self.piece_size
                y1 = y0 + self.piece_size
                image = ImageTk.PhotoImage(
                        self.image.crop((x0, y0, x1, y1)))
                piece = {'id'     : None,
                         'image'  : image,
                         'pos_o'  : (x, y),
                         'pos_a'  : None,
                         'visible': True}
                self.board.append(piece)
        self.board[-1]['visible'] = False

    def check_status(self):
        for piece in self.board:
            if piece['pos_a'] != piece['pos_o']:
                return
        title = 'Ganaste!'
        message = 'Lo resolviste en %d movidas!' % self.steps
        mb.showinfo(title, message)

    def show(self):
        random.shuffle(self.board)
        index = 0
        for x in range(self.board_grid):
            for y in range(self.board_grid):
                self.board[index]['pos_a'] = (x, y)
                if self.board[index]['visible']:
                    x1 = x * self.piece_size
                    y1 = y * self.piece_size
                    image = self.board[index]['image']
                    id = self.canvas.create_image(
                            x1, y1, image=image, anchor=tk.NW)
                    self.board[index]['id'] = id
                index += 1


if __name__ == '__main__':

    app = Application('EPN.png', 3)
    app.master.title('Sliding puzzle')
    app.mainloop()

