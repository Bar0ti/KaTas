5# Bunker 1-2 7.38 made by Bar0ti https://youtu.be/lvmWrBAX0TU
# High chance of improving it, I haven't tested out all of the combinations of elevator entry
#also the moment when I throw the bottle isn't optimized, it's very likely delaying the earliest possible
#moment at which I can intereact with the button
#A possible change to the whole strat is to use both bottles to kill both the rickies, this will allow for a longer
#ricky boost, however to achieve this one will have to try fiddling with the position from which they execute the ricky boost.

from katas import Controller, Scripter


script = Scripter()
script.Button(Controller.left_shoulder, duration=0)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(17)
script.Button(Controller.X, duration=1)
script.Wait(4)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(16)
script.Button(Controller.X, duration=1)
script.Wait(5)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(21)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(2)
script.Button(Controller.X, duration=1)
script.Wait(23)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(13)
script.Button(Controller.right, duration=10)
script.Wait(2)
script.MoveLeftStick(25)
script.Button(Controller.X, duration=1)
script.Wait(20)
script.MoveLeftStick(330)
script.Button(Controller.X, duration=1)
script.Wait(3)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(4)
script.MoveLeftStick(180)
script.Button(Controller.B, duration=1)
script.Wait(15)
script.Button(Controller.Y, duration=1)
script.Wait(3)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(5)
script.Button(Controller.X, duration=1)



script.save()
