#try:
#    3 / 0
#except Exception as e:
#    print("Error: %s" % e)
#x = [1,2,3,4,5]
#y = "Cactus"
#try:
#    if 3 in x and "u" in y:
#        3 / 0
#        print("Yahoo")
#except ZeroDivisionError as e:
#    print("Error: %s" % e)
#except ArithmeticError as e:
#    print("Dance")
try:
    3 / 1
#    print("Yahoo")
except ZeroDivisionError as e:
    print("Error: %s" % e)
except ArithmeticError as e:
    print("Error: %s" % e)
except SyntaxError as e:
    print("Error %s" % e)
finally:
    print("No error at all")
    