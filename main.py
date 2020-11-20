from tkinter import *
import string
import random
import pyperclip

root = Tk()

# =========== Variables ===========
color = '#bfbfbf'
strength = StringVar()
defaultValue = StringVar()
defaultValue.set('8')


# =========== Functions ===========
def generate_password(val):
    generatedPassword.delete(0, END)
    if val == 'week':
        week_letters = string.ascii_letters
        week_letters = ''.join(random.choice(week_letters) for i in range(int(length.get())))
        generatedPassword.insert(0, week_letters)
    elif val == 'good':
        good_letters = ''.join(string.ascii_letters) + ''.join(string.digits)
        good_letters = ''.join(random.choice(good_letters) for i in range(int(length.get())))
        generatedPassword.insert(0, good_letters)
    elif val == 'strong':
        strong_letter = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"""
        strong_letter = ''.join(random.choice(strong_letter) for i in range(int(length.get())))
        generatedPassword.insert(0, strong_letter)


def clearFunc():
    generatedPassword.delete(0, END)


def quiteFunc():
    root.destroy()


# =========== settings ===========
root.title('Password Generator')
root.geometry('400x300')
root.resizable(height=False, width=False)
root.config(bg=color)

# =========== Frame ===========
resultFrame = Frame(root, width=400, height=100, bg=color)
resultFrame.pack()

settingFrame = Frame(root, width=400, height=150, bg=color)
settingFrame.pack()

generateFrame = Frame(root, width=400, height=50, bg=color)
generateFrame.pack()

# =========== generated password ===========
generatedPassword = Entry(resultFrame, font=('Arial', 16), borderwidth=0)
generatedPassword.pack(side=LEFT, pady=10)

copyBtn = Button(resultFrame, text='copy', borderwidth=0, relief=SUNKEN, highlightthickness=0,
                 command=lambda: pyperclip.copy(generatedPassword.get()))
copyBtn.pack(side=LEFT)

# =========== password setting ===========
length = Entry(settingFrame, width=5, font=('Arial', 15), textvariable=defaultValue)
length.pack(side=RIGHT, pady=75)

EmLine = Label(settingFrame, text='', bg=color).pack(pady=10)
Radiobutton(settingFrame, text='Week', variable=strength, value='week', bg=color, highlightbackground=color,
            justify=LEFT).pack(
    padx=(10, 196))
Radiobutton(settingFrame, text='Good', variable=strength, value='good', bg=color, highlightbackground=color,
            justify=LEFT).pack(
    padx=(10, 201))
Radiobutton(settingFrame, text='Strong', variable=strength, value='strong', bg=color, highlightbackground=color,
            justify=LEFT).pack(
    padx=(10, 193))

# =========== Buttons ===========
clearBtn = Button(generateFrame, text='Clear', command=clearFunc)
clearBtn.pack(side=LEFT, pady=5, padx=2)

generateBtn = Button(generateFrame, text='Generate', bg='#e82113', fg='white',
                     command=lambda: generate_password(strength.get()))
generateBtn.pack(side=LEFT, pady=5, padx=2)

quiteBtn = Button(generateFrame, text='Quite', command=quiteFunc)
quiteBtn.pack(side=LEFT, pady=5, padx=2)

root.mainloop()