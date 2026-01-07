# Exercise 2: Finding the good ones #

The goal of this exercise is to recognize good and bad unit tests in an existing code base. Have a look at all the unit tests in this file and answer the following questions.

1. Can you find unit tests that have a good name?
   Explain why.
2. Can you find unit tests that have a bad name?
   Explain why.
3. Can you find unit tests for which the contents are good ?
   Explain why.
4. Can you find unit tests for which the contents are bad ?
   Explain why.

## Test functions ##

def test_something_function(self):
    sut = MySut()
    value = sut.something(1, 2, 3)
    expected_value = 4
    self.assertEqual(value, expected_value)

    sut._private_value= 5
    value = sut.something(1, 2, 3)
    self.assertNotEqual(value, expected_value)

def test_slow_function__made_fast__passes(self):
    sut = MySut()
    expected_result = 10
    # There is no method to change the value of _wait_time other than
    # directly accessing it. It would be better to create a test-interface to
    # set this, but for now change the value to 0 to speed up the test
    sut._wait_time = 0

    result = sut.slow_function()

    self.assertEqual(result, expected_result)

def test_my_test(self):
    sut = MySut()
    expected_result = 10

    result = sut.slow_function()

    self.assertNotEqual(result, expected_result)