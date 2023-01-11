#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-01-11 08:01:17
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


import pytest
import requests

import app


class MockResponse:
    
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


@pytest.fixture
def mock_response(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockResponse()
    
    monkeypatch.setattr(requests, "get", mock_get)


def test_get_json(mock_response):

    result = app.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"