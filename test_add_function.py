"""
Code to test the add function using pytest
"""
from pytest import mark

# import local module
from company_program import add


@mark.math_functions
def test_add():
    for int_1 in range(1, 201):
        for int_2 in range(1, 201):
            for int_3 in range(1, 201):
                assert add(int_1, int_2, int_3) == int_1 + int_2 + int_3


# test expected to fail
@mark.math_functions
@mark.xfail
def test_add_false():
    assert add(1, 1, 1) == 404
