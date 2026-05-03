import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sdk.omnitrace import OmniTrace

tracer = OmniTrace(backend_url="http://localhost:8000")

def dummy_llm(prompt):
    return f"Simulated AI response to: {prompt}"

if __name__ == "__main__":
    print("Running dummy agent...")
    response = tracer.wrap_llm_call(
        agent_id="agent_alpha",
        prompt="What is the capital of France?",
        llm_function=dummy_llm
    )
    print("Final Response:", response)