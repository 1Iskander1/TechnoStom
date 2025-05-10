from fastapi import APIRouter

# from .posts.views import router as posts_router
from .products.views import router as products_router
from .roles.views import router as roles_router
from .tasks.views import router as tasks_router
from .users.views import router as users_router

router = APIRouter()
# router2 = APIRouter()
# router3 = APIRouter()
# router4 = APIRouter()


router.include_router(router=users_router, prefix="/users")
router.include_router(router=tasks_router, prefix="/tasks")
router.include_router(router=roles_router, prefix="/roles")
# router3.include_router(router=posts_router, prefix="/posts")
