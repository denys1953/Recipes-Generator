from fastapi import APIRouter, Depends, UploadFile, File

from src.ai_provider.service import AIService
from src.auth.dependencies import get_current_user
from src.database import get_db

ai_service = AIService()
router = APIRouter()

@router.post("/test-ai")
async def test_ai(difficulty: int, ingredients: list[str], current_user=Depends(get_current_user), db=Depends(get_db)):
    recipe = await ai_service.create_recipe_from_text(difficulty=difficulty, ingredients=ingredients, user_id=current_user.id, db=db)
    return recipe

@router.post("/test-ai-image")
async def test_ai_image(difficulty: int, file: UploadFile = File(...), current_user=Depends(get_current_user), db=Depends(get_db)):
    image_data = await file.read()
    recipe = await ai_service.create_recipe_from_image(difficulty=difficulty, image_data=image_data, user_id=current_user.id, db=db)
    return recipe