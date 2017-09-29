#Copyright 2017 Michael Graziano mjgrazia@bu.edu

class Polynomial():
    def __init__(self, coefs):

        """ __init__: Creates the container for the polynomial based on the 
            provided  list coefs
        """
        
        self.express = {} # Dictionary for storing

        if not coefs:
            self.express.update({0:0})
        else:
            for i in range(len(coefs) - 1, -1, -1): 
                self.express.update({i : list(reversed(coefs))[i]})

    def __add__(self, poly):

        """ __add__: Updates the '+' symbol in order to allow for the 
            expression Poly 1 + Poly 2 to produce a valid result.
        """

        new_express = self.express.copy()
        new_express.update(poly.express)

        for expon in new_express.keys():
            if expon in self.express and expon in poly.express:
                new_express[expon] = self.express[expon] + poly.express[expon]
            elif expon in self.express and expon not in poly.express:
                new_express[expon] = self.express[expon]
            else:
                pass

        for expon in list(reversed(new_express.keys())):
            if new_express[expon] == 0:
                new_express.pop(expon)
            else:
                break

        return Polynomial(list(reversed(new_express.values())))

    def __sub__(self, poly):

        """ __sub__: Updates the '-' symbol in order to allow for the
            express Poly 1 + Poly 2 to produce a valid result.
        """
    
        return self.__add__(Polynomial([-x for x in list(reversed(
                            poly.express.values()
                           ))]))
        
    def __len__(self):
        
        """ __len__: Provides the length of the of the polynomial when the 
            built in function len() is called.
        """
        
        return len(self.express)

    def __str__(self):

        """ __str__: Creates the 'informal' output for the Polynomial class
            when called from str(Polynomial), print() and format().
        """

        return str(self.express)

def main():
    # Polynomial Creation Practice
    test = [Polynomial([]),
            Polynomial([1]),
            Polynomial([5, 6, 8]),
            Polynomial([7, 9, 2, 4])
           ]
    adder = Polynomial([1, 2, 3])
    diff = Polynomial([5, 3, 8])
    output = []

    # Polynomial "Pretty Print" Practice
    for item in test:
        print(item)
        print(adder)
        print(item + adder)
        print(diff)
        print(item - diff)

if __name__=="__main__":
	main()
