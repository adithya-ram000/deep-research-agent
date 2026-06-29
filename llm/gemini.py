from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from core.config import MODEL_NAME,TEMPERATURE

load_dotenv()

model = ChatGoogleGenerativeAI(
    model =MODEL_NAME,
    temperature =TEMPERATURE,
)
