import pytest


@pytest.mark.regression
def test_sub0():
    assert 2-2 == 0


@pytest.mark.skip
def test_sub1():
    assert 2-2 != 0


@pytest.mark.sanity
def test_sub2():
    assert 1-1 == 0


@pytest.mark.smoke
def test_sub3():
    assert 0-0 == 0


@pytest.mark.smoke
def test_sub4():
    assert 2-2 == 0
