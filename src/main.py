from fastapi import FastAPI, UploadFile, File

from src.ai_provider.service import AIService

# from app.auth.router import router as auth_router

swagger_params = {
    "persistAuthorization": True
}

app = FastAPI(
    swagger_ui_parameters=swagger_params
)
ai_service = AIService()

@app.get("/")
async def main():
    return {"Status": "OK"}

@app.post("/test-ai")
async def test_ai(ingredients: list[str]):
    recipe = await ai_service.create_recipe_from_text(ingredients)
    return recipe

@app.post("/test-ai-image")
async def test_ai_image(file: UploadFile = File(...)):
    image_data = await file.read()
    recipe = await ai_service.create_recipe_from_image(image_data)
    return recipe


# app.include_router(auth_router, prefix="/auth", tags=["Auth"])