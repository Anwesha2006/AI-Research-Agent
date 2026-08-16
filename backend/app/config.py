from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    #app
    APP_NAME: str= "AI Research agent"
    APP_VERSION:str="1.0.0"
    DEBUG:bool=True
    #AI
    GEMINI_API_KEY: str
    #AI Settings
    GEMINI_MODEL:str="gemini-2.5-flash"
    MAX_OUTPUT_TOKENS:int=2048
    TEMPERATURE:float=0.7
    #environmental variables
    model_config={
        "env_file":".env",
        "env_file_encoding":"utf-8",
        "extra":"ignore"  
    }
settings=Settings()

