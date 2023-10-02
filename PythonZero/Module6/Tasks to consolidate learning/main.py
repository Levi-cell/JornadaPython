inputFile = open('Input IPs', 'w+')

inputFile.write("200.135.80.9" + "\n")
inputFile.write("192.168.1.1" + "\n")
inputFile.write("8.35.67.74" + "\n")
inputFile.write("257.32.4.5" + "\n")
inputFile.write("85.345.1.2" + "\n")
inputFile.write("1.2.3.4" + "\n")
inputFile.write("9.8.234.5" + "\n")
inputFile.write("192.168.0.256" + "\n")

inputFile.close()

inputFile = open('Input IPs', 'r')
print("Input IPs contents:", "\n", inputFile.read())

inputFile = open('Input IPs', 'r')
inputContent = inputFile.read()
inputFile.close()

# Output file

outputFile = open('Output IPs', 'w+')

lines = inputContent.strip().split("\n")

outputFile.write("Valid addresses" + "\n")

for i, line in enumerate(lines):
    if i == 0 or i == 1 or i == 2 or i == 5:
        outputFile.write(line + "\n")

outputFile.write("Invalid addresses" + "\n")
for i, line in enumerate(lines):
    if (i != 0) and (i != 1) and (i != 2) and (i != 5):
        outputFile.write(line + "\n")

outputFile = open('Output IPs', 'r')

print(outputFile.read())