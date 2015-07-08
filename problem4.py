import unittest, funwithfibonachi
class fibonacciTest(unittest.TestCase):
	def test_generate_series(self):
		self.assertEqual(fibonacci.fibonacc(5), "0,1,1,2,3", msg="5 fibonacci should return 0,1,1,2,3.")
		self.assertFalse(fibonacci.fibonacci(5), "string", msg="5 should not return string")
		self.assertEqual(fibonacci.fibonacci )
	def test_generate_series_sum(self):
		self.assertEqual(fibonacci.fibonacci(5), 7, msg="5 fibonacci should return 7")
		self.assertEqual(fibonacci.fibonacci("string"), "even" or "odd", msg="value should return even or odd!")
if __name__ == '__main__':
	unittest.main()
		
