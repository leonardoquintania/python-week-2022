# from dataclasses import dataclass
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select
from pydantic import validator


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int


brewdog = Beer(name="Bewdog", style="NEIPA", flavor=6, image=8, cost=8)
