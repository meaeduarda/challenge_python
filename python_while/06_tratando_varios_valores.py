''''
Creating a program that reads several integers. The program will only stop when the user enters the value 999 stop condition. At the end, it will show how many numbers were entered and the sum between them, disregarding the flag.
'''
number = cont = total_sum = 0
number = int(input('Digite um número [999 para parar]: ')) # I read the number before the while structure because it will consider all values, but when entering the while it will disregard 999

while number != 999: 
    total_sum += number
    cont += 1
    number = int(input('Digite um número [999 para parar]: ')) # I put it at the end after the increments because here it will not consider 999
print ('Você digitou {} números e a soma entre eles foi {}'.format(cont,total_sum))