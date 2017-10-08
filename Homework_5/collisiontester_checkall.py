""" Check all collision programs, record pass/fail

Using the collisiontester (YOU must finish collisiontester), check
all executable collision programs for correctness.

This program is provided to you 
as a service, so that you can focus on writing your
test suite not have to learn the json and glob modules
"""
import unittest
import importlib
import glob
import io
import sys
import json

import collision_tester

SUPPRESS_OUTPUT = False


def check_all_files():
    passed, failed = [], []

    Programs = glob.glob('cf/collisionc*')
    for file_name in Programs:
        if "hard" in file_name: continue

        loader = unittest.loader.TestLoader()
        results = unittest.result.TestResult()

        try:

            if SUPPRESS_OUTPUT:
                s = io.StringIO()
                sys.stdout = s

            collision_tester.PROGRAM_TO_TEST = file_name

            tests = loader.loadTestsFromTestCase(
                collision_tester.CollisionTestCase)

            tests.run(results)

            tests_passed = results.testsRun - len(results.failures) - len(
                results.errors)

            if results.wasSuccessful():
                passed.append(file_name)
            else:
                failed.append(file_name)
            if SUPPRESS_OUTPUT:
                sys.stdout = sys.__stdout__

        except Exception as e:
            if SUPPRESS_OUTPUT:
                sys.stdout = sys.__stdout__

            print('exception', file_name, e)
            failed.append(file_name)

        print(collision_tester.PROGRAM_TO_TEST,":")
        print('Run {} tests'.format(tests_passed))
        print('You passed {} tests'.format(tests_passed))
        for test, output in results.failures:
            print(">>", test)
            print(">>", output)
        for test, output in results.errors:
            print(">>", test)
            print(">>", output)

    return passed, failed


if __name__ == "__main__":
    passed, failed = check_all_files()
    Results = {
        'failed': failed,
        'passed': passed,
        'authors': collision_tester.AUTHORS
    }
    with open('collisiontest_results.json', 'w') as f:
        json.dump(Results, f, indent=4)
