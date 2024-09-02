import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    # khaled
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

        self.label = tk.Label(self.root, text=f"Your turn ({self.current_player})", font=("Helvetica", 16))
        self.label.pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.frame, text="", width=10, height=3, font=("Helvetica", 16),
                                              command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def check_win(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        return all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3))

    def is_full(self):
        return all(cell != "" for row in self.board for cell in row)

    def make_computer_move(self):
        if self.is_full():
            return

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    self.board[row][col] = "O"
                    self.buttons[row][col]['text'] = "O"
                    return

    def on_click(self, row, col):
        if self.board[row][col] == "" and not self.check_win("X"):
            self.board[row][col] = "X"
            self.buttons[row][col]['text'] = "X"

            if self.check_win("X"):
                messagebox.showinfo("Tic Tac Toe", "You win!")
                self.root.quit()
            elif self.is_full():
                messagebox.showinfo("Tic Tac Toe", "Draw!")
                self.root.quit()
            else:
                self.make_computer_move()
                if self.check_win("O"):
                    messagebox.showinfo("Tic Tac Toe", "Computer wins!")
                    self.root.quit()
            self.current_player = 'X' if self.current_player == 'O' else 'O'
            self.label.config(text=f"Your turn ({self.current_player})")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
