from fastapi import APIRouter, status

from app.api.modules.classrooms.exceptions import ClassroomNotFoundException
from app.api.modules.classrooms.repository import ClassroomRepository
from app.api.modules.classrooms.schemas import SClassroomInfo

router = APIRouter(
    prefix="/classrooms",
)


@router.get(
    path="/{classroom_id}",
    response_model=SClassroomInfo,
    status_code=status.HTTP_200_OK,
    summary="Get classroom information.",
    description="Get classroom by id. If classroom with classroom_id not found/exist, raise ClassroomNotFoundException",
    tags=["Student"],
    responses={
        status.HTTP_200_OK: {
            "model": SClassroomInfo,
            "description": "Classroom found.",
        },
        # ClassroomNotFoundException.status_code: {
        #     "model": None,
        #     "description": ClassroomNotFoundException.detail,
        # }
    }
)
async def get_test(classroom_id: int):
    classroom = await ClassroomRepository.find_one_or_none(id=classroom_id)
    if not classroom:
        raise ClassroomNotFoundException
    return classroom.ClassroomModel


# @router.post(
#     path="/classroom/create",
#     response_model=SClassroomInfo,
#     status_code=status.HTTP_200_OK,
#     summary="Get classroom information.",
#     description="Get a classroom by id. If classroom with classroom_id not found/exist, raise ClassroomNotFoundException",
#     tags=["Student"],
#     responses={
#         status.HTTP_200_OK: {
#             "model": SClassroomInfo,
#             "description": "Classroom created successfully.",
#         },
#         # TODO: maybe handle unexpected exceptions?
#     }
# )
# async def create_classroom(title: str, description: str):
#     classroom = await ClassroomRepository.add(
#         title=title,
#         description=description,
#     )
#     return classroom
