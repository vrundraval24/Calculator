from tkinter import *
import time

root = Tk()
root.overrideredirect(True) 

calc_width = 285
calc_height = 375

root.geometry(f"{calc_width}x{calc_height}+540+150")

def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def do_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

def on_enter(event):
    close_button.config(background='firebrick2', foreground= "white")
    
def on_leave(event):
    close_button.config(background='firebrick3', foreground= "white")


# make a frame for the title bar
title_bar = Frame(root, bg="grey85", highlightbackground="black", highlightthickness=1)

label0 = Label(title_bar, text="  Calculator", bg="grey85", fg="grey20", font=("",12,""), anchor=NW, height=1)
label0.pack(side=LEFT)



# put a close button on the title bar
close_button = Button(title_bar, text='X',bg="firebrick3",width=3,
fg="white",font=("",12,""), relief=FLAT, bd=-2,
activebackground='firebrick3', activeforeground='white')

# pack the widgets
title_bar.pack(expand=1, fill=X, anchor=N)
close_button.pack(side=RIGHT)

def close(event):
    time.sleep(0.2)
    root.destroy()

close_button.bind('<Enter>', on_enter)
close_button.bind('<Leave>', on_leave)
close_button.bind("<Button-1>", close)

title_bar.bind("<ButtonPress-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", do_move)

label0.bind("<ButtonPress-1>", start_move)
label0.bind("<ButtonRelease-1>", stop_move)
label0.bind("<B1-Motion>", do_move)


