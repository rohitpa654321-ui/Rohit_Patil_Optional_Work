# add new iteam :  add()
set1 = {"apple","banana","cherry"}
set1.add("orange")
print("1. ",set1)

# add set to set:  update()
set1 = {"apple","banana","cherry"}
set2 = {"pinapple","mango","kiwi"}
set1.update(set2)
print("2. ",set1)

# add any iteration:  update()
set1 = {"apple","banana","cherry"}
mylist = ["orange","kiwi","papaya"]
set1.update(mylist)
print("3. ",set1)