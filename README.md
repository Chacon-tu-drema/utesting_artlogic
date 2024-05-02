# Artlogic Testing Workshops
## Setup
go to the directory that you want to the workshop to be
```bash
python3 -m venv vevn
source venv/bin/activate
pip install poetry
```

day 1
---
## Agile practices
- scrim & kanbas
- eXtreme Programming
### why do we need them??
pear programing and testing enviroments. addres technical debt (trades off between quality and speed)
### XP practices
#### Feedback practicies
- TDD
- Pair programming
#### Design practices
- Simple design
- Refactoring
### Pair programming
- keep each other on task
- clarify ideas
- Brainstorm
- Lower frustration because of bugg fixing
- hold each other accountable
#### Pair programming roles
##### The navigator and the driver
- Navigator: thinks about the big picture, the next steps, and the overall direction
- Driver: Focuses on the details, writes the code, and keeps the navigator on track
###### Switching roles
- **Chess clock:** roles switch every in a time interval
- **Ping pong:** roles switch every time a test passes
- **Pomodoro:** roles switch in an interval with a brake after
###### Pair rotation
- **Change by task:** roles switch every task
### TDD
The core benefit of TDD:
- **Design:**
Creates a more felixible and maintainable codebase
- **Documetation:**
The test serves as the documentation of the code
- **Debugging:**
Testing work as a debugging tool, help you to find faster the bug
- **Courge:**
You can make changes without fear of breaking the code
#### Three laws of TDD
1. write a failing test
2. write the minimum amount of code to make the test pass
3. refactor the code
#### Baby steps
1. **Fake implementation:**
Hardcode the return value
2. **Obvious implementation:**
When you know the code you want to write
3. **Triangulation:**
Generalize behavior

##### Notes
* Assertions are what make a test a test
* just code for the test you are writing

## Exercise
1. Write a function that takes numbers from 1 to 100 and outputs them as a string, but for multiples of three returns “Fizz” instead of the number and for the multiples of five returns “Buzz”. For numbers which are multiples of both three and five returns “FizzBuzz”.

To start the excercice create a new poetry project:
```bash
poetry new <project name>
cd <project name>
poetry add pytest
```

2. Leap year kata
Write a function that returns true or false depending on whether its input integer is a leap year or not.
A leap year is defined as one that is divisible by 4, but is not otherwise divisible by 100 unless it is also divisible by 400.
For example, 2001 is a typical common year and 1996 is a typical leap year, whereas 1901 is an atypical common year and 2000 is an atypical leap year.

To start the excercice create a new poetry project:
```bash
poetry new <project name>
cd <project name>
poetry add pytest
```

### Solution
1. 
[fizzbuzz.py](./fizzbuzz/fizzbuzz/fizzbuzz.py)
```python
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
```
test_fizzbuzz.py (./fizzbuzz/tests/test_fizzbuzz.py)
```python
from fizzbuzz.fizzbuzz import FizzBuzz
from parameterized import parameterized

class TestFizzBuzz:
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
```
2.
[leap_year.py](./leap_year/leap_year/leap_year.py)
```python
class LeapYearCalculator:
    def is_leap_year(self, year: int) -> bool:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False
```
[test_leap_year.py](./leap_year/tests/test_leap_year.py)
```python
from parameterized import parameterized

from leap_year_kata.leap_year_kata import LeapYearCalculator


class TestLeapYearCalculator:
    @parameterized.expand(
        [
            (2001, False), 
            (1996, True), 
            (1900, False), 
            (2000, True)
        ]
    )
    def test_is_leap_year(self, year, is_leap) -> None:
        assert LeapYearCalculator().is_leap_year(year) == is_leap
```
---

