import os

command = 'cd "D:\Защита информации\Лаб4. Реализация системы удаленного  выполнения команд с использованием шифрования"' #command to be executed

res = os.system(command)
#the method returns the exit status

print("Returned Value: ", res)
