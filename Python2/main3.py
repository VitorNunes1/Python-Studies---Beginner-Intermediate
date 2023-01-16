f = open("isthat.txt", "r")

try: 
    su = 0
    for _ in range(5):
        n = int(f.readline())
        su += n

    print('Sun of the numbers = {}, average = {}'.format(su, su/5))

finally:
    f.close()
