from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str = "mongodb://localhost:27017"
    db_name: str = "llm_app"
    
    class Config:
        env_file = ".env"

# Create the settings instance
settings = Settings()