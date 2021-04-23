#sorting a list using selective  sort
def sort(lst):
    for i in range(0,len(lst)):
        minpos = i #we are taking the postion of the first value in the loop
        for j in range(i,len(lst)): #to take the value from i to last of the loop. i varies since we shift the lowest
            if lst[j] < lst[minpos]: #values to the first index
                minpos = j #we are taking only the index position of the lowest value
#here we are interchanging the values
        temp = lst[i]#i is taken since i holds the first value to which we need to shif the lowest value.
        lst[i] = lst[minpos]
        lst[minpos] = temp


lst = [3,5,1,8,4,2]
sort(lst)
print(lst)