import pytest
import allure


@allure.title("TC#1 Verify that 3-3 is equal to 0")
@allure.description("This is a regression Test case")
@pytest.mark.regression
def test_sub0():
    assert 3-3 == 0


@allure.title("TC#2 Verify that 2-2 is not equal to 0")
@allure.description("This is a regression Test case")
@pytest.mark.skip
def test_sub1():
    assert 2-2 != 0


@allure.title("TC#3 Verify that 1-1 is equal to 0")
@allure.description("This is a Sanity Test case")
@pytest.mark.sanity
def test_sub2():
    assert 1-1 == 0


@allure.title("TC#4 Verify that 0-0 is equal to 0")
@allure.description("This is a Smoke Test case")
@pytest.mark.smoke
def test_sub3():
    assert 0-0 == 0


@allure.title("TC#5 Verify that 2-2 is equal to 0")
@allure.description("This is a Smoke Test case")
@pytest.mark.smoke
def test_sub4():
    assert 2-2 == 0
