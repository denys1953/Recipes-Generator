from datetime import datetime

from src.ai_provider.schemas import RecipeAIResponse

class Recipe(RecipeAIResponse):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime