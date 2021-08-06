# -*- coding: utf-8 -*-

from model.user import UserModify


def test_modify_first_user(app):
    app.session.login(username="admin", password="secret")
    app.user.modify_first_user(UserModify(new_lastname="new lastname", new_firstname="new firstname",
                                          new_address="new address", new_home="new home", new_mobile="new mobile",
                                          new_work="new work", new_secondary_phone="new secondary phone",
                                          new_email="new_email", new_email_2="new_email_2", new_email_3="new_email_3"))
    app.session.logout()