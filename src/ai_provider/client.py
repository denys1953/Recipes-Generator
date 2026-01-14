from src.config import settings
from .schemas import RecipeAIResponse
from src.recipes.service import save_recipe
from sqlalchemy.ext.asyncio import AsyncSession
from src.recipes.models import Recipe

from typing import Optional

import google.generativeai as genai
from sqlalchemy.future import select

class GeminiClient:
    def __init__(self):
        genai.api_key = settings.GEMINI_API_KEY
        self.model = genai.GenerativeModel(
            model_name=settings.GEMINI_MODEL_NAME,
            generation_config={
                "response_mime_type": "application/json", 
                "response_schema": RecipeAIResponse
            }
        )

    async def generate_recipe(self, prompt: str, user_id: int, db: AsyncSession, image_data: Optional[bytes] = None) -> RecipeAIResponse:
        content = [prompt]
        
        query = select(Recipe.title).where(Recipe.user_id == user_id)
        result = await db.execute(query)
        restriction = "Make sure you don't repeat the following recipes: " + ", ".join([row[0] for row in result.all()])
        
        if result:
            content.append(restriction)

        if image_data:
            content.append({
                "mime_type": "image/jpeg",
                "data": image_data
            })

        response = self.model.generate_content(content)
        
        recipe = RecipeAIResponse.model_validate_json(response.text)

        await save_recipe(db, recipe, user_id)

        return recipe
    

