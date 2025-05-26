from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.balance_editor_interface import BalanceEditorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class BalanceEditorView(ViewInterface):
  def __init__(self, controller: BalanceEditorInterface)-> None:
    self.__controller = controller

  def handle(self, http_request: HttpRequest)-> HttpResponse:
    
      user_id = http_request.params.get("user_id")
      new_balance = http_request.body.get("new_balance")
      headers_user_id = http_request.headers.get("uid")

      self.__validate_inputs(user_id, new_balance, headers_user_id)
      response = self.__controller.edit(user_id, new_balance)
      return HttpResponse(body={"data":response},status_code=200)

      

  def __validate_inputs(self, user_id, new_balance, header_user_id:any)-> None:
      if (
        not user_id
        or not new_balance
        or not isinstance(new_balance, float)
        or int(header_user_id) != int(user_id)

      ):
        raise Exception("Invalid Input")
      
