print(f"Is 22 greater than 8? {22 > 8}")
print(f"Is 7 less than 4? {7 < 4}")
print(f"Does 2 equal 1? {2 == 1}")
print(f"Does 1 equal 1? {1 == 1} ")

#numeric values
print("One is equal to 2:",int(1==2))
print("One is equal to 1:",int(1==1))

myname = "Fred"
myage = 22
print(f"a: {43} ")
print(f"b: {'Sup'} ")
print(f"c: {False} ")
print(f"d: {myname} ")
print(f"e: {myage} ")

print((1-4+2),(4-2+8))
print((1*4+2),(4*2+8))

print(f"is 'Fred'=='Fredo'? {'Fred'=='Fredo'}")

print("Comparison:","aa" < "b")
print("Comparison:", 5 < 6) 

a = 4
b = 6
print(f"Comparison: {a} is greater than {b}" if a > b else "")
print(f"Comparison: {a} is less than {b}" if a < b else "")
print(f"Comparison: {a} is greater than or equal to {b}" if a >= b else "")
print(f"Comparison: {a} is less than {b}" if a <= b else "")


bank_balance = 50

if bank_balance < 100:
  money = 1000
  bank_balance += money 
else:
  print("You don't have enough money")

bank_balance = 700 
savings = 200
if bank_balance < 200:
  money = 1050
  bank_balance += money 
elif bank_balance > 200:
  savings += 200
  bank_balance -= 200
else:
  savings += 50
  bank_balance -= 50

fuel = 1
print("Fill tank now" if fuel <= 1 else "there's enough fuel")

fuel = 10
while fuel > 1:
  print("there's enough fuel")
  fuel -= 1

books = ['Diary of a wimpy kid','Enders Game','Duncan']
for book in books:
  print(f"book: {book}")
for i in range(5):
  print(f'i: {i}')


for count in range(13):
  print(f"{count} times 12 is {count * 14}")
  if count == 7:
        break
  
for count in range(13):
  if count == 7:
    continue 
    print(f"{count} times 12 is {count * 14}")