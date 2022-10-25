file = open("./VScode snippet maker/code.txt", "r")

for line in file:
    # clear the last \n(end of line)
    line = str(line).replace("\n", "")
    # make " into \"
    line = line.replace("\"", "\\\"")
    print("\"" + line + "\",")
