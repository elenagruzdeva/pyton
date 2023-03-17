#Naidite symmy tsifr trexznachnogo chisla.
# 123 -> 6 (1+2+3)

number = int(input('vvedite 3xznachnoe chislo: '))
a = number % 10
number = number // 10
b = number % 10
number = number //10
sum = a+ b+ number
print (sum)
