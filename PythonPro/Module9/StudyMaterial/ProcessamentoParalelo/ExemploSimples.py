from multiprocessing import Process

if __name__ == '__main__':
    def test(ordem):
        print(ordem)


    for i in range(5):
        p = Process(target=test(i,))
        p.start()
