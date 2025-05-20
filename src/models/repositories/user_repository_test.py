from .user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler

def test_registry_user():
  db_connection_handler.connect()
  conn = db_connection_handler.get_connection()
  repo = UserRepository(conn=conn)

  username = "Milton"
  password = "1234Miltin!"

  repo.registry_user(username=username, password=password)






