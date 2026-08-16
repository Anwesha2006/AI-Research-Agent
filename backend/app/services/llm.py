from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import settings
from dotenv import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(
    model=settings.GEMINI_MODEL,
    api_key=settings.GEMINI_API_KEY,
    temperature=settings.TEMPERATURE,
    max_output_tokens=settings.MAX_OUTPUT_TOKENS)
