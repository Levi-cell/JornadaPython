# args
def teste_args(*args):
    print(args)


teste_args("parâmetro1", 2, 3.0, None)

# kwargs


def teste_kwargs(**kwargs):
    print(kwargs)


teste_kwargs(p1="parâmetro1", p2=2, p3=3.0, p4=None)

# sem args


def teste_sem_args(p1, p2, p3, p4):
    print(p1, p2, p3, p4)


p_list = ["parâmetro1", 2, 3.0, None]
teste_sem_args(*p_list)

