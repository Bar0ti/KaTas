# Factory-1 12.13 made by Bar0ti https://youtu.be/2jwB2F1O6CM
# Guaranteed to be improved
# Find slash angles when going up the buildings to clip into them
# Find better timings for everything
# End the roll earlier on the floorboard section

from katas import Controller, Scripter
script = Scripter()

script.Button(Controller.down, duration=1)
script.Button(Controller.right, duration=1)
script.Wait(1)
script.Roll()
script.Wait(13)
script.MoveLeftStick(0.8)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(15)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(12)
script.MoveLeftStick(0.8)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(15)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(14)
script.MoveLeftStick(30)
script.Button(Controller.X, duration=0)
script.Wait(12)
script.Button(Controller.down, duration=0)
script.Button(Controller.right, duration=1)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(16)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(11)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(7)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(8)
script.MoveLeftStick(60)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=0)
script.Button(Controller.right, duration=1)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(12)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(8)
script.MoveLeftStick(55)
script.Button(Controller.X, duration=0)
script.Wait(12)
script.Button(Controller.right, duration=10)
script.Wait(6)
script.MoveLeftStick(50)
script.Button(Controller.X, duration=0)
script.Wait(12)
script.Button(Controller.right, duration=8)
script.Wait(5)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(11)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(11)
script.Button(Controller.A, duration=0)
script.Wait(1)
script.Button(Controller.down, duration=18)
script.Button(Controller.right, duration=21)
script.Wait(21)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(8)
script.MoveLeftStick(350)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(11)
script.Button(Controller.right, duration=21)
script.Button(Controller.A, duration=0)
script.Wait(5)
script.Button(Controller.down, duration=10)
script.Wait(14)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(5)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(6)
script.MoveLeftStick(0.8)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(15)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(5)
script.MoveLeftStick(10)
script.Button(Controller.X, duration=0)
script.Wait(1)
script.Button(Controller.Y, duration=0)
script.save()

#slow-mo
#script.Button(Controller.left_thumb, duration=0)

#c-slash timings
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()
#script.Wait(10)
#script.MoveLeftStick(0)
#script.Button(Controller.X, duration=0)
#script.Wait(11)

#scuffed slow-mo c-slashing timings
#script.MoveLeftStick(0.8)
#script.Button(Controller.X, duration=0)
#script.Wait(11)
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()
#script.Wait(10)
#script.Button(Controller.left_thumb, duration=0)
#script.Wait(3)
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()
#script.Wait(10)

#slow-mo roll cancel timings
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()
#script.Wait(11)
#script.Button(Controller.right, duration=6)
#script.Button(Controller.A, duration=0)
#script.Button(Controller.left_thumb, duration=0)
#script.Wait(2)
#script.Button(Controller.down, duration=0)
#script.Wait(2)
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()

#Roll cancel on stairs
#script.Button(Controller.right, duration=7)
#script.Button(Controller.A, duration=0)
#script.Button(Controller.left_thumb, duration=0)
#script.Wait(3)
#script.Button(Controller.down, duration=2)
#script.Wait(1)
#script.Roll()
