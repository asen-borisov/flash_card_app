from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# -----Flash Cards------

try:
    data = pandas.read_csv("data/words ot learn.csv")

except:
    orig_data = pandas.read_csv("data/french_words.csv")
    to_learn = orig_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill= "black")
    canvas.itemconfig(card_bg, image=front_img)
    flip_time = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words ot learn.csv", index=False)


    next_card()




# -------- UI --------:

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash card app")

flip_time = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front_img)

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 35, "italic"))
card_text = canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))

yes_img = PhotoImage(file="./images/right.png")
yes = Button(image=yes_img, highlightthickness=0, command=is_known)
yes.grid(column=1, row=1)

no_img = PhotoImage(file="images/wrong.png")
no = Button(image=no_img, highlightthickness=0, command=next_card)
no.grid(column=0, row=1)

next_card()
window.mainloop()
