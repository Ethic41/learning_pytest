#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-01-08 17:32:34
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from typing import Generator
from emaillib import Email, MailAdminClient, MailUser # type: ignore

import pytest


@pytest.fixture
def mail_admin():
    return MailAdminClient()


@pytest.fixture
def mail_user(mail_admin: MailAdminClient)-> Generator[MailUser, None, None]:
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)


@pytest.fixture
def sending_user(mail_user: MailUser):
    yield mail_user


@pytest.fixture
def receiving_user(mail_admin: MailAdminClient, mail_user: MailUser):
    yield mail_user
    mail_user.clear_mailbox()


def test_email_received(sending_user: MailUser, receiving_user: MailUser):
    email = Email(subject="Hey!", body="How's it going?")
    sending_user.send_email(email, receiving_user)
    assert email in receiving_user.inbox

