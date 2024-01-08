import unittest
from calc import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertRaises(ZeroDivisionError, divide, 5, 0)  # Expect an error when dividing by zero

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCalculator))
    return unittest.TextTestRunner().run(test_suite)

if __name__ == '__main__':
    result = run_tests()
    total_tests = result.testsRun
    failed_tests = len(result.failures) + len(result.errors)
    passed_tests = total_tests - failed_tests

    print("\nTest Results")
    print("============")
    print(f"Passed: {passed_tests}/{total_tests}")

    # Calculate and display grade
    grade = (passed_tests / total_tests) * 100
    print(f"Grade: {grade}%")

    # This can be used by GitHub Actions for final grading
    # You might need to adjust this part based on your CI setup
    with open("grade.txt", "w") as file:
        file.write(f"{grade}")
