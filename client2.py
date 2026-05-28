import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 98.90.53.6 -p 11000")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 98.90.53.6 -p 11000")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

rep = printer1.printString("Hello World from printer1!")
print("printer1.printString:", rep)

rep = printer1.concat("Distributed ", "Systems")
print("printer1.concat:", rep)

rep = printer1.contains("Distributed Systems", "Systems")
print("printer1.contains:", rep)

rep = printer2.printString("Hello World from printer2!")
print("printer2.printString:", rep)

rep = printer2.concat("ICE ", "Middleware")
print("printer2.concat:", rep)

rep = printer2.contains("ICE Middleware", "Java")
print("printer2.contains:", rep)