def func1(event):


    try:
        
        text = event.widget.cget("text")

        if len(data.get()) > 11:


            if text == 0 or text == 1 or text == 2 or text == 3 or text == 4 or text == 5 or text == 6 or text == 7 or text == 8 or text == 9 or text == '.':
                pass
        
            else:
                     
                if data.get() == 'Error':
                    data.set("0")
                
                if data.get() == '0':
                    data.set("")
                    
                    if text == 'AC':
                        data.set("0")
                        data0.set("")

                    elif text == 'C':
                        data.set("0")

                    elif text == '=':
                        if data.get() == '':
                            if data0.get()[-1] == '+' or data0.get()[-1] == '-' or data0.get()[-1] == '*' or data0.get()[-1] == '/':
                                data0.set(data0.get()[:-1])
                                data.set(data0.get())
                                data0.set("")

                        elif data.get() == '':
                            data.set("0")


                    elif text == '.':
                        if '.' in data.get():
                            pass
                            
                        else:
                            data.set("0.")

                    elif text == '+' or text == '-' or text == '*' or text == '/':
                            data0.set(data0.get()[:-1])
                            data0.set(data0.get() + text)
                            data.set("0")

                    else:
                        data.set(data.get() + str(text))

                elif text == '+' or text == '-' or text == '*' or text == '/':
                    data0.set(data0.get() + data.get() + text)
                
                    if data0.get()[-1] == '+' or data0.get()[-1] == '-' or data0.get()[-1] == '*' or data0.get()[-1] == '/' :
                        data0.set(data0.get()[:-1])
                        data0.set(eval(data0.get()))
                        data0.set(data0.get() + text) 

                        data.set('0')

                elif text == '=':
                    
                    data.set(data0.get() + data.get())
                    data.set(eval(data.get()))
                    data0.set("")

                    if '.' in data.get():
                        
                        for i in range(1, len(data.get())):
                            if data.get()[i] == '.':
                                a = i + 1
                                b = len(data.get())
                                
                                if a > 9:
                                    data.set("Error")
                                    data0.set("")
                                
                                elif b - a >= 3:
                                    data.set(data.get()[0: a + 3])
                                    break                                
                                
                    elif len(data.get()) > 12:
                        data.set("Error")
                        data0.set("")

                elif text == '.':
                    if data.get()[-1] == '+' or data.get()[-1] == '-' or data.get()[-1] == '*' or data.get()[-1] == '/':
                        data.set(data.get() + '0.')
                        
                    elif '.' in data.get():
                        a = data.get()
                        l = []
                        x = 0
                        
                        for i in range (1, len(a)):
                            if a[i] == '+' or a[i] == '-' or a[i] == '*' or a[i] == '/':
                
                                l.append(a[x:(i)])
                                x = i + 1

                        l.append(a[x:])

                        if '.' in l[-1]:
                            pass
                        else:
                            data.set(data.get() + '.')            

                    else:
                        data.set(data.get() + str(text))


                elif text == '+' or text == '-' or text == '*' or text == '/': 
                    if data.get()[-1] == '+' or data.get()[-1] == '-' or data.get()[-1] == '*' or data.get()[-1] == '/':
                        data.set(data.get()[:-1])
                        data.set(data.get() + str(text))
                    
                    elif data.get()[-1] == '.':
                        data.set(data.get() + '0' + text)

                    else:
                        data.set(data.get() + str(text))

                elif text == 'C':
                    data.set(data.get()[:-1])  
                    if data.get() == "":
                        data.set("0")

                elif text == 'AC':
                    data.set("0")
                    data0.set("")

                else:
                    data.set(data.get() + str(text))
        else:     
                if data.get() == 'Error':
                    data.set("0")
                
                if data.get() == '0':

                    data.set("")
                    
                    if text == 'AC':
                        data.set("0")
                        data0.set("")

                    elif text == 'C':
                        data.set("0")

                    elif text == '=':  

                        if data.get() == '':
                            
                            if data0.get() == '':
                                data.set("0")                            
                                data0.set("")                            

                            elif data0.get()[-1] == '+' or data0.get()[-1] == '-' or data0.get()[-1] == '*' or data0.get()[-1] == '/':
                                
                                try:
                                    if data0.get()[-2] in data0.get():
                                        data0.set(data0.get()[:-1])
                                        data.set(data0.get())
                                        data0.set("")  

                                except:
                                    if data0.get()[-1] == '+' or data0.get()[-1] == '-' or data0.get()[-1] == '*' or data0.get()[-1] == '/':
                                        data.set("0")
                                        data0.set("")                                
                                            

                    elif text == '.':
                        if '.' in data.get():
                            pass
                            
                        else:
                            data.set("0.")

                    elif text == '+' or text == '-' or text == '*' or text == '/':
                            data0.set(data0.get()[:-1])
                            data0.set(data0.get() + text)
                            data.set("0")

                    else:
                        data.set(data.get() + str(text))


                elif text == '+' or text == '-' or text == '*' or text == '/':
                    data0.set(data0.get() + data.get() + text)
                
                    if data0.get()[-1] == '+' or data0.get()[-1] == '-' or data0.get()[-1] == '*' or data0.get()[-1] == '/' :
                        data0.set(data0.get()[:-1])
                        data0.set(eval(data0.get()))
                        data0.set(data0.get() + text) 

                        data.set('0')

                elif text == '=':
                    
                    data.set(data0.get() + data.get())
                    data.set(eval(data.get()))
                    data0.set("")

                    if '.' in data.get():
                        
                        for i in range(1, len(data.get())):
                            if data.get()[i] == '.':
                                a = i + 1
                                b = len(data.get())
                                
                                if a > 9:
                                    data.set("Error")
                                    data0.set("")
                                
                                elif b - a >= 3:
                                    data.set(data.get()[0: a + 3])
                                    break                                
                                
            
                    elif len(data.get()) > 12:
                        data.set("Error")
                        data0.set("")

                elif text == '.':
                    if data.get()[-1] == '+' or data.get()[-1] == '-' or data.get()[-1] == '*' or data.get()[-1] == '/':
                        data.set(data.get() + '0.')
                        
                    elif '.' in data.get():
                        a = data.get()
                        l = []
                        x = 0
                        
                        for i in range (1, len(a)):
                            if a[i] == '+' or a[i] == '-' or a[i] == '*' or a[i] == '/':
                
                                l.append(a[x:(i)])
                                x = i + 1

                        l.append(a[x:])

                        if '.' in l[-1]:
                            pass
                        else:
                            data.set(data.get() + '.')            

                    else:
                        data.set(data.get() + str(text))


                elif text == '+' or text == '-' or text == '*' or text == '/': 
                    if data.get()[-1] == '+' or data.get()[-1] == '-' or data.get()[-1] == '*' or data.get()[-1] == '/':
                        data.set(data.get()[:-1])
                        data.set(data.get() + str(text))
                    
                    elif data.get()[-1] == '.':
                        data.set(data.get() + '0' + text)

                    else:
                        data.set(data.get() + str(text))

                elif text == 'C':
                    data.set(data.get()[:-1])  
                    if data.get() == "":
                        data.set("0")

                elif text == 'AC':
                    data.set("0")
                    data0.set("")

                else:
                    data.set(data.get() + str(text))
    except:
        data.set("Error")
        data0.set("")    

