my_id = "ilovepython"
password = "mypass1234"

string1 = input("Enter id: ")
string2 = input("Enter password: ")
if ((string1 != my_id) and (string2 != password)):
    print("Identification and password not found")
if ((string1 == my_id) and (string2 == password)):
    print("Welcome")
if (string1 != my_id) and (string2 == password):
    print("Identification not found")
if ((string1 == my_id) and (string2 != password)):
    print("The password is wrong")
