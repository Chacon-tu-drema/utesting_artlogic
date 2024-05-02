class FizzBuzz:
    def number_conversion_to_string(self, number: int) -> str:
        if number < 0 or number > 100:
            return "Out of range"
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"
        return str(number)
