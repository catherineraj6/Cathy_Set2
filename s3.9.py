dict = {"Cathy":7,"Victor":"funny","Anita":8,8:"awesome"};
count = 0;
for i in dict:
        m = dict.get(i)
        if (m != str(m)):
            count += 1;
print("The number of number values are:",count)
