# 📚 Cloud Run Hackathon - Participant Resources

## 🚀 Quick Links

### Essential Documentation

- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [ADK Documentation](https://google.github.io/adk-docs/)
- [Cloud Run GPU Guide](https://cloud.google.com/run/docs/configuring/services/gpu)
- [Gemma on Cloud Run](https://cloud.google.com/run/docs/run-gemma-on-cloud-run)

### Hackathon Materials

- [Tutorial](./HACKATHON_TUTORIAL.md) - Complete step-by-step guide
- [Quick Start](./QUICKSTART_GUIDE.md) - 30-minute setup
- [Judging Criteria](./JUDGING_CRITERIA.md) - How you'll be evaluated
- [Template Repository](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/hackathon-templates)

## 🛠️ Development Tools

### Required Tools

```bash
# Google Cloud SDK
curl https://sdk.cloud.google.com | bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Docker (for local testing)
# Installation varies by OS - see https://docs.docker.com/get-docker/

# Python environment
pip install uv  # Fast Python package manager
```

### Recommended IDEs

- **VS Code**: With Cloud Code extension
- **PyCharm**: Professional or Community edition
- **Cloud Shell**: Browser-based development environment
- **Cursor**: AI-powered development environment

### Helpful Extensions

- **Cloud Code**: Deploy directly from VS Code
- **Docker**: Container management
- **Python**: Language support and debugging
- **REST Client**: API testing

## 🤖 Agent Development Kit (ADK)

### Core Concepts

```python
from adk import BaseAgent, tool, create_adk_app

class MyAgent(BaseAgent):
    @tool
    async def my_tool(self, input: str) -> str:
        """Tool description for the agent"""
        return f"Processed: {input}"

agent = MyAgent()
app = create_adk_app(agent)
```

### ADK Features

- **Tools**: Define agent capabilities
- **Routing**: Handle different conversation flows
- **Validation**: Automatic input validation
- **Logging**: Built-in monitoring and debugging
- **Web Interface**: Interactive agent testing

### Example Tools

```python
@tool
async def web_search(self, query: str) -> str:
    """Search the web for information"""
    # Implementation here
    pass

@tool
async def analyze_data(self, data: Dict) -> Dict:
    """Analyze structured data"""
    # Implementation here
    pass

@tool
async def generate_image(self, prompt: str) -> str:
    """Generate image from text prompt"""
    # Implementation here
    pass
```

## 🔧 Cloud Run Configuration

### Basic Deployment

```bash
gcloud run deploy my-service \
    --source . \
    --region us-central1 \
    --allow-unauthenticated
```

### Advanced Configuration

```bash
gcloud run deploy my-service \
    --source . \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 4Gi \
    --cpu 2 \
    --concurrency 10 \
    --max-instances 100 \
    --min-instances 1 \
    --set-env-vars KEY=VALUE,KEY2=VALUE2 \
    --set-secrets SECRET_KEY=secret_name:latest
```

### GPU Configuration

```bash
gcloud run deploy gpu-service \
    --source . \
    --region us-central1 \
    --allow-unauthenticated \
    --gpu 1 \
    --gpu-type nvidia-l4 \
    --memory 8Gi \
    --cpu 4
```

## 🧠 LLM Integration Examples

### Ollama Integration

```python
import httpx

async def query_ollama(prompt: str, model: str = "gemma2:2b"):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]
```

### Gemini API Integration

```python
import google.generativeai as genai

def query_gemini(prompt: str):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text
```

### OpenAI Compatible API

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://your-service-url/v1",
    api_key="not-needed"
)

response = client.chat.completions.create(
    model="gemma2:2b",
    messages=[{"role": "user", "content": prompt}]
)
```

## 📊 Monitoring and Observability

### Cloud Logging

```python
import logging
from google.cloud import logging as cloud_logging

# Setup Cloud Logging
cloud_logging.Client().setup_logging()
logger = logging.getLogger(__name__)

# Use in your code
logger.info("Processing request", extra={"user_id": "123"})
```

### Cloud Trace

```python
from google.cloud import trace_v1

def trace_function():
    tracer = trace_v1.TraceServiceClient()
    # Add tracing to your functions
    pass
```

### Custom Metrics

```python
from google.cloud import monitoring_v3

def record_metric(value: float, metric_type: str):
    client = monitoring_v3.MetricServiceClient()
    # Record custom metrics
    pass
```

## 🎨 Frontend Integration

### React Example

```jsx
import React, { useState } from "react";

function AgentChat() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await fetch("/api/tools/research_with_llm", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic: message, focus: "general" }),
    });
    const data = await res.json();
    setResponse(data.result);
  };

  return (
    <div>
      <input value={message} onChange={(e) => setMessage(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
      <div>{response}</div>
    </div>
  );
}
```

### Streamlit Example

```python
import streamlit as st
import requests

st.title("My AI Agent")

user_input = st.text_input("Ask me anything:")
if st.button("Submit"):
    response = requests.post(
        f"{AGENT_URL}/api/tools/research_with_llm",
        json={"topic": user_input, "focus": "general"}
    )
    st.write(response.json()["result"])
```

## 🔒 Security Best Practices

### Environment Variables

```bash
# Set sensitive data as environment variables
gcloud run deploy my-service \
    --set-env-vars DATABASE_URL=postgresql://... \
    --set-secrets API_KEY=my-secret:latest
```

### Input Validation

```python
from pydantic import BaseModel, validator

class UserInput(BaseModel):
    query: str

    @validator('query')
    def validate_query(cls, v):
        if len(v) > 1000:
            raise ValueError('Query too long')
        return v.strip()
```

### Rate Limiting

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/query")
@limiter.limit("10/minute")
async def query_endpoint(request: Request):
    # Your endpoint logic
    pass
```

## 🧪 Testing and Debugging

### Unit Testing

```python
import pytest
from agent import HackathonAgent

@pytest.fixture
def agent():
    return HackathonAgent("http://localhost:11434")

async def test_research_tool(agent):
    result = await agent.research_with_llm(
        ResearchQuery(topic="AI", focus="technical")
    )
    assert "Research Analysis" in result
```

### Load Testing

```python
from locust import HttpUser, task

class AgentUser(HttpUser):
    @task
    def test_research(self):
        self.client.post("/api/tools/research_with_llm", json={
            "topic": "artificial intelligence",
            "focus": "technical"
        })
```

### Local Development

```bash
# Run locally with hot reload
uvicorn agent:app --reload --host 0.0.0.0 --port 8080

# Test with curl
curl -X POST http://localhost:8080/api/tools/research_with_llm \
  -H "Content-Type: application/json" \
  -d '{"topic": "AI", "focus": "technical"}'
```

## 📱 Multi-Modal Capabilities

### Image Processing

```python
import base64
from PIL import Image
import io

@tool
async def analyze_image(self, image_data: str) -> str:
    """Analyze an uploaded image"""
    # Decode base64 image
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))

    # Process image and return analysis
    return "Image analysis results"
```

### Audio Processing

```python
import speech_recognition as sr

@tool
async def transcribe_audio(self, audio_file: bytes) -> str:
    """Transcribe audio to text"""
    recognizer = sr.Recognizer()
    # Process audio and return transcription
    return "Transcribed text"
```

## 🌐 External Integrations

### Database Integration

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@tool
async def query_database(self, query: str) -> str:
    """Query the database"""
    session = Session()
    # Execute query and return results
    return "Query results"
```

### API Integrations

```python
import httpx

@tool
async def call_external_api(self, endpoint: str, params: dict) -> dict:
    """Call external API"""
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint, params=params)
        return response.json()
