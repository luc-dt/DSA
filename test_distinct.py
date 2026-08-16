import time
import unittest


class TestDistinct(unittest.TestCase):

    def check_case(self, A, expected):
        """Run solution, time it, and print a detailed PASS/FAIL report."""
        start = time.perf_counter()
        result = solution(A)
        runtime = time.perf_counter() - start

        print()
        print("=" * 70)
        print(f"Input      : {A}")
        print(f"Output     : {result}")
        print(f"Expected   : {expected}")
        print(f"Runtime    : {runtime:.8f}s")
        print(f"Status     : {'PASS' if result == expected else 'FAIL'}")
        print("=" * 70)

        self.assertEqual(result, expected)

    def test_example(self):
        """Standard array with duplicates."""
        self.check_case([2, 1, 1, 2, 3, 1], 3)

    def test_empty_array(self):
        """Edge Case: Empty list."""
        self.check_case([], 0)

    def test_single_element(self):
        """Edge Case: Single element array."""
        self.check_case([42], 1)

    def test_all_identical(self):
        """All elements are the same."""
        self.check_case([5, 5, 5, 5], 1)

    def test_negative_numbers(self):
        """Array with negative and positive values."""
        self.check_case([-10, -5, -10, 0, 5, -5], 4)

    def test_invalid_type(self):
        """Defensive test: Invalid type input."""
        start = time.perf_counter()

        with self.assertRaises(TypeError):
            solution("invalid_string_input")

        runtime = time.perf_counter() - start

        print()
        print("=" * 70)
        print(f"Input      : 'invalid_string_input'")
        print(f"Expected   : TypeError raised")
        print(f"Runtime    : {runtime:.8f}s")
        print(f"Status     : PASS")
        print("=" * 70)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDistinct)
    unittest.TextTestRunner(verbosity=2).run(suite)