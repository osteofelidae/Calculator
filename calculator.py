upTo = int(input("Input upper limit... "))
fileName = input("Input file name... ")
file = open(fileName + ".py", "w")

file.write("operation = input('Input operation... ')\n\n")

for a in range(upTo):
    for b in range(upTo):
        file.write("if operation == '" + str(a) + "+" + str(b) + "': \n")
        file.write("\tprint('Answer is ' + str(" + str(a+b) + ")) \n\n")
        file.write("if operation == '" + str(a) + "-" + str(b) + "': \n")
        file.write("\tprint('Answer is ' + str(" + str(a-b) + ")) \n\n")
        file.write("if operation == '" + str(a) + "*" + str(b) + "': \n")
        file.write("\tprint('Answer is ' + str(" + str(a*b) + ")) \n\n")
        if b != 0:
            file.write("if operation == '" + str(a) + "/" + str(b) + "': \n")
            file.write("\tprint('Answer is ' + str(" + str(a/b) + ")) \n\n")
        
file.close()