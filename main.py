import turtle
import time
import random  

WIDTH, HEIGHT = 500, 500    
COLORS = ['red','blue','green','yellow','orange','purple','black','gray','turquoise','skyblue']

def number_of_racers():
    counter = 0
    while counter < 3:
        try:    
            num = int(input("Enter the number of racers in range (2,10): "))
            if 2 <= num <= 10:
                return num
            else:
                counter += 1
                print("Invalid number of racers\nPlease make sure that the number is in range (2,10)")
                print(f"You still have {3-counter} tries left")
        except ValueError:
            counter += 1
            print("Invalid input \nOnly integers are valid")
            print(f"You still have {3-counter} tries left")
    else:
        print("You ran out of tries\nTry again later")
        return None
    

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')
    return screen


def create_turtles(colors):
    turtles = []
    distance = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.penup()           # to not draw any line from moving from the center to the starting position      
        racer.left(90)
        racer.setpos(-WIDTH//2 + (i + 1) * distance, -HEIGHT//2 + 20)
        racer.pendown()         # to draw a line when moving from staring point till the end point
        turtles.append(racer)
    return turtles  


def race(turtles, colors):
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


racers = number_of_racers()
if racers:
    screen = init_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    print(colors)
    turtles = create_turtles(colors)
    winner = race(turtles, colors)
    print(f'The winner is the {winner} turtle!')
    screen.mainloop()
