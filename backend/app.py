import traceback

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from db.database import engine
from models.usermodels import Base
from routes.user_routes import router as user_router
from utils.status_codes import INTERNAL_ERROR

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user_router)


@app.middleware("http")
async def exception_logger(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        traceback.print_exc()
        return JSONResponse(
            status_code=INTERNAL_ERROR,
            content={"detail": "Internal server error"},
        )


@app.get("/")
def test_db():
    return {"message": "DB CONNECTED SUCCESSFULLY"}
