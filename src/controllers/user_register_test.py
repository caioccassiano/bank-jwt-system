from .user_register import UserRegister

class MockUserRepository:
  def __init__(self)-> None:
    self.registry_user_atributes = {}

  def registry_user(self, username, password)-> None:
    self.registry_user_atributes["username"] = username
    self.registry_user_atributes["password"] = password


def test_registry():
  repository = MockUserRepository()
  controller = UserRegister(repository)

  username = "CaioCassiano"
  password = "myPassword"

  response = controller.register_user(username, password)

  print()
  print(response)
  print()
  print(repository.registry_user_atributes)

  assert repository.registry_user_atributes["password"] != password
  assert repository.registry_user_atributes["username"] == username

  assert response["type"] == "User"



# Cria um banco de dados fake com o MockRepository. Após chamar
# o controller, na funcao __registry_new_user, ele chama a
# funcao registry_user do repositório, através do self
# que foi injetado na dependencia. Depois verifica que a senha
# enviada é diferente da senha retornada após passar pelo controller
# e ser criptografada.

