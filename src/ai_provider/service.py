from typing import List, Optional
from .client import GeminiClient
from .schemas import RecipeAIResponse
from .constants import SYSTEM_PROMPT
from src.recipes.models import Recipe

class AIService:
    def __init__(self):
        self.client = GeminiClient()

    def _format_user_prompt(self, base_instruction: str, difficulty: int, titles: List[str]) -> str:    
        user_prompt = f"{base_instruction} The recipe should have a difficulty level of {difficulty} out of 10."

        if titles:
            restriction = "Make sure you don't repeat the following recipes: " + ", ".join(titles)
            user_prompt += "\n" + restriction

        full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"
        return full_prompt
    
    async def create_recipe_from_text(self, difficulty: int, ingredients: list[str], titles: Optional[list[str]]) -> RecipeAIResponse:
        base_instruction = f"Create a recipe from these ingredients: {', '.join(ingredients)}."
        full_prompt = self._format_user_prompt(base_instruction, difficulty, titles)

        return await self.client.generate_recipe(prompt=full_prompt)
    
    async def create_recipe_from_image(self, difficulty: int, image_data: bytes, titles: Optional[list[str]]) -> RecipeAIResponse:
        base_instruction = "Look at this photo and suggest a recipe using these ingredients."
        full_prompt = self._format_user_prompt(base_instruction, difficulty, titles)
        
        return await self.client.generate_recipe(prompt=full_prompt, image_data=image_data)