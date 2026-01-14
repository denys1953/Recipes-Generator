from datetime import UTC, datetime

from src.database import Base
from sqlalchemy.orm import relationship
from src.users.models import User

from sqlalchemy import DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)  
    ingredients: Mapped[list] = mapped_column(JSONB) 
    instructions: Mapped[list] = mapped_column(JSONB)
    cooking_time: Mapped[int] = mapped_column(nullable=False)
    difficulty: Mapped[str] = mapped_column(nullable=False)
    calories: Mapped[int] = mapped_column(nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(tz=UTC),
        server_default=sa.text("CURRENT_TIMESTAMP"),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(tz=UTC),
        onupdate=datetime.now(tz=UTC),
        server_default=sa.text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    author: Mapped[list["User"]] = relationship(
        back_populates="recipes",
    )
    
    
