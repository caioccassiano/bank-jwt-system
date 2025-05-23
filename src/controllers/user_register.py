from src.models.interface.user_repository_interface import UserRepositoryInterface

class UserRegister:
  def __init__(self, user_repository:UserRepositoryInterface )-> None:
    self.__user_repo = user_repository

  def register_user(self, username:str, password:str, balance:float):
    pass

  