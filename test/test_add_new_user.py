# -*- coding: utf-8 -*-

from model.user import User
import os


def test_add_new_user(app):
    app.session.login(username="admin", password="secret")
    app.user.add_new(User(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
                          photo=os.getcwd() + "\\images\\test_image.png", title="title",
                          company="company", address="address\n+380111111111",
                          home="home", mobile="mobile", work="work", fax="fax",
                          email="e-mail", email_2="e-mail2", email_3="e-mail3", homepage="homepage",
                          byear="2000", bmonth="January", bday="1", ayear="2015", amonth="February", aday="1",
                          secondary_address="secondary address", secondary_phone="secondary home", notes="hello"
                          ))
    app.user.choose_group()
    app.user.submit()
    app.session.logout()

