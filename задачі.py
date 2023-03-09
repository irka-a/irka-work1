#Ірина Кобизєв
print('Задача 1')
a= ('Te amo')
print(a)
b= ('I love you')
a=b
print(a)

print('Задача 2')
Name='Ira'
print('Hello,',Name,'would you like to learn some Python today?')

print('Задача 3')
famous_person='Невідомий автор'
message=' "Можливо ти лише людина,але для когось ти цілий світ." '
print(famous_person +' once said '+ message)

print('Задача 4')
Namee=("  Ira  ")
me=('\n Vika \t Stacy \n Mia \t Kate ')
print(me)
g= Namee.lstrip()
y = Namee.rstrip()
z = Namee.strip()
print("efji", g,"jugvy")
print("rfink", y,"skvme")
print("lfdme", z,"dielf")
print('Задача 5')
print('Кобизєв Ірина \n Укріїна \n 64000 \n Камянка \n Набережна \n 76')
#6 Дізнатися скільки метрів ми трансформуємо в різні види
print('Задача 6')  #+
m = float(input("Введіть цифру щоб ми її трансформували "))
фут = m * 3.280840
дю = m * 39.370
м = m * 0.00062137
яр = m * 1.0936
print('метри ',m ,'\n фунти',фут  ,'\n дюйми',дю,'\nмиля',м,'\nярд',яр)

print('Задача 7')
holidays=int(input('Впишіть цифру, щоб дізнатися знечення після транформування в секунди '))
hh=24*holidays
hm=60*hh
hs=60*hm
print('Години {0:10}, Хвилини {1:10}, Секунди {2:10}' .format(hh, hm, hs))
#11 ввести цифру
H_day= int(input('Впишіть число, щоб дізнатися результат, скільки в літніх канікулах секунд '))
H_mat= H_day*24*60*60
print('секунд канікул {:10}'.format(H_mat))

print('Задача 8')
C = int(input('Впишіть температуру:'))
F = C*32+9/5
K = C+273.15
print('Цельсія{:15,.2f}\t Фаренгейта{:15,.2f} \t Кельвіна{:15,.2f}'.format(C,F,K))

print('Задача 9')
Num =int(input('Ведіть будь яке 4-ох значне число:'))
Тис= Num // 1000
Сот= (Num % 1000) //100
Дес= (Num % 100) //10
Один=Num%10
Sum= Тис+Сот+Дес+Один
print('{}+{}+{}+{}={}'.format(Тис,Сот,Дес,Один,Sum))
#10 вирахувати відстань
print('Задача 10')
import math
x1=39.9075000
y1 = 116.3972300
x2 = 50.4546600
y2 = 30.5238000
Z1= math.radians(x1)
Z2= math.radians(x2)
V1= math.radians(y1)
V2= math.radians(y2)

distance = 6371.032 * math.acos(math.sin(Z1) * math.sin(Z2) + math.cos(Z1) * math.cos(Z2) * math.cos(V1 - V2))
print(f'{distance:.3f}')
