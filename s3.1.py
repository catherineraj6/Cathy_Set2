

def delete(list):

    newlist = [];
    deletedlist = [];
    counter = 0

    for i in list:
        if (i != 5 and i != 9 and i!= 6):
            newlist.append(i)
        if(i == 5 or i == 9 or i == 6):
            deletedlist.append(i)
    print(deletedlist);
    print(newlist);
    for i in deletedlist:
        if i:
            counter+=1
    print("Number of deleted numbers:",counter)
list = [1,2,3,4,5,6,7,8,9,10]
delete(list)


