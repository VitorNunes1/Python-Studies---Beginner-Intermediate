try:
    def adult_func(n):
        if n >= 18:
            return True
        else:
            return False
    ages = [34, 39, 20, 18, 13, 54]

    print("List of adults: ")
    #filter só funciona por causa da condição True
    for a in filter(adult_func, ages):
        print(a, end = ' ')
    
    def usual():
        ages = [24, 29, 20, 38, 13, 54, 8]

        print("List of adults: ")

        for a in filter(lambda x: x >= 19, ages):
            print(a, end = ' ')
        usual()
except:
    print("Invalid.")