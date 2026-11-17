from fastapi import HTTPException
from fastapi_restful.cbv import cbv
from pydantic import BaseModel, ConfigDict, Field



from sqlalchemy.orm import Session
from fastapi.params import Depends

from database import get_db
from fastapi import APIRouter

from routers.base import BaseAPI



router = APIRouter(prefix="/user", tags=["User"])

@cbv(router)
class UserAPI(BaseAPI):
    db: Session = Depends(get_db)
    
