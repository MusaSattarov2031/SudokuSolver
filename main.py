import tkinter as tk
from tkinter import filedialog

from sudokuReader import main
from sudokuSolve import solveSudoku


def upload_image():
    file_path=filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *,jpeg *.png")])

    if file_path:
        sudoku_array=main(file_path)

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Sudoku Array: \n")
        result_text.insert(tk.END, str(sudoku_array))
        
        solved_sudoku=solveSudoku(sudoku_array)

        result_text.insert(tk.END, "\nSolved Sudoku:\n")
        result_text.insert(tk.END, str(solved_sudoku))

root=tk.Tk()
root.title("Sudoku Solver")

upload_button=tk.Button(root, text="Upload Sudoku Image", command=upload_image)
upload_button.pack(pady=20)

result_label=tk.Label(root, text="Sudoku Array: ")
result_label.pack()

result_text=tk.Text(root,  width=50, height=15)
result_text.pack(pady=10)

root.mainloop()