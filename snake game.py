# you can play this game using [W][A][S][D] keys


from tkinter import *
import random

# We divide the screen into pixels using the PIXEL_SIZE we define 
# so it will be easier to handle .
# also we define our default values here so
# we can change the appearance of our game with just editing few lines of code .

GameWidth = 800
GameHeight = 800
SPEED = 100
PIXEL_SIZE = 40
BODY_LENGTH = 3
SNAKE_COLOR = "#00e600"
FOOD_COLOR = "#e60000"


window = Tk()
window.title("Snake Game")
window.resizable(False, False)
window.configure(background="#2b2b2b")


# This class will create a snake object that will appear at Top-Left of the screen
class SNAKE :
    def __init__(self):
        self.BodySize = BODY_LENGTH
        self.location = []                              
        self.squares = []

        for bodypart in range(0, BODY_LENGTH):          
            self.location.append([0, 0])

        for x, y in self.location:                       
            parts = CANVAS.create_rectangle(x, y, x+PIXEL_SIZE, y+PIXEL_SIZE, fill=SNAKE_COLOR)
            self.squares.append(parts)


# this class will create a food object at random location in the screen
class FOOD:

    def __init__(self):
        x = random.randint(0, int(GameWidth / PIXEL_SIZE) - 1) * PIXEL_SIZE
        y = random.randint(0, int(GameHeight / PIXEL_SIZE) - 1) * PIXEL_SIZE

        self.food_location = [x, y]
        self.food_obj = CANVAS.create_oval(x, y, x+PIXEL_SIZE, y+PIXEL_SIZE, fill=FOOD_COLOR)



def GameProcces (snake , food):

    # This part specifies the location of the snake's head
    x , y = snake.location[0]
    if DIRECTION == "left" :
        x = x - PIXEL_SIZE
    elif DIRECTION == "right" :
        x = x + PIXEL_SIZE
    elif DIRECTION == "up" :
        y = y - PIXEL_SIZE
    elif DIRECTION == "down" :
        y = y + PIXEL_SIZE

    snake.location.insert(0, [x, y])

    square = CANVAS.create_rectangle(x, y, x+PIXEL_SIZE, y+PIXEL_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

 
    # if snake pass the walls on each side it will appear on the other side
    x , y = snake.location[0]
    if x >= GameWidth :
        x , y = 0-PIXEL_SIZE , y
        snake.location.insert(0, [x, y])
    elif x < 0 :
        x , y = GameWidth,y
        snake.location.insert(0, [x, y])
    elif y >= GameHeight :
        x , y = x , 0-PIXEL_SIZE
        snake.location.insert(0, [x, y])
    elif y < 0 :
        x , y = x , GameHeight
        snake.location.insert(0, [x, y])


    # if snake eats the food it will apear at a new random location
    # and you will get "1" score
    if x == food.food_location[0] and y == food.food_location[1] :
        global SCORE
        SCORE += 1
        score_label.config(text=("SCORE = {}".format(SCORE)))
        CANVAS.delete(food.food_obj)
        food = FOOD()
    else :
        del snake.location[-1]
        CANVAS.delete(snake.squares[-1])
        del snake.squares[-1]


    # in case snake's head location = one of snake body part's location you will "Lose"
    if conditions():
        GameOver()
    else:
        window.after(SPEED, GameProcces, snake , food)


def conditions():
    x, y = snake.location[0]
    for i in snake.location[1::]:
        if x == i[0] and y == i[1] :
            return TRUE
    else :
        return FALSE


def GameOver():
    CANVAS.delete("all")
    CANVAS.create_text(GameWidth/2, GameHeight/2, text="< Game Over Bro />", fill=FOOD_COLOR, font="Arial 60 bold")

def change_direction(new_direction):
    global DIRECTION
    if new_direction == "left":
        if DIRECTION != "right":
            DIRECTION = new_direction
    elif new_direction == "right":
        if DIRECTION != "left":
            DIRECTION = new_direction
    elif new_direction == "up":
        if DIRECTION != "down":
            DIRECTION = new_direction
    elif new_direction == "down":
        if DIRECTION != "up":
            DIRECTION = new_direction


#===============================================================


SCORE = 0
DIRECTION = "right"

score_label = Label(window, text="SCORE = {}".format(SCORE), bg="#2b2b2b", fg="white", font=('consolas', 40))
score_label.pack()

CANVAS = Canvas(window, width=GameWidth, height=GameHeight, bg="#000000"
              , highlightthickness=0, highlightbackground="#2b2b2b")
CANVAS.pack()

food = FOOD()
snake = SNAKE()

GameProcces(snake , food)

window.bind("<w>", lambda event : change_direction("up"))
window.bind("<s>", lambda event : change_direction("down"))
window.bind("<a>", lambda event : change_direction("left"))
window.bind("<d>", lambda event : change_direction("right"))

window.mainloop()
