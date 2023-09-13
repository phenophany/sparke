import uvicorn
from starlette.middleware.cors import CORSMiddleware

import sparke
import sparke.config
from fastapi import FastAPI

settings = sparke.config.Settings()

app = FastAPI(
    # title=settings.title,
    # description=settings.description,
    # version=settings.version,
    # docs_url=settings.docs_url,
    # redoc_url=settings.redoc_url,
    # openapi_url=settings.openapi_url,
)

origins = [
    "*",  # 允许所有域名访问
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)

