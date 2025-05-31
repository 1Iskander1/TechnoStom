from fastapi import APIRouter

from .categories.views import router as categories_router
from .consumers.views import router as consumers_router
from .demo_auth.views import router as auth_router
from .materials.views import router as materials_router

# from .posts.views import router as posts_router
from .roles.views import router as roles_router

# from .specialization.views import router as spec_router
from .tasks.views import router as tasks_router
from .users.auth import router as C
from .users.views import router as users_router

router = APIRouter()
# router2 = APIRouter()
# router3 = APIRouter()
# router4 = APIRouter()

router.include_router(router=auth_router)
router.include_router(router=users_router, prefix="/users")
router.include_router(router=tasks_router, prefix="/tasks")
router.include_router(router=roles_router, prefix="/roles")
router.include_router(router=consumers_router, prefix="/consumers")
router.include_router(router=materials_router, prefix="/materials")

router.include_router(router=categories_router, prefix="/categories")
# router.include_router(
#     router=spec_router,
#     prefix="/specializations",
#     tags=["Specializations"],  # Добавьте явное указание тега
# )
# router.include_router(router=users_router)
# router3.include_router(router=posts_router, prefix="/posts")
