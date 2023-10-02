"""Utilizando um Pool de tarefas para serem processadas
Utilize o python online compiler:
https://www.programiz.com/python-programming/online-compiler/
"""

from multiprocessing import Pool
from time import sleep

if __name__ == '__main__':
    def work_log(each):
        print(f"Process {each[0]} waiting {each[1]} seconds")
        sleep(int(each[1]))
        print(f"Process {each[0]} Finished.")


    pool = Pool()
    pool.map(work_log, (["A", 5], ["B", 2], ["C", 1], ["D", 3]))
    pass




