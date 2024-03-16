from uuid import UUID, uuid4

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api.db.base import Base


class ImageModel(Base):
    __tablename__ = "images"

    uuid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    filename: Mapped[str] = mapped_column(String(50))

    # one to one. child to parent = image to user.
    user_uuid: Mapped[UUID] = mapped_column(ForeignKey("users.uuid", ondelete="CASCADE"))
    user: Mapped["UserModel"] = relationship(back_populates="icon")

    # many to one. child to parent = images to comment.
    comment_id: Mapped[int] = mapped_column(ForeignKey("comments.id", ondelete="CASCADE"))
    comment: Mapped["CommentModel"] = relationship(back_populates="images")

    # many to one. child to parent = images to comment.
    step_id: Mapped[int] = mapped_column(ForeignKey("steps.id", ondelete="CASCADE"))
    step: Mapped["StepModel"] = relationship(back_populates="images")