# Write a function that takes numbers from 1 to 100 and outputs them as a string, but for multiples of three returns “Fizz” instead of the number and for the multiples of five returns “Buzz”. For numbers which are multiples of both three and five returns “FizzBuzz”.

# number from [1-100] return string number
# if multiple of 3 return fizz
# if multple of 5 return buzz
from parameterized import parameterized

from fizzbuzz.fizzbuzz import FizzBuzz


class TestFizzBuzz:

    # def test_number_conversion_to_string(self):
    #     assert FizzBuzz().number_conversion_to_string(number=1) == "1"
    #     assert FizzBuzz().number_conversion_to_string(number=2) == "2"
    #     assert FizzBuzz().number_conversion_to_string(number=4) == "4"
    #     assert FizzBuzz().number_conversion_to_string(number=4) == "4"
    #     assert FizzBuzz().number_conversion_to_string(number=7) == "7"
    #
    # def test_number_conversion_when_multiple_of_3(self):
    #     assert FizzBuzz().number_conversion_to_string(number=3) == "Fizz"
    #     assert FizzBuzz().number_conversion_to_string(number=6) == "Fizz"
    #
    # def test_number_conversion_when_multiple_of_5(self):
    #     assert FizzBuzz().number_conversion_to_string(number=5) == "Buzz"
    #     assert FizzBuzz().number_conversion_to_string(number=10) == "Buzz"
    #
    # def test_number_conversion_when_multiple_of_5_and_3(self):
    #     assert FizzBuzz().number_conversion_to_string(number=15) == "FizzBuzz"
    #
    # def test_number_out_of_range(self):
    #     assert FizzBuzz().number_conversion_to_string(101) == "Out of range"

    @parameterized.expand(
        [
            (1, "1"),
            (2, "2"),
            (3, "Fizz"),
            (4, "4"),
            (5, "Buzz"),
            (15, "FizzBuzz"),
        ]
    )
    def test_fizzbuzz(self, number, output) -> None:
        assert FizzBuzz().number_conversion_to_string(number) == output
