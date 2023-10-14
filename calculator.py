from tkinter import *
from tkinter import messagebox


master = Tk()#class#
#master.geometry("800x400")#screen size#
master.title("this is a title!")#title#
#master.resizable(width=False,height=False)#screen resizible#


firstNum = ""

secondNum = ""

action = ""


num1Bool = True

num2Bool = False


def equal():

    global num1Bool, num2Bool, firstNum, secondNum, action

    if action == "x":

        try:

            messagebox.showinfo("Number", f"Your number is: {int(firstNum) * int(secondNum)}")

        except:

            messagebox.showerror("Error", "Number incorect")


    num1Bool = True

    num2Bool = False

    firstNum = ""

    secondNum = ""

    action = ""

    actionVar.set("")

    fristVar.set("")

    secondVar.set("")



def multy():

    global action, num1Bool, num2Bool

    action = "x"

    actionVar.set(action)

    num1Bool = False

    num2Bool = True



def num_1():
    
    global secondNum, firstNum

    if num1Bool:

        firstNum += "1"

        fristVar.set(firstNum)        



    if num2Bool:

        secondNum += "1"

        secondVar.set(secondNum)



def num_2():
    
    global secondNum, firstNum

    if num1Bool:

        firstNum += "2"

        fristVar.set(firstNum)        



    if num2Bool:

        secondNum += "2"

        secondVar.set(secondNum)




def num_3():
    
    global secondNum, firstNum

    if num1Bool:

        firstNum += "3"

        fristVar.set(firstNum)        

 

    if num2Bool:

        secondNum += "3"

        secondVar.set(secondNum)







#first number
fristVar = StringVar()
firstNum_label = Label(master, textvariable=fristVar, font="60", width=10, bg="white")
firstNum_label.grid(row=0, column=0, sticky=W, pady=5)


#action type
actionVar = StringVar()
action_label = Label(master, textvariable=actionVar, font="60", width=10, bg="white")
action_label.grid(row=0, column=1, sticky=W, pady=5)


#second number
secondVar = StringVar()
secondNum_label = Label(master, textvariable=secondVar, font="60", width=10, bg="white")
secondNum_label.grid(row=0, column=2, sticky=W, pady=5)


button1 = Button(master, text="1", command=num_1, width=10, height=4)
button1.grid(row=1, column=0 , sticky=W)

button2 = Button(master, text="2", command=num_2, width=10, height=4)
button2.grid(row=1, column=1 , sticky=W)

button3 = Button(master, text="3", command=num_3, width=10, height=4)
button3.grid(row=1, column=2 , sticky=W)


button4 = Button(master, text="4", command=None, width=10, height=4)
button4.grid(row=2, column=0 , sticky=W)

button5 = Button(master, text="5", command=None, width=10, height=4)
button5.grid(row=2, column=1 , sticky=W)

button6 = Button(master, text="6", command=None, width=10, height=4)
button6.grid(row=2, column=2 , sticky=W)


button7 = Button(master, text="7", command=None, width=10, height=4)
button7.grid(row=3, column=0 , sticky=W)

button8 = Button(master, text="8", command=None, width=10, height=4)
button8.grid(row=3, column=1 , sticky=W)

button9 = Button(master, text="9", command=None, width=10, height=4)
button9.grid(row=3, column=2 , sticky=W)

button0 = Button(master, text="0", command=None, width=10, height=4)
button0.grid(row=4, column=1 , sticky=W)


buttonMulty = Button(master, text="x", command=multy, width=10, height=4)
buttonMulty.grid(row=4, column=0 , sticky=W)


buttonEqual = Button(master, text="=", command=equal, width=10, height=4)
buttonEqual.grid(row=4, column=2 , sticky=W)




if __name__ == "__main__":

    master.update_idletasks()#screen update#
    master.mainloop()#app loop#