from fcntl import F_FULLFSYNC, F_GET_SEALS


try:
    x = int(input("Digite um valor interior: "))
    y = int(input("Digite um valor interior: "))

    def altera_val_global():

