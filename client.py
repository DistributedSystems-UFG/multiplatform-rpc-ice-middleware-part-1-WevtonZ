import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:tcp -h 98.90.53.6 -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

rep = printer.printString("Hello World!")
print("printString returned:", rep)

rep = printer.concat("Hello ", "World!")
print("concat returned:", rep)

rep = printer.contains("Hello World!", "World")
print("contains returned:", rep)

rep = printer.contains("Hello World!", "Python")
print("contains returned:", rep)
