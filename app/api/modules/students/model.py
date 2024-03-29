from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.api.db.base import Base


class StudentModel(Base):
    __tablename__ = "students"

    classroom_id: Mapped[int] = mapped_column(ForeignKey("classrooms.id"), primary_key=True)
    user_uuid: Mapped[UUID] = mapped_column(ForeignKey("users.uuid"), primary_key=True)
