ex1=int(input("Number of multiplication table: "))
count = 1

while ex1 > 10 or ex1 < 0:
    print("Only value until 10")

while (count < 10):
    mt = ex1 * count
    print()
    print(ex1, "x", count, "= ", mt)
    count += 1