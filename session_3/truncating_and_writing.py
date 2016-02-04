from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C"
print "If you want that, hit RETURN"

raw_input("?")

print "Opening file.."
target = open(filename, "w")

print "Truncating the file, goodbye!"
target.truncate()

print "Now i'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally we close the file"
target.close()