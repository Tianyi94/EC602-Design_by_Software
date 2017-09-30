# Copyright 2017 Michael Graziano mjgrazia@bu.edu

class Polynomial():
    def __init__(self, coefs):

        """ __init__: Creates the container for the polynomial based on the 
            provided  list coefs
        """
        
        self.express = {} # Dictionary for storing

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

    def __sub__(self, poly):

        """ __sub__: Updates the '-' symbol in order to allow for the
            express Poly 1 + Poly 2 to produce a valid result.
        """
    
        new_poly = poly.copy()
        
        for key in new_poly.keys():
            new_poly[key] = new_poly[key] * -1

        return self.__add__(new_poly)

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

    def __eq__(self, poly):
        
        """ __eq__: Method that will compare two exponents to verify if they
            are equal or not
        """

        equal = False

        for key1 in self.keys():
            for key2 in poly.keys():
                if key1 == key2 and self[key1] == poly[key2]:
                    equal = True
                    break
                else:
                    equal = False
            if not equal:
                break

        return equal

    def eval(self, value):
        
        """ eval: Method that will return the result of Polynomial based on
            substituting the x statement with the passed value.
        """

        result = 0
        
        for key in self.keys():
            result += self[key]*(value**key)
        
        return result

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
    pass
    # Polynomial Creation Practice
#    test = [Polynomial([]),
#            Polynomial([1]),
#            Polynomial([5, 6, 8]),
#            Polynomial([7, 9, 2, 4]),
#            Polynomial([1.35, 2.42])
#           ]
#    adder = Polynomial([1, 2, 3])
#    diff = Polynomial([5, 3, 8])
#    multi = Polynomial([2, 3])
#    compare = Polynomial([5, 6, 8])
#
    # Polynomial "Pretty Print" Practice
#    for item in test:
#        print(item)
#        print(item.eval(3))
#        print(adder)
#        print(item + adder)
#        print(diff)
#        print(item - diff)
#        item[-2] = 10
#        print(item.deriv())
#        print(item)
#        print(multi)
#        print(item * multi)
#        print(diff)
#        print(item - diff)
#        print(compare)
#        print(item == compare)
#    print("Polynomial Adder = ", adder)
#    adder_copy = adder.copy()
#    adder_copy[1] = 0
#    print("Polynomial Adder = ", adder_copy)
#    print("Polynomial Adder = ", adder)

if __name__=="__main__":
	main()