def func2(event):
    pass

data0 = StringVar()
data0.set("")

lable1 = Label(root, textvariable=data0, bg="grey12",fg="sienna1",font=("",10,""), anchor=SE, height=1)
lable1.pack(expand=True, fill=BOTH)

data = StringVar()
data.set("0")

lable2 = Label(root, textvariable=data, bg="grey12",fg="white",font=("",30,""), anchor=SE, height=1)
lable2.pack(expand=True, fill=BOTH)

f0 = Frame(root, bg='black')
f1 = Frame(root, bg='black')
f2 = Frame(root, bg='black')
f3 = Frame(root, bg='black')
f4 = Frame(root, bg='black')
f0.pack()
f1.pack()
f2.pack()
f3.pack()
f4.pack()

def button(frame, texts, bgcolour, button_width, button_height, fgcolour, font, abgc, hebg, func):

    button = Button(frame, text=texts, bg=bgcolour,width=button_width, height=button_height,
    fg=fgcolour,font=("",font,""), relief=FLAT, bd=-2,
    activebackground=abgc, activeforeground=fgcolour) 

    # def func(event):
    #     print("Pressed")

    def on_enter1(event):
        button.config(background=hebg, foreground= fgcolour)
    
    def on_leave1(event):
        button.config(background=bgcolour, foreground= fgcolour)

    button.pack(side=LEFT, padx=1, pady=1)

    button.bind('<Enter>', on_enter1)
    button.bind('<Leave>', on_leave1)
    button.bind("<Button-1>", func)  

def all_buttons():

    button(f0,'AC', 'gray85',     4, 1, 'sienna2',    20, 'grey60',  'grey70',  func1)
    button(f0, '' , 'gray85',     4, 1, 'black',      20, 'grey60',  'grey70',  func2)
    button(f0, '' , 'gray85',     4, 1, 'black',      20, 'grey60',  'grey70',  func2)
    button(f0, '/', 'gray85',     4, 1, 'black',      20, 'grey60',  'grey70',  func1)
    button(f1,   7, 'gray90',     4, 1, 'black',      20, 'grey60',  'grey80',  func1)
    button(f1,   8, 'gray90',     4, 1, 'black',      20, 'grey60',  'grey80',  func1)
    button(f1,   9, 'gray90',     4, 1, 'black',      20, 'grey60',  'grey80',  func1)
    button(f1, '*', 'gray85',     4, 1, 'black',      20, 'grey60',  'grey70',  func1)
    button(f2,   4, 'gray90',     4, 1, 'black',      20, 'grey60',  'grey80',  func1)
    button(f2,   5, 'gray90',     4, 1, 'black',      20, 'grey60',  'grey80',  func1)
    button(f2,   6, 'gray90',     4, 1, 'black',      20, 'grey60',  'grey80',  func1)
    button(f2, '-', 'gray85',     4, 1, 'black',      20, 'grey60',  'grey70',  func1)
    button(f3,   1, 'gray90',     4, 1, 'black',      20, 'grey60',  'grey80',  func1)
    button(f3,   2, 'gray90',     4, 1, 'black',      20, 'grey60',  'grey80',  func1)
    button(f3,   3, 'gray90',     4, 1, 'black',      20, 'grey60',  'grey80',  func1)
    button(f3, '+', 'gray85',     4, 1, 'black',      20, 'grey60',  'grey70',  func1)
    button(f4, 'C', 'gray85',     4, 1, 'sienna2',    20, 'grey60',  'grey70',  func1)
    button(f4,   0, 'gray90',     4, 1, 'black',      20, 'grey60',  'grey80',  func1)
    button(f4, '.', 'gray85',     4, 1, 'black',      20, 'grey60',  'grey70',  func1)
    button(f4, '=', 'sienna1',    4, 1, 'white',      20, 'sienna3', 'sienna2', func1)

all_buttons()

root.mainloop()