from pydantic import BaseModel
from datetime import datetime

class publicacionesModel(BaseModel):
    title : str
    description :str
    created_at : datetime = datetime.now()
    status: bool