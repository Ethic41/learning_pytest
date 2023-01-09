#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-01-09 09:19:15
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


smtpserver = "mail.python.org"


def test_showhelo(smtp_connection):
    assert 0, smtp_connection.helo()

