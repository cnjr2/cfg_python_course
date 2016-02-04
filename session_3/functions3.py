
# another function
def print_fruit(fruit1, fruit2, fruit3):

	print fruit1 + "\t" + fruit2 + "\t" + fruit3


a = "apple"
b = "banana"
c = "mango"

print_fruit(a, b, c)
print_fruit(fruit1=a, fruit2=b, fruit3=c)
print_fruit(fruit2=a, fruit3=b, fruit1=c)

print_fruit("a", "b", "c")	

