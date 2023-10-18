import tkinter as tk
window=tk.Tk()
window.title("tic-tac")
game_board = tk.Canvas(window, width=300, height=300)
game_board.pack()
cell_size = 100  #size of kletka

for row in range(3):
    for col in range(3):
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        game_board.create_rectangle(x1, y1, x2, y2)
window.mainloop()