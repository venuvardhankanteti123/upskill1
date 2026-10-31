from pydantic import BaseModel 

class RequestModel(BaseModel):
    name : str 
    age : int 
    region : str 
class ResponseModel(BaseModel):
    message : str 
    status : bool