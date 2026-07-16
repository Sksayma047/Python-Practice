try: # we handl;e error coz user will see normal text message rather than coding error
    a = int(input("Enter a number"))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")



