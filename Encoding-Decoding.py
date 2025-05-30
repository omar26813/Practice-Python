code = {
    11: "m", 12: "t", 13: "f", 14: "e", 15: "n", 16: "u", 17: "i", 18: "w",
    19: "g", 20: "x", 21: "o", 22: "k", 23: "h", 24: "q", 25: "p", 26: "l",
    27: "j", 28: "s", 29: "v", 30: "y", 31: "d", 32: "b", 33: "a", 34: "c",
    35: "r", 36: "z", 37: " ", 38: ",", 39: ".", 40: "-", 41: "?", 42: "!",
    43: "*", 44: '"', 45: "$", 46: "'", 47: "(", 48: ")"
}

input1 = input("Type to Encode or Decode:\n")  # Input string example

output = ""
output2 = ""

# Iterate over the input string in pairs
if input1.isdecimal() and len(input1) % 2 == 0:
    for i in range(0, len(input1), 2):
        key = int(input1[i:i+2])
        if key in code:
            output += code[key]
elif input1.isdecimal() and len(input1) % 2 == 1:
    print("The code length must be even! Check it again")
else:
    for char in input1:
        if char.isupper():
            output2 += char.lower()
        else:
            output2 += char
    for char in output2:
        for key, value in code.items():
            if char == value:
                output += str(key)

print(output)