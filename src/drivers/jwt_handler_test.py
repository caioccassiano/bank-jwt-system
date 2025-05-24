from .jwt_handler import JwtHandler

def test_jwt_handler():
  jwt_handler = JwtHandler()
  body= {
    "email": "caio@gmail.com",
    "username": "caioccasiano",
    "senha": "kdfjewbicoepwd"
  }
  token = jwt_handler.create_jwt_token(body=body)
  token_informations = jwt_handler.decode_jwt_token(token)

  assert token is not None
  assert isinstance(token, str)
  assert token_informations["username"] == body["username"]

  print(token)
  print()
  print(token_informations)

  


  




