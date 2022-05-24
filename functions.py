import tkinter
from tkinter import*
import pymysql

def iExit(root):
    iExit = tkinter.messagebox.askyesno("MySQL Connector", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def DisplayData(window, data_records):
    sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
    cur = sqlCon.cursor()
    cur.execute(f"Select * from {window}")
    result = cur.fetchall()
    if len(result) != 0:
        data_records.delete(*data_records.get_children())
        for row in result:
            data_records.insert('', END, values=row)
    sqlCon.commit()
    sqlCon.close()

def Separate(fetch):
    str_fetch = fetch[0][0]
    list = str_fetch.split(",")
    list.insert(0, ' ')
    return list




