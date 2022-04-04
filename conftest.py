from asyncio import SendfileNotAvailableError
from django.contrib.auth.models import User
import pytest
from pytest_factoryboy import register

from tests.factories import UserFactory, CategoryFactory, ProductFactory

register(UserFactory)      # Fixture name will be: user_factory
register(CategoryFactory)  # Fixture name will be: category_factory
register(ProductFactory)   # Fixture name will be: product_factory


# @pytest.fixture()
# def user_1(db):
#     user = User.objects.create_user("test-user")
#     return user

# @pytest.fixture
# def new_user_factory(db):
#     def create_app_user(
#         username: str,
#         password: str = None,
#         first_name: str = "firstname",
#         last_name: str = "lastname",
#         email: str = "test@test.com",
#         is_staff: bool = False,
#         is_superuser: bool = False,
#         is_active: bool = True
#     ):
#         user = User.objects.create_user(
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             is_staff=is_staff,
#             is_superuser=is_superuser,
#             is_active=is_active
#         )
#         return user
#     return create_app_user

# @pytest.fixture
# def new_user(db, new_user_factory):
#     return new_user_factory("Test_user", "password", "MyName")

# @pytest.fixture
# def staff_user(db, new_user_factory):
#     return new_user_factory("Test_staff_user", "password", "IAmStaffUser", is_staff=True)

@pytest.fixture
def new_user(db, user_factory):
    user = user_factory.create()
    return user
