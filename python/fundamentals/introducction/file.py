num1 = 42 #declaración de variable de tipo entero
num2 = 2.3#declaración de variable de tipo flotante
boolean = True#Declaración d variable de tipo booleana
string = 'Hello World' #declaración de cariable de tipo string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #declaración de un array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#declaración de un diccionario
fruit = ('blueberry', 'strawberry', 'banana')#declaración de una tupla
print(type(fruit))#imprime en la consola el tipo de dato de la variable fruit
print(pizza_toppings[1])#Imprime el elemento en la posición 1 del array pizza_toppings
pizza_toppings.append('Mushrooms')#agrega al array pizza_toppings la cadena 'Mushrooms'
print(person['name'])#busca en el diccionario el elemento asociado al codigo 'name'
person['name'] = 'George'#reasicnamos el valor de elemento 'name'
person['eye_color'] = 'blue'#agregamos el dato eye_color al dicionario person
print(fruit[2])#Imprimimos el elemento en la posición 2 de la tupla fruit

if num1 > 45:#condicional: si num1 es menor que 45 pasa lo siguiente
    print("It's greater")#Imprime en pantalla es mayor
else:#si no 
    print("It's lower")#imprime en pantalla es menor

if len(string) < 5:#si la longitud de la cadena es menor a 5
    print("It's a short word!")#imprime en pantalla: es una palabra corta
elif len(string) > 15:#si no si la longitud de la cadena es mayor a 15
    print("It's a long word!")#imprime en pantalla: es una palabra larga
else:#si no
    print("Just right!")#Imprime en pantalla: justo asi

for x in range(5):#el bucle se repetira 5 veces
    print(x)
for x in range(2,5):#el bucle se repetira mientras x<5 con x = 2 en el inicio
    print(x)
for x in range(2,10,3):#el bucle se repetira mientras x<10 con x = 2 en el inicio y el valor aumentara de 3 en 3
    print(x)
x = 0 #declaramos una variable de tipo entero con valor = 0
while(x < 5):#mientras x sea menor a 5 se repetira el bucle
    print(x)
    x += 1#x=x+1

pizza_toppings.pop()#del Array pizza_toppings eleminaremos el elemento del final del Array
pizza_toppings.pop(1)#del Array pizza_toppings eleminaremos el elemento con index 1

print(person)#Imprime el diccionario person
person.pop('eye_color')#elimina el elemento eye_color del diccionario
print(person)#Imprime el diccionario person

for topping in pizza_toppings:#El bucle se repetira por todos los elementos del array
    if topping == 'Pepperoni':#si topping es igual a pepperoni
        continue#el bucle continuara en su siguiente elemento
    print('After 1st if statement')
    if topping == 'Olives':#si topping es igual a Olives
        break#el bucle se rompe

def print_hello_ten_times():#definimos una función
    for num in range(10):
        print('Hello')

print_hello_ten_times()#llamamos a la función

def print_hello_x_times(x):#definimos una función que resivira como parametro una variable x
    for num in range(x):
        print('Hello')

print_hello_x_times(4)#llamamos a la función 4 como argumento

def print_hello_x_or_ten_times(x = 10):#definimos una función que resivira como parametro una variable x=10 en caso de que no reciva argumento
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()#llamamos a la función sin argumento
print_hello_x_or_ten_times(4)#llamamos a la función con un argumento


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)