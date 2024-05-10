from fastapi import APIRouter
from app.views import list_user, retrieve_user, create_user, delete_user, update_user

user_router = APIRouter(prefix="/users", tags=["user"])

user_router.add_api_route(path="/", endpoint=create_user, methods=["POST"])
user_router.add_api_route(path="/", endpoint=list_user, methods=["GET"])
user_router.add_api_route(path='/{user_id}', endpoint=retrieve_user, methods=["GET"])
user_router.add_api_route(path='/{user_id}', endpoint=update_user, methods=["PUT"])
user_router.add_api_route(path='/{user_id}', endpoint=delete_user, methods=["DELETE"])