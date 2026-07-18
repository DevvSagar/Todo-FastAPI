from fastapi import FastAPI , Depends
from app.routes import todo , auth
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.config.app_config import get_app_config


app = FastAPI()


# Routes

app.include_router(todo.router)
app.include_router(auth.router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = {}
    for error in exc.errors():
        print(f"The error is: {error}")
        errors[error["loc"][-1]] = error["msg"]

    return JSONResponse(
        {"message": "Validation Error", "errors": errors}, status_code=422
    )



@app.get("/")
def root():
    config = get_app_config()
    return{
        "app_name": config.app_name
    }










