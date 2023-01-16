def new_func():
    sick1 = int(input('Adicione um valor: '))
    sick2 = int(input('Adicione um valor: '))
    sick3 = int(input('Adicione um valor: '))
    res = (sick2 * sick3) + sick1

    if (res > 100):
        print('Senai')
    else:
        print('Echola')

new_func()