# Studio-1 9.67 made by Bar0ti https://youtu.be/ZKOv8Fy6J6c
# Most likely can be done faster
# Check ricky boosts at different slash angles

from katas import Controller, Scripter
script = Scripter()

script.Button(Controller.left_shoulder, 0)
script.Wait(431)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(7)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(12)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(17)
script.MoveLeftStick(25.118)
script.Button(Controller.X, duration=0)
script.Wait(1)
script.MoveLeftStick(20)
script.Button(Controller.B, duration=0)
script.Button(Controller.right, duration=40)
script.Wait(4)
script.MoveLeftStick(15)
script.Button(Controller.B, duration=0)
script.Wait(19)
script.MoveLeftStick(329.99, duration=30)
script.Wait(26)
script.Roll()
script.Wait(10)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()

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


