from fastapi import FastAPI , Depends
from app.routing import todo
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app = FastAPI()


# Routes

app.include_router(todo.router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    # error = exc.errors()[0]

    # return JSONResponse(
    #     content={
    #         "field ": error["loc"][-1],
    #         "Error": error["msg"]
    #     },
    #     status_code=422
    # )
    errors = {}
    for error in exc.errors():
        print(f"The error is: {error}")
        errors[error["loc"][-1]] = error["msg"]

    return JSONResponse(
        {"message": "Validation Error", "errors": errors}, status_code=422
    )
















