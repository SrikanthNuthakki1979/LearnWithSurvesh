from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    model_name: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    mcp_server_base_url: str = os.getenv("MCP_SERVER_BASE_URL", "http://localhost:8001")


settings = Settings()
