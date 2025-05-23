from .password_handler import PasswordHandler


def test_encrypt():

  minhaSenha = "Caio123"
  password_handler = PasswordHandler()

  hashed_password = password_handler.encrypt_password(minhaSenha)
  checked_password = password_handler.check_password(minhaSenha, hashed_password)

  assert checked_password

  


