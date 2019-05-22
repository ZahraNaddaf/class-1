# Mirror in the middle of a list


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print (lst)

lst1 = lst.reverse()
#print (lst)
count_of_members = len(lst)
mirror_location =(count_of_members)/2
#print "mirror location :", mirror_location

num = (mirror_location)


if count_of_members % 2 == 0:
    right = lst[0:num]
    left = lst[num:]
    print "Left:", left, "  Right:", right

else:
    right = lst[0:num+1]
    left = lst[num:]
    print "Left:", left, "  Right:", right



#if we wan't to show the middle number in odd list, replace right and left in "else" with:
# right = lst[0:num]
# left = lst [num+1::]




