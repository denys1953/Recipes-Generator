from pydantic import BaseModel
from typing import List, Optional

class RecipeAIResponse(BaseModel):
    title: str
    description: str
    ingredients: List[str]
    instructions: List[str]
    cooking_time: int
    difficulty: str
    calories: int

