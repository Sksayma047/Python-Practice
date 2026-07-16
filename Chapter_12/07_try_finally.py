def main():  # finally erroe ane k bad bhi function me chalega  aur error na yaa to bhi chlega
    try: # we handl;e error coz user will see normal text message rather than coding error
        a = int(input("Enter a number: "))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("Hey i am finally")


main()
