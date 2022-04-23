#!/bin/python3
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import os
import random


keyWindow = Tk()
keyWindow.title("Ceaser++ Encryption")
keyWindow.geometry("370x180")
keyWindow.config(background="#009900")

key = ""

def save_file():

    global keyWindow
    global key
    key = asksaveasfile(initialfile = 'Untitled.key',
defaultextension=".key",filetypes=[("Text Documents","*.key")])
    #f = open(key)
    key.write(str(random.randint(100000000000000000000, 10000000000000000000000000000)))
    #f.close()
    key = key.name
    label_file_explorer.configure(text="File Opened: "+key)
    keyWindow.destroy()
    print("File created")


def browseFiles():

    global key
    filename = filedialog.askopenfilename(initialdir = ".",
                                          title = "Select a File",
                                          filetypes = (("Key files",
                                                        "*.key*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    try:
        label_file_explorer.configure(text="File Opened: "+filename)
        keyWindow.destroy()
    except:
        pass
    key = filename
    print(key)
    
    return filename
    

label_file_explorer = Label(keyWindow,
                            text = "Load Key File",
                            width = 100, height = 4,
                            fg = "blue")
button_explore = Button(keyWindow,
                        text = "Browse Files",
                        command = browseFiles)
button_exit = Button(keyWindow,
                     text = "Create Key",
                     command = lambda: save_file())

label_file_explorer.config(fg="#FFFFFF", background="#009900")
button_explore.config(fg="#FFFFFF", background="#005500")
button_exit.config(fg="#FFFFFF", background="#005500")

label_file_explorer.pack()
  
button_explore.pack()
  
button_exit.pack()

keyWindow.mainloop()
print(key)

def get_key(val):
    for key, value in encryptDict.items():
         if val == value:
             return key
 
    return "key doesn't exist"
    
def load_key(key):
  keyfile = open(key)
  key = keyfile.read()
  key = key.splitlines()[0]
  keyfile.close()
  return key

def encrypt(plainText, keylist):
    
    #plainText = plainText.upper()
    

    cryptText = ""
    
    keyIter = 0
    for character in plainText:
        while keyIter > len(keylist) - 1:
            keyIter -= len(keylist)
#            print(keyIter)
        print(character)
        print(get_key(character))
        print(keylist[keyIter])
        try:
            thing = get_key(character) + keylist[keyIter]
        except:
            errorWindow("A character you typed is not supported. For now, this program only supports characters in the US keyboard")
        if thing > dictlength:
            thing -= dictlength
        #print(thing)
        cryptText += encryptDict[thing]
        #print(encryptDict[thing])
        keyIter += 1

    return cryptText

def decrypt(plainText, keylist):

    decryptText = ""
    #plaintext = plainText.upper()

    keyIter = 0
    for character in plainText:
        while keyIter > len(keylist) - 1:
            keyIter -= len(keylist)
#            print(keyIter)
        print(character)
        print(get_key(character))
        print(keylist[keyIter])
        thing = get_key(character) - keylist[keyIter]
        if thing < 1:
            thing += dictlength
            print("OverStepped The Line with", thing, dictlength)
        #print(thing)
        decryptText += encryptDict[thing]
        #print(encryptDict[thing])
        keyIter += 1

    #decryptText = decryptText.lower()
    return decryptText

def encryptOrDecrypt(plainText, keylist, decryptOrEncrypt):

    global topLabel

    global output_text_box

    topLabel.config(text="Processing...")

    plainTextIntoLines = plainText.splitlines()
    print(plainTextIntoLines)
    fullBoii = ""

    #output_text_box.config(state='normal')
    for n in plainTextIntoLines:
        if decryptOrEncrypt == "encrypt":
            output_text_box.delete("1.0","end")
            #output_text_box.insert('end', encrypt(n, keylist))
            fullBoii += encrypt(n, keylist)
            print("encrypted")
        elif decryptOrEncrypt == "decrypt":
            output_text_box.delete("1.0","end")
            #output_text_box.insert('end', decrypt(n, keylist))
            fullBoii += decrypt(n, keylist)
        fullBoii += "\n"
    output_text_box.insert('end', fullBoii)
    #output_text_box.config(state='disabled')
    topLabel.config(text="Encrypt Or Decrypt a message")

def SwitchToEncrypted():
    global decryptOrEncrypt

    decryptOrEncrypt = "encrypt"
    print("So we encrypted")

def SwitchToDecrypted():
    global decryptOrEncrypt

    decryptOrEncrypt = "decrypt"
    print("So we decrypted")

def errorWindow(text):
    windowForError = Tk()
    windowForError.title("Error Window")
    labelForError = Label(master=windowForError, text=text)
    buttonForerror = Button(master=windowForError, text="Ok", command=windowForError.destroy)

    labelForError.pack()
    buttonForerror.pack()

    print("An error was thrown")

    windowForError.mainloop()


decryptOrEncrypt = ""

keyloaded = False




keylist = []

while keyloaded != True:
    try:
        if key == ():
            print("Key")
            quit()
        if key == "()":
            quit()
        if key == "":
            quit()
        key = load_key(key)
        keyloaded = True
        for digit in key:
            keylist.append(int(digit))
        print("not so accepted")
        print()
    except:

        if key == ():
            quit()
            break
        if key == "":
            quit()
            break

        keyloaded = False
        errorWindow("The key contains a non-numerical character (eg. letters, symbols, emojis, etc.)")
        browseFiles()
        print("excepted")
print(keylist)

encryptDict = {
  1: "A",
  2: "B",
  3: "C",
  4: "D",
  5: "E",
  6: "F",
  7: "G",
  8: "H",
  9: "I",
  10: "J",
  11: "K",
  12: "L",
  13: "M",
  14: "N",
  15: "O",
  16: "P",
  17: "Q",
  18: "R",
  19: "S",
  20: "T",
  21: "U",
  22: "V",
  23: "W",
  24: "X",
  25: "Y",
  26: "Z",
  27: " ",
  28: "`",
  29: "~",
  30: "!",
  31: "@",
  32: "#",
  33: "$",
  34: "%",
  35: "^",
  36: "&",
  37: "*",
  38: "(",
  39: ")",
  40: "-",
  41: "_",
  42: "=",
  43: "+",
  44: "[",
  45: "]",
  46: "\\",
  47: "{",
  48: "}",
  49: "|",
  50: ";",
  51: "'",
  52: ":",
  53: "\"",
  54: ",",
  55: ".",
  56: "/",
  57: "<",
  58: ">",
  59: "?",
  60: "a",
  61: "b",
  62: "c",
  63: "d",
  64: "e",
  65: "f",
  66: "g",
  67: "h",
  68: "i",
  69: "j",
  70: "k",
  71: "l",
  72: "m",
  73: "n",
  74: "o",
  75: "p",
  76: "q",
  77: "r",
  78: "s",
  79: "t",
  80: "u",
  81: "v",
  82: "w",
  83: "x",
  84: "y",
  85: "z",
  86: "0",
  87: "1",
  88: "2",
  89: "3",
  90: "4",
  91: "5",
  92: "6",
  93: "7",
  94: "8",
  95: "9",

}
dictlength = 95



#if decryptOrEncrypt == "encrypt":
#    plainText = input("Enter your message: ")
#    plainText = plainText.upper()
#    print(encrypt(plainText, keylist))
    
#if decryptOrEncrypt == "decrypt":
#    plainText = input("Enter your message: ")
#    plainText = plainText.upper()
#    print(decrypt(plainText, keylist))



window = Tk()
window.title("Ceaser++ Encryption")
window.geometry("560x330")
window.config(bg="#009900")

topFrame = Frame(window, bg="#009900")

LeftTexBoxFrame = Frame(window, bg="#009900")
RightTextBoxFrame = Frame(window, bg="#009900")

BottomFrame = Frame(window, bg="#009900")

topLabel = Label(window, text="Encrypt Or Decrypt a message", width=100, height=2, font=("Arial", 25), bg="#009900")

encryptRadio = Radiobutton(topFrame, text="Encrypt", variable=decryptOrEncrypt, value="encrypt", command=SwitchToEncrypted, bg="#009900", borderwidth=0, highlightbackground="#009900", selectcolor="#009900")
decryptRadio = Radiobutton(topFrame, text="Decrypt", variable=decryptOrEncrypt, value="decrypt", command=SwitchToDecrypted, bg="#009900", borderwidth=0, highlightbackground="#009900")

input_text_box = Text(LeftTexBoxFrame, height=10, width=30, bg="#005500", fg="#FFFFFF", borderwidth=0)
output_text_box = Text(RightTextBoxFrame, height=10, width=30, bg="#005500", fg="#FFFFFF", borderwidth=0)

input_label = Label(LeftTexBoxFrame, text="Input: ", bg="#009900", fg="#FFFFFF")
output_label = Label(RightTextBoxFrame, text="Output: ", bg="#009900", fg="#FFFFFF")


#output_text_box.config(state='disabled')

actionButton = Button(BottomFrame, text="Process", command=lambda: encryptOrDecrypt(input_text_box.get(1.0, "end-1c"), keylist, decryptOrEncrypt), bg="#005500", fg="#FFFFFF", borderwidth=0)


topLabel.pack()

topFrame.pack()

encryptRadio.pack(side=LEFT)
decryptRadio.pack(side=LEFT)

LeftTexBoxFrame.pack(side=LEFT)
RightTextBoxFrame.pack(side=LEFT)

input_label.pack()
input_text_box.pack()

output_label.pack()
output_text_box.pack()

BottomFrame.pack(side=LEFT)
actionButton.pack(side=BOTTOM)

window.mainloop()
