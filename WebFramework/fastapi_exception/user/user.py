from fastapi.routing import APIRouter

from .exception import UserDoesNotExistsException

router_user = APIRouter(prefix='/user', tags=['用户模块'])

@router_user.get("/{user_id}")
async def get_id_by_user(user_id: int):
    if user_id != 1:
        # 这里使用我们自定义的用户错误处理
        # 返回的统一响应格式{"code":10000,"err_msg":"user does not exists","status":"Failed"}
        raise UserDoesNotExistsException
    return {"user_id": user_id}