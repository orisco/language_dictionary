from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
BLACK = "black"
WHITE = "white"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}
# ---------------------------- GET A RANDOM WORD ------------------------------- #


def next_card():
    global current_card
    canvas.itemconfig(card_image, image=front_image)
    current_card = random.choice(to_learn)
    french_word = current_card['French']
    canvas.itemconfig(language, text="French", fill=BLACK)
    canvas.itemconfig(word, text=french_word, fill=BLACK)
    window.after(3000, flip_card)


# ---------------------------- FLIP CARD ------------------------------- #

def flip_card():
    canvas.itemconfig(card_image, image=back_image)
    english_word = current_card['English']
    canvas.itemconfig(language, text="English", fill=WHITE)
    canvas.itemconfig(word, text=english_word, fill=WHITE)


def remove_card():
    to_learn.remove(current_card)
    new_list = pandas.DataFrame(to_learn)
    new_list.to_csv("data/words_to_learn.csv")
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 270, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text="French", fill=BLACK, font=LANGUAGE_FONT)
word = canvas.create_text(400, 263, text="trouve", font=WORD_FONT, fill=BLACK)

right_button = PhotoImage(file="images/right.png")
button = Button(image=right_button, highlightthickness=0, command=next_card)
button.grid(column=0, row=1)

wrong_button = PhotoImage(file="images/wrong.png")
button = Button(image=wrong_button, highlightthickness=0, command=remove_card)
button.grid(column=1, row=1)


next_card()

window.mainloop()