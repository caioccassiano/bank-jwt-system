class HttpResponse:
  def __init__(sel, body:dict, status_code:int)-> None:
    self.body = body
    self.status_code = status_code


  