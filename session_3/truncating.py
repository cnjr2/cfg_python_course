from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that hit CTRL-C"
print "otherwise hit ENTER"

raw_input("?")

print "opening file.."
target = open(filename, "w")

print "truncating the file"
target.truncate()

print "now we're going to print lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")





