from fastapi import APIRouter, Depends, Form, UploadFile, File

from src.ai_provider.service import AIService
from src.auth.dependencies import get_current_user
from src.database import get_db
from .schemas import RecipeRequest
from src.recipes.service import get_user_recipes_title, save_recipe

ai_service = AIService()
router = APIRouter()

@router.post("/text")
async def generate_text(
    request: RecipeRequest, 
    current_user=Depends(get_current_user), 
    db=Depends(get_db)
):
    titles = await get_user_recipes_title(db, current_user.id)
    recipe = await ai_service.create_recipe_from_text(difficulty=request.difficulty, ingredients=request.ingredients, titles=titles)
    await save_recipe(db, recipe, current_user.id)

    return recipe

@router.post("/image")
async def generate_image(
    difficulty: int = Form(...), 
    file: UploadFile = File(...), 
    current_user=Depends(get_current_user), 
    db=Depends(get_db)
):
    image_data = await file.read()
    titles = await get_user_recipes_title(db, current_user.id)
    recipe = await ai_service.create_recipe_from_image(difficulty=difficulty, image_data=image_data, titles=titles)
    await save_recipe(db, recipe, current_user.id)
    return recipe