from .user_register_view import UserRegisterView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class MockController:
  def register_user(self, username, password):
    return {"alguma":"coisa"}

def test_handle_user_register():
  body = {
    "username": "MyUsername",
    "password": "MyPassword"
  }

  request = HttpRequest(body=body)

  mock_controller = MockController()
  view = UserRegisterView(mock_controller)

  response = view.handle(request)
  print()
  print(response)
  print(response.body)

  assert isinstance(response, HttpResponse)
  assert response.body == {"data": {"alguma":"coisa"}}
  assert response.status_code == 201


  
