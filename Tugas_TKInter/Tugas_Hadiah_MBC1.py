import tkinter as tk
from time import strftime
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkcalendar import Calendar
todos ={}

def detailTodo(cb = None):
    win = tk.Toplevel()
    win.wm_title("Detail Kegiatan")
    selectedItem = treev.focus()
    selectedIndex = treev.item(selectedItem)['text']
    selectedTodo = todos[tanggal][selectedIndex]
    judul = tk.StringVar(value= selectedTodo['Judul'])
    tk.Label(win, text = "Tanggal:").grid(row =0, column= 0, sticky= "N")
    tk.Label(win, text ="{} | {}". format(tanggal, selectedTodo["Waktu"])).grid(row = 0, column= 1, sticky="E")
    tk.Label(win, text = "Judul:"). grid(row = 1, column= 0, sticky= "N")
    tk.Entry(win, state = "readonly", textvariable= judul).grid(row=1, column= 1, sticky= "E") #Merubah state disabled menjadi readonly
    tk.Label(win, text = "Keterangan:").grid(row=2, column=0, sticky= "N")
    keterangan = ScrolledText(win, width =12, height= 5)
    keterangan.grid(row = 2, column= 1, sticky= "E")
    keterangan.insert(tk.INSERT, selectedTodo["Keterangan"])
    keterangan.configure(state= "disabled")

def LoadTodos():
    global todos
    f = open('mytodo.dat', 'r')
    data = f.read()
    f.close()
    todos = eval(data)
    ListTodo()

def SaveTodos():
    f = open ('mytodo.dat', 'w')
    f.write(str(todos))
    f.close()

def delTodo():
    tanggal = str(cal.selection_get())
    selectedItem = treev.focus()
    todos[tanggal].pop(treev.item(selectedItem)['text'])
    ListTodo()