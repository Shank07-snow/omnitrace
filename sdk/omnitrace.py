import requests
import uuid

class OmniTrace:
    def __init__(self, backend_url="http://localhost:8000"):
        self.backend_url = backend_url
        self.run_id = str(uuid.uuid4())

    def wrap_llm_call(self, agent_id, prompt, llm_function, *args, **kwargs):
        print(f"[OmniTrace] Intercepting call for {agent_id}...")
        response = llm_function(prompt, *args, **kwargs)
        event = {
            "agent_id": agent_id,
            "run_id": self.run_id,
            "prompt": prompt,
            "response": str(response)
        }
        try:
            requests.post(f"{self.backend_url}/ingest", json=event)
        except Exception as e:
            print(f"[OmniTrace] Failed to log trace: {e}")
        return response