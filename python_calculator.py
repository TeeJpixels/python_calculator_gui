from tkinter import *
import platform


def evaluate():
    try:
        result = str(eval(equation_label.get()))
        equation_label.set(result)
    except ZeroDivisionError:
        equation_label.set("Cannot divide by zero")
    except SyntaxError:
        equation_label.set("Syntax Error")
    except Exception:
        equation_label.set("Error")


window = Tk()
window.title("100% Accurate Calculator")

label = Label(window, text="100% Accurate Calculator", bg="black", fg="white", font=("Arial", 18), width=30, height=2)
label.pack()


equation_label = StringVar()
label2 = Label(window, textvariable=equation_label, font=("Arial", 18), width=30, height=2, bg="lightgrey", fg="black")
label2.pack()

frame=Frame(window)
frame.pack()

button1 = Button(frame, text="1", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "1"))
button1.grid(row=0, column=0)

button2 = Button(frame, text="2", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "2"))
button2.grid(row=0, column=1)

button3 = Button(frame, text="3", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "3"))
button3.grid(row=0, column=2)

button4 = Button(frame, text="4", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "4"))
button4.grid(row=1, column=0)

button5 = Button(frame, text="5", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "5"))
button5.grid(row=1, column=1)

button6 = Button(frame, text="6", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "6"))
button6.grid(row=1, column=2)

button7 = Button(frame, text="7", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "7"))
button7.grid(row=2, column=0)

button8 = Button(frame, text="8", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "8"))
button8.grid(row=2, column=1)

button9 = Button(frame, text="9", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "9"))
button9.grid(row=2, column=2)

button0 = Button(frame, text="0", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "0"))
button0.grid(row=3, column=0)

plus_button = Button(frame, text="+", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "+"))
plus_button.grid(row=0, column=3)

minus_button = Button(frame, text="-", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "-"))
minus_button.grid(row=1, column=3)

multiply_button = Button(frame, text="*", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "*"))
multiply_button.grid(row=2, column=3)

divide_button = Button(frame, text="/", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "/"))
divide_button.grid(row=3, column=3)

equals_button = Button(frame, text="=", width=10, height=4, command=evaluate)
equals_button.grid(row=3, column=2)

decimal_button = Button(frame, text=".", width=10, height=4, command=lambda: equation_label.set(equation_label.get() + "."))
decimal_button.grid(row=3, column=1)

clear_button = Button(frame, text="Clear", width=20, height=4, command=lambda: equation_label.set(""))
clear_button.grid(row=4, column=0, columnspan=2)

backspace_button = Button(frame, text="←", width=20, height=4, command=lambda: equation_label.set(equation_label.get()[:-1]))
backspace_button.grid(row=4, column=2, columnspan=2)


'''if platform.system() == "Windows":
    window.state('zoomed')  # Windows only
else:
    window.attributes('-zoomed', True)  # macOS/Linux alternative'''

window.mainloop()