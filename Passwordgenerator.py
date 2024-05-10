import random
print("_________________________________\n| WELCOME TO PASSWORD GENERATOR |\n*********************************\n")

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z','A' , 'B' , 'C' ,'D' ,'E' ,'F' ,
        'G' ,'H' ,'I' ,'J' ,'K' ,'L' ,'M' ,'N','O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,
        'U' ,'V' ,'W' ,'X' ,'Y' ,'Z']

symbols=['~','!','@','#','$','%','^','&','*','(',')','_','+','=','|',':',';','<'
        ,'>','?','/']

numbers=['0','1','2','3','4','5','6','7','8','9']
password_l=[]
letters_in=int(input("How many letters would you like in your Password?\n:- "))
symbols_in=int(input("How many symbols would you like in your Password?\n:- "))
numbers_in=int(input("How many numbers would you like in your Password?\n:- "))

for i in range(1,letters_in+1):
    latt=random.choice(letters)
    password_l+=latt
    
for i in range(1,symbols_in+1):
    sym=random.choice(symbols)
    password_l+=sym

for i in range(1,numbers_in+1):
    num=random.choice(numbers)
    password_l+=num


random.shuffle(password_l)

password= ""

for i in password_l:
    password+=i
    
print(f"Your generated password.\n:- {password} ")





