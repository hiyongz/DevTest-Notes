from fastapi import FastAPI
from exception import golbal_exception_handlers
from user.user import router_user

app = FastAPI(debug=True, exception_handlers=golbal_exception_handlers)

app.include_router(router_user, prefix='/api/v1')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='0.0.0.0', port=9002, reload=True)