```

## 📊 Performance Optimization

### Caching

```python
from functools import lru_cache
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

@lru_cache(maxsize=128)
def expensive_computation(input_data: str) -> str:
    # Expensive computation
    return result
```

### Async Processing

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def process_multiple_requests(requests: List[str]):
    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        tasks = [
            loop.run_in_executor(executor, process_request, req)
            for req in requests
        ]
        results = await asyncio.gather(*tasks)
    return results
```

## 🎯 Project Ideas

### Beginner Projects

1. **Research Assistant**: Query and summarize information on topics
2. **Code Reviewer**: Analyze code and provide feedback
3. **Meeting Summarizer**: Process meeting transcripts and create summaries
4. **FAQ Bot**: Answer common questions about your domain

### Intermediate Projects

1. **Multi-Modal Analysis**: Combine text, image, and audio processing
2. **Workflow Automation**: Chain multiple tools together
3. **Data Visualization**: Create charts and graphs from data
4. **Content Generator**: Create articles, reports, or documentation

### Advanced Projects

1. **Autonomous Agent**: Make decisions and take actions independently
2. **Real-time Processing**: Handle streaming data and events
3. **Collaborative Agents**: Multiple agents working together
4. **Learning Agent**: Adapt and improve over time

## 🆘 Troubleshooting

### Common Issues

**Deployment Failures**

```bash
# Check logs
gcloud run services logs tail my-service --region us-central1

# Check service status
gcloud run services describe my-service --region us-central1
```

**GPU Issues**

```bash
# Check GPU quota
gcloud compute project-info describe --project=YOUR_PROJECT_ID

# Verify GPU configuration
gcloud run services describe my-service --region us-central1 --format="value(spec.template.spec.template.spec.containerConcurrency)"
```

**Connection Issues**

```bash
# Test connectivity
curl -I https://your-service-url.run.app

# Check firewall rules
gcloud compute firewall-rules list
```

### Getting Help

**During the Hackathon**

- **Slack**: #cloud-run-hackathon channel
- **Mentors**: Available at designated help stations
- **Office Hours**: Scheduled Q&A sessions

**Google Cloud Support**

- [Stack Overflow](https://stackoverflow.com/questions/tagged/google-cloud-run)
- [Community Forums](https://cloud.google.com/support/community)
- [Documentation](https://cloud.google.com/run/docs)

## 📈 Success Tips

1. **Start Simple**: Get the basic requirements working first
2. **Iterate Quickly**: Make small, frequent improvements
3. **Test Early**: Don't wait until the end to test your deployment
4. **Document Everything**: Good documentation impresses judges
5. **Practice Demo**: Prepare for technical difficulties during presentation
6. **Use Templates**: Leverage provided templates and examples
7. **Ask Questions**: Don't hesitate to ask mentors for help
8. **Have Fun**: Enjoy the process and learn something new!

## 🎉 Post-Hackathon

### Continuing Development

- Keep building on your project
- Contribute to open source
- Share your learnings with the community
- Consider turning your project into a startup

### Staying Connected

- Join the AI Tinkerers community
- Follow Google Cloud on social media
- Subscribe to Cloud Run newsletters
- Participate in future hackathons

Good luck with your hackathon project! 🚀
