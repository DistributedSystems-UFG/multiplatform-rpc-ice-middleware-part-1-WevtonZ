import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s + "*"

    def concat(self, a, b, current=None):
        result = a + b
        print("concat({}, {}) = {}".format(a, b, result))
        return result

    def contains(self, s, sub, current=None):
        result = sub in s
        print("contains({}, {}) = {}".format(s, sub, result))
        return result

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
adapter.activate()

communicator.waitForShutdown()
