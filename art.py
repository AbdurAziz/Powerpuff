import turtle
import time


ww = turtle.Screen()
ww.title('Raining')
ww.bgcolor('Light Blue')


## register the shapes to use them in python

ww.register("OAcf.gif")
ww.register("8Nwv.gif")


player = turtle.Turtle()
player.shape("square")
player.color("Yellow")




def player_animate():

    if player.shape() == "square":
        player.shape("circle")
    elif player.shape() == "circle":
        player.shape("square")
    
    #set timer
    ww.ontimer(player_animate,500)


while True:
    print("Main Loop")
    player_animate()
    
ww.mainloop()
