#a)
def doTwice(f):
    f()
    f()

def printSpam():
    print('spam')

doTwice(printSpam)

#b)
def doTwiceAltered(f, x):
    f(x)
    f(x)

def printSpam1(x):
    print(x)

doTwiceAltered(printSpam1, 'text1')
doTwiceAltered(printSpam1, 'text1')




