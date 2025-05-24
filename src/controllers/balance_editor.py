from src.models.interface.user_repository_interface import UserRepositoryInterface
from .interfaces.balance_editor_interface import BalanceEditorInterface

class BalanceEditor(BalanceEditorInterface):
  def __init__(self, user_repository: UserRepositoryInterface)-> None:
    self.__user_repository = user_repository

  def edit(self, user_id:int, new_balance:float = None )->dict:
    self.__user_repository.edit_balance(user_id, new_balance)
    return {
      "type": "User",
      "count": 1,
      "new_balance": new_balance

    }
  
