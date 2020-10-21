#English to Hindi Translator
import tkinter as tk
from googletrans import Translator
root= tk.Tk()
root.title("I AM A TRANSLATOR")

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

label1 = tk.Label(root, text='Translator English to Hindi')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)
        
label2 = tk.Label(root, text='Enter Text in English:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def translatethindi():
    try:
        pack_forget()
    except:
        pass
        
    txt = entry1.get()
    translator = Translator()
    res = translator.translate(txt,src="en",dest="hi")
    label3 = tk.Label(root, text = res.text, bg = "gray")
    label3.config(font=('helvetica', 20))
    label3.config(width=24)
    canvas1.create_window(200, 220, window=label3)
    canvas1.pack()
    
button1 = tk.Button(text='Translate', command=translatethindi, bg='blue', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
