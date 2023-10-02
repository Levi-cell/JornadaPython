# aqui usamos o argumento de args depois
import threading

def process(name, age):
    print(f"Processing {name}, age {age}")

# Criando objetos de thread com diferentes argumentos usando o parâmetro args
t1 = threading.Thread(target=process, args=("Alice", 25))
t2 = threading.Thread(target=process, args=("Bob", 30))
t1.start()
t2.start()
t1.join()
t2.join()
print("All threads finished")