import pytest
from django.contrib.auth.models import User


# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user("test-user")

# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") == True

# def test_set_check_password(user_1):
#     assert user_1.username == "test-user"

# def test_new_user(new_user):
#     print(new_user.first_name)
#     assert new_user.first_name == "MyName"

# def test_new_staff_user(staff_user):
#     print(staff_user.first_name)
#     assert staff_user.first_name == "IAmStaffUser"
#     assert staff_user.is_staff == True

# def test_new_staff_user(user_factory):
#     print(user_factory.username)
#     assert True

# def test_new_staff_user1(user_factory):
#     user = user_factory.build()  # This is same as above, which is implicit behavior of build strategy
#     print(user.username)
#     assert True

# # 2nd strategy: create, which requires test database to create object
# @pytest.mark.django_db
# def test_new_staff_user2(user_factory):
#     user = user_factory.create()  # This is same as above, which is implicit behavior of build strategy
#     count = User.objects.all().count()
#     print(f"Users count: {count}")
#     print(user.username)
#     assert True

# @pytest.mark.django_db
# def test_new_staff_user3(user_factory):
#     user = user_factory.build()  # build doesn't save object into database
#     count = User.objects.all().count()  # To prove, here is the count to check whether user is created or not
#     print(f"Users count: {count}")
#     print(user.username)
#     assert True


# pytest-factoryboy example test
def test_new_user(new_user):
    print(new_user.username)
    print(f"Staff status: {new_user.is_staff}")
    assert True

def test_product(product_factory):
    product = product_factory.build()
    print(f"description: {product.description}")
    assert True
