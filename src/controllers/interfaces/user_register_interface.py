from abc import ABC, abstractmethod

class UserRegisterInterface(ABC):

  @abstractmethod
  def register_user(self, username:str, password:str)-> dict: pass