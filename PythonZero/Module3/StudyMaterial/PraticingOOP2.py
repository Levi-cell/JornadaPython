# declarando uma classe Televisão

class Television:
    def __init__(self):
        self.powerOn = False
        self.channel = 2


# Create an object named "tv" from the Television class

tv = Television()

# Display the value of the "powerOn" attribute of the "tv" object

print(tv.powerOn)

# Display the value of the "channel" attribute of the "tv" object

print(tv.channel)

# The attribute "room" does not exist

print(tv.room)