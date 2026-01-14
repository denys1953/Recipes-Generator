from .client import GeminiClient
from .schemas import RecipeAIResponse
from .constants import SYSTEM_PROMPT
from src.recipes.models import Recipe

class AIService:
    def __init__(self):
        self.client = GeminiClient()
    
    async def create_recipe_from_text(self, difficulty: int, ingredients: list[str], user_id: int, db) -> RecipeAIResponse:
        user_prompt = f"Create a recipe from these ingredients: {', '.join(ingredients)}. The recipe should have a difficulty level of {difficulty} out of 10."
        full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"
        return await self.client.generate_recipe(prompt=full_prompt, user_id=user_id, db=db)
    
    async def create_recipe_from_image(self, difficulty: int, image_data: bytes, user_id: int, db) -> RecipeAIResponse:
        user_prompt = f"Look at this photo and suggest a recipe using these ingredients. The recipe should have a difficulty level of {difficulty} out of 10."
        full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"
        return await self.client.generate_recipe(prompt=full_prompt, image_data=image_data, user_id=user_id, db=db)