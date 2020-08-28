def string(dict):
    dict = {"Alex":"nice","Cathy":"also nice"}
    for key in dict:
        if key:
            print(key[-1::-1])
string(dict)
