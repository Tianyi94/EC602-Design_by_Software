# Copyright 2017 Michael Graziano mjgrazia@bu.edu

class Polynomial():
    def __init__(self, coefs):

        """ __init__: Creates the container for the polynomial based on the 
            provided  list coefs
        """
        
        self.express = {} # Dictionary for storing

#        if not coefs:
#            self.express.update({0:0})
#        else:
        for i in range(len(coefs) - 1, -1, -1): 
            self.express.update({i : list(reversed(coefs))[i]})

    def __getitem__(self, key):

        """ __getitem__: Allows for the exact exponent to be reference by
            key without having to access express directly.
        """
        
        return self.express[key];

    def __setitem__(self, key, value):
        
        """ __setitem__: Allows forthe reassignment or creation of a value
            based onthe referenced key.
        """

        self.express.update({key:value})

    def __len__(self):
        
        """ __len__: Provides the length of the of the polynomial when the 
            built in function len() is called.
        """
        
        return len(self.express)

    def keys(self):
        
        """ keys: Retrieves the list of dictionary keys that relate to the 
            various exponents of the Polynomial.
        """

        return self.express.keys()

    def copy(self):
        
        """ copy: Creates a copy of the Polynomial. Usually used to avoid
            channging values of an existing variable when creating a new
            variable.
        """

        new_poly = Polynomial([])
        for key in self.keys():
            new_poly[key] = self[key]
        return new_poly

    def pop(self, key):
        
        """ pop: Removes the exponential key and its associated value from the
            Polynomial.
        """

        self.express.pop(key)

    def __str__(self):

        """ __str__: Creates the 'informal' output for the Polynomial class
            when called from str(Polynomial), print() and format().
        """

        return str(self.express)

    def __repr__(self):

        """ __repr__: Creates the "official" string representation of the 
            Polynomial class.
        """

        return str(self.express)

    def __add__(self, poly):

        """ __add__: Updates the '+' symbol in order to allow for the 
            expression Poly 1 + Poly 2 to produce a valid result.
        """

        new_poly = Polynomial([])
        master_keys = set(self.keys()).union(set(poly.keys()))

        for key in master_keys:
            if key in self.express and key in poly.express:
                new_poly[key] = self[key] + poly[key]
            elif key in self.express and key not in poly.express:
                new_poly[key] = self[key]
            else:
                new_poly[key] = poly[key]
            
            if new_poly[key] == 0:
                new_poly.pop(key)
            else:
                continue

        return new_poly

#        new_express = self.express.copy()
#        new_express.update(poly.express)
#
#        for expon in new_express.keys():
#            if expon in self.express and expon in poly.express:
#                new_express[expon] = self.express[expon] + poly.express[expon]
#            elif expon in self.express and expon not in poly.express:
#                new_express[expon] = self.express[expon]
#            else:
#                pass
#
#        for expon in list(reversed(list(new_express.keys()))):
#            if new_express[expon] == 0:
#                new_express.pop(expon)
#            else:
#                break
#
#        return Polynomial(list(reversed(list(new_express.values()))))

    def __sub__(self, poly):

        """ __sub__: Updates the '-' symbol in order to allow for the
            express Poly 1 + Poly 2 to produce a valid result.
        """
    
        new_poly = poly.copy()
        
        for key in new_poly.keys():
            new_poly[key] = new_poly[key] * -1

        return self.__add__(new_poly)

#        return self.__add__(Polynomial([-x for x in list(reversed(
#                            list(poly.express.values())
#                           ))]))
        
    def __mul__(self, poly):
        
        """__mul__: Updates the "*" symbol in order to allow for the 
            expression Poly 1 * Poly 2 to produce a valid result.
        """
        
        products = []

        for key1 in poly.keys():
            new_poly = Polynomial([])
            for key2 in self.keys():
                new_key = key1 + key2
                new_value = poly[key1] * self[key2]
                new_poly[new_key] = new_value
            products.append(new_poly)
        
        for i in range(len(products)):
           if i == 0 and len(products) == 1:
                return products[i]
           elif i == 0:
                final_poly = products[i] + products[i+1]
           elif i == 1:
                continue
           else:
                temp_poly = final_poly.copy()
                final_poly = products[i] + temp_poly

        return final_poly

    def deriv(self):

        """deriv(): Method that will return the derivative of the Polynomial.
        """

        new_poly = Polynomial([])
        
        for key in self.keys():
            if key == 0:
                continue
            else:
                new_poly[key-1] = self[key] * key

        return new_poly
                
def main():
    # Polynomial Creation Practice
    test = [Polynomial([]),
            Polynomial([1]),
            Polynomial([5, 6, 8]),
            Polynomial([7, 9, 2, 4])
           ]
    adder = Polynomial([1, 2, 3])
    diff = Polynomial([5, 3, 8])
    multi = Polynomial([2, 3])

    # Polynomial "Pretty Print" Practice
    for item in test:
        print(item)
#        print(adder)
#        print(item + adder)
#        print(diff)
#        print(item - diff)
        item[-2] = 10
#        print(item.deriv())
        print(item)
        print(multi)
        print(item * multi)
        print(diff)
        print(item - diff)
#    print("Polynomial Adder = ", adder)
#    adder_copy = adder.copy()
#    adder_copy[1] = 0
#    print("Polynomial Adder = ", adder_copy)
#    print("Polynomial Adder = ", adder)


if __name__=="__main__":
	main()
