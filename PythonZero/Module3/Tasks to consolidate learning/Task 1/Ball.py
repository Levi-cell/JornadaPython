class Ball:
    def __init__(self, color, circumference, material):
        self.color = color
        self.circumference = circumference
        self.material = material

    def changeColor(self):
        newColor = input('Enter the new color:')
        self.color = newColor

    def showColor(self):
        print('Your new color is:', self.color)


# Testing
ball = Ball('orange', '29.5', 'tactel')

print(ball.color)

ball.color = 'red'

print(ball.color)

# Using methods
ball.changeColor()
ball.showColor()