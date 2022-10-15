

from cgi import print_form


list1 = ["physics", "mathematics","science",1000,2001]
list2 = [1,2,3,4,5,6,7]
list3 = ["a","b","c","d","e"]


print(list1[2]) ,print(list2[4])

print(list3[4])

#to delete
print("Before deleting index of 2 is science  = : ")
print(list1)
del list1[2]
print("after deletion")
print("")
print(list1)
list4 = list1 + list2 + list3
print(list4)