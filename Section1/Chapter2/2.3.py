# testStr = "Test \t \" \n \" "
# print(testStr) 

# testStr = "New string to test a variable: %s" % "New Variable"
# print(testStr)
testStr = "new string to test variable: %s, %f3" % ("NEW VERSION",3)
# print(testStr) 
# c = testStr[0:]
# c = testStr.upper()
# print(c)
# c = testStr.replace("NEW VERSION", "Yay")
# print(c)
c = testStr.split(" ")
# print(c[2:5])
print(c.index("NEW"))