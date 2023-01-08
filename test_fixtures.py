#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-01-08 13:29:18
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


import pytest


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
    assert all(fruit.cubed for fruit in fruit_salad)

