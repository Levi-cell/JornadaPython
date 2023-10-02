class TV:
    def __init__(self, channelNumber):
        self.channelNumber = channelNumber
        self.volume = 30

    def changeChannel(self):
        self.channelNumber = int(input("Enter the new channel number: "))
        print("The new channel is", self.channelNumber)

    def increaseVolume(self):
        if self.volume <= 99:
            self.volume += 1
            print("The volume is now", self.volume)
        else:
            print("Volume cannot be increased beyond 100")

    def decreaseVolume(self):
        if self.volume >= 1:
            self.volume -= 1
            print("The volume is now", self.volume)
        else:
            print("Volume cannot be decreased below 0")

    def showData(self):
        print("Your channel number is:", self.channelNumber)
        if 1 <= self.volume <= 99:
            print("The volume is:", self.volume)
        else:
            print("Volume cannot be set to this value")


channelNumber = int(input("Enter your channel number: "))

tv1 = TV(channelNumber)
tv1.showData()
unitCount = int(input("How many units do you want to increase the volume by?"))

position = 0

while position < unitCount:
    tv1.increaseVolume()
    position += 1
tv1.showData()