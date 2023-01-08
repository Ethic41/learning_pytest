#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-01-08 13:29:18
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


import pytest


### Intro to fixtures

class Fruit:
    
    def __init__(self, name):
        self.name = name
        self.cubed = False
    

    def cube(self):
        self.cubed = True


class FruitSalad:

    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self.__cube_fruit()
    

    def __cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()
    

# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)


### fixtures of fixtures

# Arrange
@pytest.fixture
def first_entry() -> str:
    return "a"


# Arrange
@pytest.fixture
def order(first_entry) -> list[str]:
    return [first_entry]


def test_string(order: list[str]):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]


### reusable fixtures


def test_int(order: list):
    # Act
    order.append(2)

    # Assert
    assert order == ["a", 2]



### requesting multiple fixtures

# Arrange
@pytest.fixture
def second_entry():
    return 2


# Arrange
@pytest.fixture
def order1(first_entry, second_entry):
    return [first_entry, second_entry]


# Arrange
@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]


def test_string1(order1, expected_list):
    # Act
    order1.append(3.0)

    # Assert
    assert order1 == expected_list


### fixtures and caching

# Arrange
@pytest.fixture
def order_for_caching():
    return []


# Act
@pytest.fixture
def append_first(order_for_caching, first_entry):
    return order_for_caching.append(first_entry)


def test_string_only(append_first, order_for_caching, first_entry):
    # Assert
    assert order_for_caching == [first_entry]


### Autouse & fixtures

@pytest.fixture(autouse=True)
def append_first_1(order_for_caching, first_entry):
    return order_for_caching.append(first_entry)


def test_string_only_1(order_for_caching, first_entry):
    assert order_for_caching == [first_entry]


def test_string_and_int(order_for_caching, first_entry):
    order_for_caching.append(2)
    assert order_for_caching == [first_entry, 2]

