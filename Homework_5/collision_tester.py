"This is the main part of the assignment"""

# Copyright 2017 Michael Graziano mjgrazia@bu.edu
import unittest
import subprocess

# Please change this to valid author emails
AUTHORS = ['mjgrazia@bu.edu']

PROGRAM_TO_TEST = "cf/collisionc_24_hard"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)


class CollisionTestCase(unittest.TestCase):

    def test_programname(self):
        self.assertTrue(PROGRAM_TO_TEST.startswith('cf/'),"wrong program name")

    def test_emptycmd(self):
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,[""],"")
        self.assertEqual(rc,2)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

    def test_inval_in(self):
        strin = "one 20 10 -2 1 two"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,1)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

    def test_one(self):
        strin = "one 20 10 -2 1"
        correct_out = "3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_decimal_time(self):
        strin = "one 20 10 -2 1"
        correct_out = "2.5\none 15 12.5 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2.5"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_neg_time(self):
        strin = "one 20 10 -2 1"
        correct_out = "1\none 18 11 -2 1\n3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1","-2","3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_multi_in(self):
        strin = "one 20 10 -2 1\ntwo 30 20 -2 1\nthree 10 0 -2 1"
        correct_out = "3\none 14 13 -2 1\ntwo 24 23 -2 1\nthree 4 3 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_headon(self):
        strin = "one -10 0 1 0\ntwo 10 0 -1 0\n"
        correct_out1 = "2\none -8 0 1 0\ntwo 8 0 -1 0\n"
        correct_out2 = "5\none -5 0 1 0\ntwo 5 0 -1 0\n"
        correct_out3 = "7\none -7 0 -1 0\ntwo 7 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2","5","7"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,
                         correct_out1 + correct_out2 + correct_out3
                        )
        self.assertEqual(errs,"")
        
    def test_station(self):
        strin = "one -15 0 1 0\ntwo 0 0 0 0\n"
        correct_out1 = "2\none -13 0 1 0\ntwo 0 0 0 0\n"
        correct_out2 = "5\none -10 0 1 0\ntwo 0 0 0 0\n"
        correct_out3 = "7\none -10 0 0 0\ntwo 2 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2","5","7"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,
                         correct_out1 + correct_out2 + correct_out3
                        )
        self.assertEqual(errs,"")

    def test_ninety(self):
        strin = "one -10 0 1 0\ntwo 0 10 0 -1\n"
        

def main():
    "show how to use runprogram"

#    print(runprogram('./test_program.py', ["4", "56", "test"], "my input"))
    unittest.main()
          
if __name__ == '__main__':
    main()

