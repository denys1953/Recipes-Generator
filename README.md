# AI Recipes Generator

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
[![PostgreSQL](https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com)

An asynchronous **FastAPI** service that leverages **Google Gemini AI** to transform your ingredients or food photos into delicious, structured recipes.

## 🚀 Key Features

*   **Multimodal AI**: Generate recipes from text ingredients or by uploading a photo (Computer Vision).
*   **Structured Output**: AI responses are strictly validated via Pydantic models.
*   **User History**: Each generated recipe is saved to a PostgreSQL database linked to your account.
*   **JWT Authentication**: Secure endpoints using OAuth2 password flow with JWT tokens.
*   **Async Architecture**: Fully asynchronous database operations and AI requests.
*   **Scalable Structure**: Modular project organization (Separation of Concerns).

---

## 🛠 Tech Stack

*   **Core**: FastAPI, Pydantic v2
*   **AI Engine**: Google Generative AI (Gemini 1.5 Flash)
*   **Database**: PostgreSQL, SQLAlchemy 2.0 (Async)
*   **Migrations**: Alembic
*   **Image Processing**: Pillow (PIL)
*   **Security**: Jose (JWT), Bcrypt
*   **Environment**: Docker & Docker Compose

---

## 📥 Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd "Recipes Generator"
2. Configure Environment Variables

Create a .env file in the root directory and fill in your credentials:

# App Security
SECRET_KEY=your_generated_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=recipes
POSTGRES_HOST=db  # Use 'localhost' for local run, 'db' for Docker
POSTGRES_PORT=5432

# AI Provider
GEMINI_API_KEY=your_google_gemini_api_key
GEMINI_MODEL_NAME=gemini-1.5-flash
3. Run with Docker (Recommended)

docker-compose up --build

The API will be available at http://localhost:8000

4. Local Setup (Manual)

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start server
uvicorn src.main:app --reload
📂 Project Structure
code
Text
download
content_copy
expand_less
├── alembic/              # Database migrations
├── src/
│   ├── auth/             # Authentication & JWT logic
│   ├── users/            # User models & profiles
│   ├── recipes/          # Recipe storage & history
│   ├── ai_provider/      # Gemini AI integration
│   ├── generator/        # Core business logic (Orchestrator)
│   ├── config.py         # Global settings
│   ├── database.py       # Async DB connection
│   └── main.py           # Application entry point
├── docker-compose.yml
└── Dockerfile
🔐 API Endpoints Summary
Method	Endpoint	Description	Auth
POST	/auth/register	Register a new user	❌
POST	/auth/login	Get JWT Access Token	❌
GET	/users/me	Get current user profile	✅
POST	/generator/text	Generate recipe from ingredients	✅
POST	/generator/image	Generate recipe from photo	✅
GET	/recipes/history	View your generated recipes	✅
📖 Usage Examples
Generate from Ingredients (cURL)

curl -X 'POST' \
  'http://localhost:8000/generator/text' \
  -H 'Authorization: Bearer <YOUR_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "difficulty": 2,
  "ingredients": ["chicken breast", "broccoli", "soy sauce"]
}'

