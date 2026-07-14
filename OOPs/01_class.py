class employee: #ye class hai jaise koi khali form jisme sirf placeholders rahete 
    language = "py" #this is a class attribute
    salary = 1200000




harry = employee() # ye instance hai jaise kisine wo form fill kara jaise harry to wo object ban gaya
harry.name = "harry"  #this is a object attribute
print(harry.name, harry.language, harry.salary)

sara = employee()
sara.name = "sara"
print(sara.name, sara.language, sara.salary)

