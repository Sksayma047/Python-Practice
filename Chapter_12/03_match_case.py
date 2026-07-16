def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _ :
            return "Unknown status"


n = int(input("Enter status: "))
print(http_status(n))




# for merging

dict1 = {'a' : 1, 'b' : 2}
dict2 = {'c' : 3, 'd' : 4}
merged = dict1 | dict2
print(merged)