class Protected:
    def __init__(self):
        self.__privateVar = 23 #Declare Variable
        
    def prntPrivate (self):
        print (self.__privateVar) #Print Variable

    def declarePrivate (self, private): #Set Variable to private
        self.__privateVar = private

obj = Protected()
obj.prntPrivate()
obj.declarePrivate(24) #Changed Variable
obj.prntPrivate()
