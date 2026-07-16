try: # we handl;e error coz user will see normal text message rather than coding error
    a = int(input("Enter a number"))
    print(a)

except ValueError as v:
    print("Heyyy")
    print(v)

except Exception as e:
    print(e)
