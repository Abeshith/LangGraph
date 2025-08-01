from pydantic import BaseModel, Field
from typing import Literal, List, Any, Dict, Optional
import os
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAI
from utils.config_loader import load_config 
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI

class ConfigLoader:
    def __init__(self):
        self.config = load_config()
    
    def __getitem__(self, key):
        return self.config[key]


class ModelLoader(BaseModel):
    model_provider: Literal["groq", "google", "openrouter"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, ___context:Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True
    
    def load_model(self):
        """
        Load the model based on the specified provider.
        """
        if self.model_provider == "groq":
            api_key = os.getenv("GROQ_API_KEY")
            model = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model = model, api_key=api_key)

        elif self.model_provider == "google":
            api_key = os.getenv("GOOGLE_API_KEY")
            model = self.config["llm"]["gemini"]["model_name"]
            llm = GoogleGenerativeAI(model=model, api_key=api_key)
            
        elif self.model_provider == "openrouter":
            api_key = os.getenv("OPENROUTER_API_KEY")
            model = self.config["llm"]["openrouter"]["model_name"]
            llm = ChatOpenAI(model=model, openai_api_key=api_key)

        return llm