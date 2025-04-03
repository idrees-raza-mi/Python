a=input("insert  a string :").lower()
spam=["Make a lot of money","buy now","subscribe this","click this"]

if any(word in a for word in spam):
    print("spam")
else:print("page is good enough")