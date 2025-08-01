from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal, Any, Optional
from agent.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Initialize the graph once at startup for better performance
print("Initializing travel agent...")
travel_graph = None

@app.on_event("startup")
async def startup_event():
    global travel_graph
    try:
        print("Building GraphBuilder...")
        graph_builder = GraphBuilder(model_provider="groq")
        print("Compiling graph...")
        travel_graph = graph_builder()
        print("Travel agent initialized successfully!")
    except Exception as e:
        print(f"Failed to initialize travel agent: {e}")

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    global travel_graph
    try:
        if travel_graph is None:
            return JSONResponse(status_code=503, content={"error": "Travel agent is not initialized yet"})
        
        print(f"Processing query: {query.question}")
        messages = {"messages": [query.question]}
        output = travel_graph.invoke(messages)
        print("Query processed successfully")

        if isinstance(output, dict) and "messages" in output:
            response = output["messages"][-1].content
        else:
            response = str(output)

        return {"answer": response}
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/")
async def root():
    return {"message": "Travel Agent API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is working properly"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

