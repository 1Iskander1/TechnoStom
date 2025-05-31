from fastapi import APIRouter

router = APIRouter(tags=["Auth"])


# @router.post("/auth/login", response_model=User)
# async def login(
#     login_data: dict,
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     # Get all users
#     stmt = select(User).order_by(User.id)
#     result = await session.execute(stmt)
#     users = result.scalars().all()
#
#     # Find user with matching credentials
#     user = next(
#         (
#             u
#             for u in users
#             if u.userLogin == login_data.get("Login")
#             and u.userPassword == login_data.get("Password")
#         ),
#         None,
#     )
#
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
#         )
#
#     # Check if user has Admin role
#     # Assuming role information is stored in role_id or similar field
#     # You'll need to adjust this based on your actual role checking logic
#     if user.role_id != 1:  # Adjust this condition based on your role IDs
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="User is not an administrator"
#         )
#
#     return user
