#!/usr/bin/python3
import pytest
import random

def test_success():
    """A successful test"""
    assert 1 + 1 == 2

def test_flaky_service():
    """A radom failure test for test retry function"""
    val = random.choice([True, False])
    print(f"random value: {val}")
    assert val is True
