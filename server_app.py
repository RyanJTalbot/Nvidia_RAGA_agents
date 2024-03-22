# https://python.langchain.com/docs/langserve#server
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langserve import add_routes

llm = ChatNVIDIA(model="mixtral_8x7b")

app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    llm,
    path="/basic_chat",
)

## Might be encountered if this were for a standalone python file...
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9012)
