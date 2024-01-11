def getValueOfLine(line):
    first   = ""
    last    = ""

    for char in line.strip():
        if char.isdigit():
            if first == "":
                first = char
            last = char
    return int(first + last)

sum = 0

with open("Inputs/01","r") as File:
    for line in File:
        sum += getValueOfLine(line)
print(f"Sum: {sum}")
