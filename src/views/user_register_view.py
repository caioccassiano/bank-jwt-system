from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.user_register_interface import UserRegisterInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse



class UserRegisterView(ViewInterface):

  def __init__(self, controller: UserRegisterInterface):
    self.__controller = controller
    


  def handle(self, http_request:HttpRequest)-> HttpResponse:
    username = http_request.body["username"]
    password = http_request.body["password"]

    self.__validate_inputs(username, password)
    response = self.__controller.register_user(username, password)
    return HttpResponse(body={"data": response},status_code= 201)

  def __validate_inputs(self, username, password)->None:
    if(
      not username
      or not password
      or not isinstance(username, str)
      or not isinstance(password, str)
    ):
      raise Exception("Invalid Input")

