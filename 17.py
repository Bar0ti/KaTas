# Hotel-4 5.27 made by Bar0ti https://youtu.be/uRzXO7cYgKQ
# Very likely to be improved
# Hard maybe on finding an earlier way to slash the two enemies
# There's guaranteed to be a spot further left from which you can throw
# Find a better way to slash the left ricky

from katas import Controller, Scripter
script = Scripter()

script.Button(Controller.left_shoulder, 0)
script.Wait(77)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(8)
script.Button(Controller.right, duration=7)
script.Button(Controller.A, duration=0)
script.Button(Controller.left_thumb, duration=0)
script.Wait(3)
script.Button(Controller.down, duration=2)
script.Wait(1)
script.Roll()
script.Wait(7)
script.MoveLeftStick(35)
script.Button(Controller.X, duration=0)
script.Wait(4)
script.Button(Controller.down, duration=2)
script.Wait(2)
script.Roll()
script.Wait(8)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(17)
script.Button(Controller.A, duration=24)
script.Wait(7)
script.MoveLeftStick(90)
script.Button(Controller.X, duration=0)
script.Wait(7)
script.MoveLeftStick(342.8)
script.Button(Controller.B, duration=0)
script.Wait(1)
script.Button(Controller.left, duration=16)
script.Wait(4)
script.Button(Controller.down, duration=7)
script.Wait(9)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(179.2)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(6)
script.Button(Controller.left_thumb, duration=0)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(18)
script.MoveLeftStick(180)
script.Button(Controller.X, duration=0)
script.Wait(5)
script.Button(Controller.down, duration=1)
script.Button(Controller.right, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(0.8)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(5)
script.Button(Controller.left_thumb, duration=0)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(9)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(3)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(6)
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
#script.Button(Controller.down, duration=1)
#script.Wait(3)
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