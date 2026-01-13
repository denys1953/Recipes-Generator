from src.config import settings
from .schemas import RecipeAIResponse

from typing import Optional

import google.generativeai as genai

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

    async def generate_recipe(self, prompt: str, image_data: Optional[bytes] = None) -> RecipeAIResponse:
        content = [prompt]

        if image_data:
            content.append({
                "mime_type": "image/jpeg",
                "data": image_data
            })

        response = self.model.generate_content(content)

        return RecipeAIResponse.model_validate_json(response.text)
    

