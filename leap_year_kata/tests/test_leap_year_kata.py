from parameterized import parameterized

from leap_year_kata.leap_year_kata import LeapYearCalculator


class TestLeapYearCalculator:
    @parameterized.expand([(2001, False), (1996, True), (1900, False), (2000, True)])
    def test_is_leap_year(self, year, is_leap) -> None:
        assert LeapYearCalculator().is_leap_year(year) == is_leap
