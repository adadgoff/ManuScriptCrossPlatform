"""One more Update Data Base Structure

Revision ID: 5d5a73f18897
Revises: d2197eac8199
Create Date: 2024-02-22 02:22:09.175020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d5a73f18897'
down_revision: Union[str, None] = 'd2197eac8199'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ClassesInfo',
    sa.Column('ClassId', sa.Integer(), nullable=False),
    sa.Column('ClassName', sa.String(), nullable=False),
    sa.Column('ClassDescription', sa.String(), nullable=True),
    sa.Column('ClassLogotypeLink', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('ClassId')
    )
    op.create_table('LessonsInfo',
    sa.Column('LessonId', sa.Integer(), nullable=False),
    sa.Column('LessonName', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('LessonId')
    )
    op.create_table('ModulesInfo',
    sa.Column('ModuleId', sa.Integer(), nullable=False),
    sa.Column('ModuleName', sa.String(), nullable=False),
    sa.Column('ModuleDescription', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('ModuleId')
    )
    op.create_table('Steps',
    sa.Column('StepId', sa.Integer(), nullable=False),
    sa.Column('StepContentType', sa.String(), nullable=False),
    sa.Column('StepDescription', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('StepId')
    )
    op.create_table('StepsSolved',
    sa.Column('Email', sa.Integer(), nullable=False),
    sa.Column('StepId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('Email')
    )
    op.create_table('Lessons',
    sa.Column('LessonId', sa.Integer(), nullable=False),
    sa.Column('StepId', sa.Integer(), nullable=False),
    sa.Column('StepOrder', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['StepId'], ['Steps.StepId'], ),
    sa.PrimaryKeyConstraint('LessonId')
    )
    op.create_table('Modules',
    sa.Column('ModuleId', sa.Integer(), nullable=False),
    sa.Column('LessonId', sa.Integer(), nullable=False),
    sa.Column('LessonOrder', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['LessonId'], ['Lessons.LessonId'], ),
    sa.PrimaryKeyConstraint('ModuleId')
    )
    op.create_table('Classes',
    sa.Column('ClassId', sa.Integer(), nullable=False),
    sa.Column('ModuleId', sa.Integer(), nullable=False),
    sa.Column('ModuleOrder', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ModuleId'], ['Modules.ModuleId'], ),
    sa.PrimaryKeyConstraint('ClassId')
    )
    op.create_table('ClassesStudents',
    sa.Column('Email', sa.String(), nullable=False),
    sa.Column('ClassId', sa.Integer(), nullable=False),
    sa.Column('IsActive', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['ClassId'], ['Classes.ClassId'], ),
    sa.PrimaryKeyConstraint('Email')
    )
    op.create_table('ClassesTeachers',
    sa.Column('Email', sa.String(), nullable=False),
    sa.Column('ClassId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ClassId'], ['Classes.ClassId'], ),
    sa.PrimaryKeyConstraint('Email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ClassesTeachers')
    op.drop_table('ClassesStudents')
    op.drop_table('Classes')
    op.drop_table('Modules')
    op.drop_table('Lessons')
    op.drop_table('StepsSolved')
    op.drop_table('Steps')
    op.drop_table('ModulesInfo')
    op.drop_table('LessonsInfo')
    op.drop_table('ClassesInfo')
    # ### end Alembic commands ###
