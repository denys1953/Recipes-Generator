from fastapi import APIRouter, Depends, UploadFile, File

from src.ai_provider.service import AIService
from src.auth.dependencies import get_current_user
from src.database import get_db

ai_service = AIService()
router = APIRouter()

@router.post("/test-ai")
async def test_ai(ingredients: list[str], current_user=Depends(get_current_user), db=Depends(get_db)):
    recipe = await ai_service.create_recipe_from_text(ingredients=ingredients, user_id=current_user.id, db=db)
    return recipe

@router.post("/test-ai-image")
async def test_ai_image(file: UploadFile = File(...), current_user=Depends(get_current_user)):
    image_data = await file.read()
    recipe = await ai_service.create_recipe_from_image(image_data)
    return recipe