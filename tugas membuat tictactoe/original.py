import tkinter.messagebox
from tkinter import *

# Jendela utama
play = Tk()
play.geometry('700x600')
play.title('Tic-Tac-Toe')
play.configure(bg="lightblue")

p1 = StringVar()
p2 = StringVar()
bclick = True
turns = 0

def btnclick(buttons):
    global bclick, turns
    if buttons['text'] == "" and bclick:
        buttons['text'] = 'X'
        bclick = False
        possibilities()
        turns += 1
    elif buttons['text'] == '' and not bclick:
        buttons['text'] = 'O'
        bclick = True
        possibilities()
        turns += 1
    else:
        tkinter.messagebox.showerror('Tic-Tac-Toe', 'Tidak valid! Pilih kotak lain.')

def possibilities():
    global turns
    # Pengecekan pemenang X
    if (b1['text'] == b2['text'] == b3['text'] == 'X' or
        b4['text'] == b5['text'] == b6['text'] == 'X' or
        b7['text'] == b8['text'] == b9['text'] == 'X' or
        b1['text'] == b4['text'] == b7['text'] == 'X' or
        b2['text'] == b5['text'] == b8['text'] == 'X' or
        b3['text'] == b6['text'] == b9['text'] == 'X' or
        b1['text'] == b5['text'] == b9['text'] == 'X' or
        b3['text'] == b5['text'] == b7['text'] == 'X'):
        tkinter.messagebox.showinfo('Tic-Tac-Toe', p1.get() + ' Menang!')
        reset_game()

    # Pengecekan pemenang O
    elif (b1['text'] == b2['text'] == b3['text'] == 'O' or
          b4['text'] == b5['text'] == b6['text'] == 'O' or
          b7['text'] == b8['text'] == b9['text'] == 'O' or
          b1['text'] == b4['text'] == b7['text'] == 'O' or
          b2['text'] == b5['text'] == b8['text'] == 'O' or
          b3['text'] == b6['text'] == b9['text'] == 'O' or
          b1['text'] == b5['text'] == b9['text'] == 'O' or
          b3['text'] == b5['text'] == b7['text'] == 'O'):
        tkinter.messagebox.showinfo('Tic-Tac-Toe', p2.get() + ' Menang!')
        reset_game()

    # Jika sudah 9 giliran → seri
    elif turns == 8:
        tkinter.messagebox.showwarning('Tic-Tac-Toe', 'Permainan Seri!')
        reset_game()

def reset_game():
    global bclick, turns
    bclick = True
    turns = 0
    for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        button.config(text="")

# Label Judul
Label(play, text='Tic-Tac-Toe', font=('calibri', 30), fg='blue').place(x=250, y=10)

# Input Nama Pemain
Label(play, text='PEMAIN 1 (X)', font=('calibri', 30), fg='RED').place(x=100, y=80)
Label(play, text='PEMAIN 2 (O)', font=('calibri', 30), fg='GREEN').place(x=100, y=130)

Entry(play, textvariable=p1, font=("calibri", 16), bg='lightblue').place(x=330, y=80)
Entry(play, textvariable=p2, font=("calibri", 16), bg='lightblue').place(x=330, y=130)

# Tombol Grid TicTacToe
b1 = Button(play, text='', font=('calibri', 25, 'bold'), width=7, height=2,
            bg='purple', fg='white', command=lambda: btnclick(b1))
b1.place(x=130, y=200)

b2 = Button(play, text='', font=('calibri', 25, 'bold'), width=7, height=2,
            bg='purple', fg='white', command=lambda: btnclick(b2))
b2.place(x=265, y=200)

b3 = Button(play, text='', font=('calibri', 25, 'bold'), width=7, height=2,
            bg='purple', fg='white', command=lambda: btnclick(b3))
b3.place(x=400, y=200)

b4 = Button(play, text='', font=('calibri', 25, 'bold'), width=7, height=2,
            bg='purple', fg='white', command=lambda: btnclick(b4))
b4.place(x=130, y=317)

b5 = Button(play, text='', font=('calibri', 25, 'bold'), width=7, height=2,
            bg='purple', fg='white', command=lambda: btnclick(b5))
b5.place(x=265, y=317)

b6 = Button(play, text='', font=('calibri', 25, 'bold'), width=7, height=2,
            bg='purple', fg='white', command=lambda: btnclick(b6))
b6.place(x=400, y=317)

b7 = Button(play, text='', font=('calibri', 25, 'bold'), width=7, height=2,
            bg='purple', fg='white', command=lambda: btnclick(b7))
b7.place(x=130, y=434)

b8 = Button(play, text='', font=('calibri', 25, 'bold'), width=7, height=2,
            bg='purple', fg='white', command=lambda: btnclick(b8))
b8.place(x=265, y=434)

b9 = Button(play, text='', font=('calibri', 25, 'bold'), width=7, height=2,
            bg='purple', fg='white', command=lambda: btnclick(b9))
b9.place(x=400, y=434)

# Tombol Reset
reset_button = Button(play, text='Reset', font=('calibri', 20, 'bold'),
                      width=10, bg='yellow', fg='black', command=reset_game)
reset_button.place(x=550, y=500)

play.mainloop()