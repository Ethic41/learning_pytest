#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-01-06 21:30:05
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) != 5


def except_fun():
    raise SystemExit(1)


def test_except_fun():
    with pytest.raises(SystemExit):
        except_fun()


def test_need_file(tmp_path):
    print(tmp_path)
    assert 0


def except_fun1():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r"123"):
        except_fun1()

