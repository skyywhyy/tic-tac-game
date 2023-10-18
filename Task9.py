def on_cell(event):
    x, y = event.x, event.y
    col = x // cell_size
    row = y // cell_size
    if game_board[row][col] == " ":
        game_board[row][col] = current_player
        draw_symbol(row, col)
        switch_player()
def draw_symbol(row, col):
    x_center = col * cell_size + cell_size // 2
    y_center = row * cell_size + cell_size // 2
    symbol = game_board[row][col]
    if symbol == "X":
        board.create_text(x_center, y_center, text="X", font=("Arial", 24), fill="blue")
    elif symbol == "O":
        board.create_text(x_center, y_center, text="O", font=("Arial", 24), fill="red")
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def start_game(player):
    global current_player
    current_player = player
    main_menu.destroy()
def quit_game():
    window.quit()

import tkinter as tk
main_menu = tk.Tk()
main_menu.title("Выберите начинающего игрока")
label = tk.Label(main_menu, text="Выберите начинающего игрока:")
label.pack()
btn_x = tk.Button(main_menu, text="Игрок X", command=lambda: start_game("X"))
btn_o = tk.Button(main_menu, text="Игрок O", command=lambda: start_game("O"))
btn_quit = tk.Button(main_menu, text="Выход", command=quit_game)
btn_x.pack()
btn_o.pack()
btn_quit.pack()
main_menu.mainloop()
# 
window=tk.Tk()
game_board = [[" " for _ in range(3)] for _ in range(3)]
main_menu = tk.Menu(window)
window.config(menu=main_menu)
current_player = None  # Глобальная переменная для хранения выбора игрока
window.title("tic-tac")
board = tk.Canvas(window, width=300, height=300)
board.pack()
cell_size = 100  #size of cell
cell_otst = 5  # Отступ внутри клетки
for row in range(3):
    for col in range(3):
        x1 = col * cell_size + cell_otst 
        y1 = row * cell_size + cell_otst 
        x2 = x1 + cell_size - cell_otst 
        y2 = y1 + cell_size - cell_otst 
        board.create_rectangle(x1, y1, x2, y2)
board.bind("<Button-1>", on_cell)
window.mainloop()
