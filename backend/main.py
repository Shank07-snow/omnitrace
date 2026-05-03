from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import datetime

app = FastAPI(title="OmniTrace Backend")

class TraceEvent(BaseModel):
    agent_id: str
    run_id: str
    prompt: str
    response: str
    timestamp: datetime.datetime = datetime.datetime.now()

traces = []

@app.post("/ingest")
async def ingest_trace(event: TraceEvent):
    traces.append(event)
    # In the future, we will broadcast this to the Next.js frontend via WebSockets
    return {"status": "success", "recorded": True}

@app.get("/traces")
async def get_traces():
    return {"traces": traces}