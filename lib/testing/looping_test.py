import io
import sys
import pytest
from looping import happy_new_year, square_integers, fizzbuzz

class TestLoops:
    def test_prints_10_to_1_hny(self):
        '''prints 10 to 1 countdown then "Happy New Year!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        happy_new_year()
        sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()
    
        answer_list = answer.split('\n')
        assert answer_list[-2] == "Happy New Year!", "Your final line does not match 'Happy New Year!', check spelling/capitalization!"

    def test_square_integers(self):
        '''returns squared ints for [1, 2, 3, 4, 5] and [-1, -2, -3, -4, -5]'''
        assert square_integers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25], "Squaring positive integers failed"
        assert square_integers([-1, -2, -3, -4, -5]) == [1, 4, 9, 16, 25], "Squaring negative integers failed"

class TestFizzBuzz:
    def test_prints_1_to_100_fizzbuzz(self):
        '''prints 1 to 100 with fizz 3s, buzz 5s, fizzbuzz 3and5s'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fizzbuzz()
        sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()
    
        assert "Fizz" in answer, "Fizz multiples not found"
        assert "Buzz" in answer, "Buzz multiples not found"
        assert "FizzBuzz" in answer, "FizzBuzz multiples not found"
        for i in range(1, 101):
            if i % 3 != 0 and i % 5 != 0:
                assert str(i) in answer, f"Number {i} not found"

if __name__ == "__main__":
    pytest.main()
