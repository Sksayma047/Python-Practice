with open("log.txt", "r") as f:
    lines = f.read()

lineno = 1
for line in lines:
    if("python" in lines):
        print("yes python is present")
        break
    lineno += 1
else:
        print("No python is not present")


