from time import sleep   # sleep is using for putting basic delay in our code
from tkinter import *    # tkinter is a library to make and see GUI
from tkinter import messagebox
window = Tk()            # initialising gui named window
from gpiozero import LED # gpiozero used for initialising of led
import RPi.GPIO          #importing Genral input/output pin
led = LED(16)
LIMIT = 12
MORSE_CODE_DICT = {         # morse code dictionary
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
}

def builder():                        # making function that translates alphabates in to morse and join them as word
    print(text1.get())              #it will print the text that should be converted in to morse
    name = (text1.get()).upper()        #it will convert lowercase to uppercase
    arr = list(name)                #it will store all the characters into array/list
    MyWord = ''
    for letter in arr:             #this for-loop will convert letters to morse and join them as word
        if len(name) <=LIMIT and len(name)>0:         # if letter was not space then 
            MyWord = MORSE_CODE_DICT[letter] + ' ' #it will build the morse code
            var = list(MyWord)      
            print(MyWord)         #and print them
            for var1 in var:          # for number or letters in morse code and 
                if(var1 == "-"):    # if sign is '-' then it will blink for 0.3 Second
                    led.on()
                    sleep(0.3)
                    led.off()
                    sleep(0.5)
                elif(var1 == "."):  # if sign is '.' then it will blink for 0.1 Second
                    led.on()
                    sleep(0.1)
                    led.off()
                    sleep(0.5)
                elif(var1 == " "): # if sign is ' ' then it will blink for 0.2 Second
                    led.on()
                    sleep(0.2)
                    led.off()
                    sleep(0.5)
        elif len(name) > LIMIT or len(name) == 0:
            messagebox.showerror("Error", "Name cannot exceed " + str(LIMIT) )
            var.set("")
        elif len(name) == 0:
            messagebox.showerror("Name cannot be null")
            var.set("")
        else:
            MyWord += ' '

    return MyWord     

def close():
    window.destroy()        #if we click on button exit it will destroy the windows-3-

window.geometry("300x175")

label1 = Label(text="Enter Your Name to Blink:")
label1.pack(pady=10)
text1 = Entry()
text1.pack(pady=10)

submit = Button(text="SUBMIT" ,command=builder) 
submit.pack(pady=3)
exit = Button(text="EXIT", command = close)
exit.pack()
window.mainloop()
