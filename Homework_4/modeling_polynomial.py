#Copyright 2017 Michael Graziano mjgrazia@bu.edu

class Polynomial():
    def __init__(self, coefs):

        """ __init__: Creates the container for the polynomial based on the 
            provided  list coefs
        """
        self.coefs, self.expon = ([], [])
        if not coefs:
            self.coefs = [0]
            self.expon = [0]
        else:
            for value in reversed(coefs): 
                self.coefs.append(value)
                self.expon.append(list(reversed(coefs)).index(value))

    def __str__(self):

        """ __str__: Creates the 'informal' output for the Polynomial class
            when called from str(Polynomial), print() and format().
        """

        return "".join("{}*x^{} + ".format(self.coefs[i], self.expon[i]) \
               if i > 0 \
               else "{}*x^{}".format(self.coefs[i], self.expon[i]) \
               for i in range(len(self.coefs)-1,-1,-1))

def main():
    # Polynomial Creation Practice
    test = [Polynomial([]),
            Polynomial([1]),
            Polynomial([5, 6, 8]),
            Polynomial([7, 9, 2, 4])
           ]
    output = []

    # Polynomial "Pretty Print" Practice
    for item in test:
        print(item)

if __name__=="__main__":
	main()
