from fastapi import APIRouter

router = APIRouter(prefix='/database', tags=['Database'], responses={404: {"description": "Not found"}})

@router.post("/create")
async def create():

    pass

@router.post("/update")
async def update():
    pass

@router.post("/delete")
async def delete():
    pass

@router.post("/query")
async def query():
    pass

