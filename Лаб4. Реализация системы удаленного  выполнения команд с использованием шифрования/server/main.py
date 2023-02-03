from RAT import data_reader

A = data_reader()
with open('pids.txt', 'w') as file:
    file.write(A.procces_list())
