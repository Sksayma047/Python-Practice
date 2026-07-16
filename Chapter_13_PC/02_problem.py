table = [str(7*i) for i in range(1,11)]

s = "\n".join(table)
print(s)






# filter func

a =[123,234,765,3,55,23,65]

def divisible5(n):
    if(n%5 == 0):
        return True
    return False


f = list(filter(divisible5, a))
print(f)