from .login_creator import LoginCreator
from src.drivers.password_handler import PasswordHandler

username = "meuUsername"
password = "minhaSenha"
hashed_password = PasswordHandler().encrypt_password(password)


class MockUserRepository:
  def get_user_by_username(self, username):
    return(10, username, hashed_password)


def test_create():
  login_creator = LoginCreator(MockUserRepository())
  response = login_creator.create(username, password)

  assert response["access"] == True
  assert response["username"] == username
  assert response["token"] is not None
  

  print(response["username"])
  print()
  print()
  print(response["token"])
