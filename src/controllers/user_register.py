from src.models.interface.user_repository_interface import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler


class UserRegister:
  def __init__(self, user_repository:UserRepositoryInterface )-> None:
    self.__user_repo = user_repository
    self.__password_handler = PasswordHandler()

  def register_user(self, username:str, password:str)-> dict:
    hashed_password = self.__create_hash_password(password)
    self.__registry_new_user(username, hashed_password)
    return self.__format_response(username)

  def __create_hash_password(self, password:str)->str:
    return self.__password_handler.encrypt_password(password)
  
  def __registry_new_user(self, username:str, hashed_password:str)->None:
    self.__user_repo.registry_user(username, hashed_password)

  def __format_response(self, username:str)-> dict:
    return {
      "type": "User",
      "count":1,
      "username": username
    }



