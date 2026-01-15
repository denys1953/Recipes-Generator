from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.recipes.models import Recipe
from src.recipes.schemas import Recipe as RecipeSchema

async def save_recipe(db: AsyncSession, recipe_in: RecipeSchema, user_id: int) -> Recipe:
    recipe = Recipe(
        **recipe_in.model_dump(), 
        user_id=user_id
    )

    db.add(recipe)
    await db.commit()
    await db.refresh(recipe)
    return recipe

async def get_user_recipes_title(db: AsyncSession, user_id: int) -> list[str]:
    query = select(Recipe.title).where(Recipe.user_id == user_id)
    result = await db.execute(query)
    return result.scalars().all()
