from pydantic import BaseModel


class RecipeRequest(BaseModel):
    difficulty: int
    ingredients: list[str]