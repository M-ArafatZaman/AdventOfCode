# I didnt make this but its so clean I had to put it here
string = open("input.in", "r").readline()
for j in 4, 14:
    i = 0
    while (len(set(string[i:i+j])) != j): i+= 1
    print(i+j)