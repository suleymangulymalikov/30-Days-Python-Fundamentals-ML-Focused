input = "   hELLo     WoRLD   !!!   this   is    a tESt. btw, u are great   "
print(input)

words = input.strip().lower().capitalize().replace("btw", "By the way").replace("u", "you").split()
output = ""
for word in words:
    if word == "!!!":
        output += word
    elif word == "this":
        output += " " + word.capitalize()
    else:
        output += " " + word


print(output)

