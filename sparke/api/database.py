from fastapi import APIRouter

from sparke.config import System, Settings
from sparke.interfaces.jobs.ppjobs import SparkePackageJob

router = APIRouter(prefix='/database', tags=['Database'], responses={404: {"description": "Not found"}})

settings = Settings(
        # chroma_sysdb_impl="sparke.db.works.sqlite.SqliteDB",
        # chroma_producer_impl="sparke.db.works.sqlite.SqliteDB",
        # chroma_consumer_impl="sparke.db.works.sqlite.SqliteDB",
        # chroma_segment_manager_impl="chromadb.segment.impl.manager.local.LocalSegmentManager",
        allow_reset=True,
        is_persistent=True,
        persist_directory="d:\\test",
    )

system = System(settings)
spp = SparkePackageJob(system)


@router.post("/createtemplatefolder")
async def createtemplatefolder(path: str):
    response = spp.createtemplatefolder(path)
    return response

@router.post("/update")
async def update():
    pass

@router.post("/delete")
async def delete():
    pass

@router.post("/query")
async def query():
    pass

