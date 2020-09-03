from tkinter import *
root=Tk()
root.title("Simple Calculator")
entry=Entry(root,width=30,borderwidth=6)
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(number))

def button_clear():
    entry.delete(0,END)

def button_add():
    x=entry.get()
    global f_num
    global math
    math="adding"
    f_num=int(x)
    entry.delete(0,END)

def button_sub():
    x=entry.get()
    global s_num
    global math
    math="subtracting"
    s_num=int(x)
    entry.delete(0,END)

def button_mul():
    x=entry.get()
    global m_num
    global math
    math="multiplying"
    m_num=int(x)
    entry.delete(0,END)

def button_div():
    x=entry.get()
    global d_num
    global math
    math="division"
    d_num=int(x)
    entry.delete(0,END)

def button_square():
    x=entry.get()
    global s_num
    global math
    math="square"
    s_num=int(x)

def button_cube():
    x=entry.get()
    global s_num
    global math
    math="cube"
    s_num=int(x)


def button_equal():
    second_number=entry.get()
    entry.delete(0,END)
    if(math=="adding"):
        entry.insert(0,f_num + int(second_number))
    if(math=="subtracting"):
        entry.insert(0,s_num - int(second_number))
    if(math=="multiplying"):
        entry.insert(0,m_num * int(second_number))
    if(math=="division"):
        entry.insert(0,d_num / int(second_number))
    if(math=="square"):
        entry.insert(0,s_num*s_num)
    if(math=="cube"):
        entry.insert(0,s_num*s_num*s_num)

#define buttons
button1=Button(root,text="1",padx=40,pady=20,bg="yellow",command=lambda: button_click(1))
button2=Button(root,text="2",padx=40,pady=20,bg="yellow",command=lambda: button_click(2))
button3=Button(root,text="3",padx=40,pady=20,bg="yellow",command=lambda: button_click(3))
button4=Button(root,text="4",padx=40,pady=20,bg="yellow",command=lambda: button_click(4))
button5=Button(root,text="5",padx=40,pady=20,bg="yellow",command=lambda: button_click(5))
button6=Button(root,text="6",padx=40,pady=20,bg="yellow",command=lambda: button_click(6))
button7=Button(root,text="7",padx=40,pady=20,bg="yellow",command=lambda: button_click(7))
button8=Button(root,text="8",padx=40,pady=20,bg="yellow",command=lambda: button_click(8))
button9=Button(root,text="9",padx=40,pady=20,bg="yellow",command=lambda: button_click(9))
button0=Button(root,text="0",padx=40,pady=20,bg="yellow",command=lambda: button_click(0))
buttonadd=Button(root,text="+",padx=39,pady=20,bg="green",command=button_add)
buttonequal=Button(root,text="=",padx=91,pady=20,bg="blue",command=button_equal)
buttonclear=Button(root,text="Clear",padx=79,pady=20,bg="blue",command=button_clear)
buttonsquare=Button(root,text="^",padx=40,pady=40,bg="green",command=button_square)
buttoncube=Button(root,text="cube",padx=80,pady=40,bg="green",command=button_cube)

buttonsub=Button(root,text="-",padx=40,pady=20,bg="green",command=button_sub)
buttonmul=Button(root,text="*",padx=40,pady=20,bg="green",command=button_mul)
buttondiv=Button(root,text="/",padx=41,pady=20,bg="green",command=button_div)

#display buttons
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonclear.grid(row=4,column=1,columnspan=2)
buttonadd.grid(row=5,column=0)
buttonequal.grid(row=5,column=1,columnspan=2)

buttonsub.grid(row=6,column=0)
buttonmul.grid(row=6,column=1)
buttondiv.grid(row=6,column=2)

buttonsquare.grid(row=7,column=0)
buttoncube.grid(row=7,column=1,columnspan=2)

