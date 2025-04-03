class MyClass:
    a = 10

# Create an object and change the attribute
obj = MyClass()
obj.a = 0

print(MyClass.a)  # This will print 10, class attribute remains unchanged
print(obj.a)      # This will print 0, instance attribute is changed
