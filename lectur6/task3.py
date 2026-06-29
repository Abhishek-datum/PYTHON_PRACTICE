# suppose there are two lists one containing nuber from 1 to 6 and other containing number fromn 6 to 1.
#  write to obtain a list thaat contains elements contains obtained by adding corresponding elememnts of the two lists.

# list1=[1,2,3,4,5,6]
# list2=[6,5,4,3,2,1]
# result=[7,7,7,7,7,7]
def displayCombineList(list1,list2):
   finallist=[]
   for x,y in zip(list1,list2):
        finallist.append(x+y)
   return finallist
list1=[1,2,3,4,5,6]
list2=[6,5,4,3,2,1]
output=displayCombineList(list1,list2)
print(output)