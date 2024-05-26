from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time

spam = 4

# Create mouse and keyboard controller objects
mouse = MouseController()
keyboard = KeyboardController()


def menu():
    keyboard.press(Key.alt_l)
    print('Left Alt key pressed')

    mouse.press(Button.right)
    time.sleep(.1)
    mouse.release(Button.right)
    print('Right click')

    mouse.move(75, 0)
    print('Mouse moved by 75 pixels')

    mouse.press(Button.left)
    time.sleep(.1)
    mouse.release(Button.left)    
    print('Left click')
    keyboard.release(Key.alt_l)

def move_mouse(x , y):
    mouse.move(x, y)
    print('Mouse moved by {x} , {y} pixels')

def roll(x, y):
    menu()
    mouse.move(x, y)
    time.sleep(.3)
    mouse.press(Button.left)
    time.sleep(.1)
    mouse.release(Button.left)

def full(x,y,name,roll_time):
    count = 0
    print('Rolling {name}!!')
    roll(x,y)
    time.sleep(roll_time)
    while count < spam:
        roll(x, y)
        time.sleep(.1)
        count += 1

def kiddle_roll(x,y):
    menu()
    mouse.move(x, y)
    time.sleep(.1)
    mouse.scroll(0, -1)
    time.sleep(.3)
    mouse.press(Button.left)
    time.sleep(.1)
    mouse.release(Button.left)

def zkiddles_gum(x,y,name,roll_time):
    count = 0
    print('Rolling {name}!!')
    kiddle_roll(x,y)
    time.sleep(roll_time)
    while count < spam:
        kiddle_roll(x, y)
        time.sleep(.1)
        count += 1
    


def main():
    count_1 = 0
    print("Starting cycle!!")
    time.sleep(5)
    try:
        while count_1 < 10:
            time.sleep(2)
            full(75,150,"AK" ,12)
            #zkiddles_gum(75,490,"Zkittles" ,9)
            count_1 +=1
    except KeyboardInterrupt:
        print('All done!')

if __name__ == "__main__":
    main()

'''
JOINTS:

White: 75,0,'white',2.2
OG: 75,-100,"og" ,5.2
skunk: 75,-200,"skunk" ,5
AK: 75,100,"AK" ,4
Amnesia: 75,200,"AMN" ,3
Purple: 75,300,"purp" ,3
Gelato: 75,400,"Gelato" ,5
Zkittles: 75,490,"Zkittles" ,3.3

BAGS:

White: 75,0,'white',14
OG: 75,-100,"og" ,8
skunk: 75,-200,"skunk" ,11
AK: 75,100,"AK" ,14
Amnesia: 75,200,"AMN" ,8
Purple: 75,300,"purp" ,9
Gelato: 75,400,"Gelato" ,9
Zkittles: 75,490,"Zkittles" ,14

GUMMIES:

White: 75,0,'white',8
OG: 75,-100,"og" ,11
skunk: 75,-200,"skunk" ,13
AK: 75,100,"AK" ,15
Amnesia: 75,200,"AMN" ,9
Purple: 75,300,"purp" ,10
Gelato: 75,400,"Gelato" ,14
Zkittles: 75,490,"Zkittles" ,9

'''