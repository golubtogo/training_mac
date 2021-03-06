from fixture.group import Group
from fixture.user import User
import random
import allure


def test_add_user_in_group(app, orm):
    with allure.step('Given a group list'):
        if len(orm.get_group_list()) == 0:
            app.group.create_group(Group(group_name="group1"))
    with allure.step('Given a non-empty group list'):
        app.user.select_group()
        group_id = app.user.get_group_id(id)
        group_id = int(group_id)
    with allure.step('Given a user list not in group %s' % group_id):
        users_list = orm.get_users_not_in_group(Group(id=group_id))
        if len(users_list) == 0:
            app.user.create_user(User(lastname="lastname1", firstname="firstname1"))
            users_list = orm.get_users_not_in_group(Group(id=group_id))
        user = random.choice(users_list)
    with allure.step('When I add the user %s to the list' % user):
        app.user.add_user_to_group_by_id(user.id)
        app.user.open_link_selected_group()
    with allure.step('Then the new user list in group %s is equal to the old list without the deleted user' % group_id):
        user_in_group = orm.get_users_in_group(sorted(orm.get_group_list_by_id(Group(id=group_id)), key=Group.id_or_max)[0])
        assert user in user_in_group

