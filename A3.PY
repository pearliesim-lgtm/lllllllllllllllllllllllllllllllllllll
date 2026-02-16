import array as arr

array_num=arr.array('i',[2,4,6,8,10,12,14,16])
print("Orignal array:"+str(array_num))


print("Number of occurrences of the nuber 3 :"+str(array_num.count(3)))

array_num.reverse()
print("Reverse the order of items:")
print(str(array_num))