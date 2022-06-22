# from dataclasses import dataclass
from typing import Optional
from sqlmodel import SQLModel, Field
# from sqlmodel import select
from pydantic import validator
from statistics import mean
from datetime import datetime


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, value, field):
        if value < 1 or value > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return value

    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean(
            [
                values["flavor"],
                values["image"],
                values["cost"]
            ]
        )
        print(v)
        return int(rate)


# brewdog = Beer(name="Bewdog", style="NEIPA", flavor=6, image=8, cost=8)
