# Modeling the Television class in a different way

class Television:
    def __init__(self, isTurnedOn, channel):
        self.isTurnedOn = isTurnedOn
        self.channel = channel

    def turnOn(self):
        print("The TV is turned on")

    def turnOff(self):
        print("The TV is turned off")

    def channelStatus(self, channel):
        print("The channel is", channel)

# Creating instances of the class

tv1 = Television(True, '2')
tv2 = Television(False, '5')

print(tv1.channel)
print("-----")

print(tv1.turnOn())
print("-----")

print(tv1.turnOff())
print("-----")

print(tv1.channelStatus('5'))