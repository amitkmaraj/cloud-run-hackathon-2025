# Cloud Run Hackathon Tutorial: Build and Deploy AI Agents

Welcome to the Cloud Run Hackathon! This tutorial will guide you through building and deploying AI agents on Google Cloud Run, leveraging Cloud Run GPUs for model inference.

## 🎯 Hackathon Objectives

By the end of this hackathon, you will:

- Deploy an open-source LLM (Gemma 2B) to Cloud Run using GPU
- Build an AI agent using the Agent Development Kit (ADK)
- Deploy your agent to Cloud Run with full monitoring capabilities

## 📋 Prerequisites

- Google Cloud Project with billing enabled
- `gcloud` CLI installed and authenticated
- Basic knowledge of Python and APIs

## 🚀 Part 1: Deploy Gemma to Cloud Run with GPU

### Step 1: Set up your environment

```bash
# Set your project ID
export PROJECT_ID="your-project-id"
gcloud config set project $PROJECT_ID

# Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

### Step 2: Deploy Gemma with a single command

Google provides prebuilt Gemma containers that you can deploy directly:

```bash
# Deploy Gemma 3-4B to Cloud Run with GPU (takes 5-10 minutes)
gcloud run deploy gemma-service \
   --image us-docker.pkg.dev/cloudrun/container/gemma/gemma3-4b \
   --concurrency 4 \
   --cpu 8 \
   --set-env-vars OLLAMA_NUM_PARALLEL=4 \
   --gpu 1 \
   --gpu-type nvidia-l4 \
   --max-instances 1 \
   --memory 32Gi \
   --allow-unauthenticated \
   --no-cpu-throttling \
   --timeout=600 \
   --region us-central1
```

**Available models:**

- Gemma 3 1B: `--image us-docker.pkg.dev/cloudrun/container/gemma/gemma3-1b`
- Gemma 3 4B: `--image us-docker.pkg.dev/cloudrun/container/gemma/gemma3-4b` (recommended)
- Gemma 3 12B: `--image us-docker.pkg.dev/cloudrun/container/gemma/gemma3-12b`
- Gemma 3 27B: `--image us-docker.pkg.dev/cloudrun/container/gemma/gemma3-27b`

### Step 3: Get your Gemma URL

```bash
# Your Gemma URL
export GEMMA_URL=$(gcloud run services describe gemma-service --region=us-central1 --format='value(status.url)')
echo "Gemma URL: $GEMMA_URL"
```

### Step 4: Test your LLM deployment

```bash
# Test the API (wait 2-3 minutes for initialization)
curl -X POST $GEMMA_URL/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma3:4b",
    "prompt": "What is artificial intelligence?",
    "stream": false
  }'
```

## 🤖 Part 2: Deploy Your AI Agent

### Step 1: Download the complete agent

We've created a ready-to-deploy agent that integrates with your Gemma deployment:

```bash
# Create agent directory
mkdir hackathon-agent && cd hackathon-agent

# Download all required files
curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/main/hackathon-templates/agent.py
curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/main/hackathon-templates/server.py
curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/main/hackathon-templates/Dockerfile
curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/main/hackathon-templates/pyproject.toml
```

### Step 2: Understand your agent

The agent includes three main tools:

1. **`research_topic`** - Research any topic with different focus areas
2. **`analyze_trends`** - Analyze trends in technology, business, or science
3. **`ask_question`** - Ask any question to the AI

### Step 3: Deploy to Cloud Run

```bash
# Deploy your agent
gcloud run deploy hackathon-agent \
    --source . \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars GEMMA_URL=$GEMMA_URL

# Get your agent URL
export AGENT_URL=$(gcloud run services describe hackathon-agent --region=us-central1 --format='value(status.url)')
echo "Agent URL: $AGENT_URL"
```

### Step 4: Test your agent

```bash
# Test the research tool
curl -X POST "$AGENT_URL/api/tools/research_topic" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "artificial intelligence",
    "focus": "technical"
  }'

# Test the trend analysis tool
curl -X POST "$AGENT_URL/api/tools/analyze_trends" \
  -H "Content-Type: application/json" \
  -d '{
    "domain": "technology"
  }'

# Test the question tool
curl -X POST "$AGENT_URL/api/tools/ask_question" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "How do neural networks work?"
  }'
```

## 🎨 Part 3: Customize Your Agent

### Step 1: Test locally (optional)

```bash
# Install uv (if not already installed)
pip install uv

# Set your Gemma URL
export GEMMA_URL="your-gemma-service-url"

# Run locally
uv run python server.py
```

Visit `http://localhost:8080/adk` to test your agent locally.

### Step 2: Add your own tools

Edit `agent.py` to add custom tools. Here's an example:

```python
@tool
async def summarize_text(self, text: str) -> str:
    """
    Summarize any text using the deployed Gemma model.

    Args:
        text: Text to summarize

    Returns:
        Summary of the text
    """

    prompt = f"""Please provide a concise summary of the following text:

Text: {text}

Please provide a clear and informative summary in 2-3 sentences."""

    logger.info(f"Summarizing text: {text[:50]}...")

    # Query the deployed Gemma model
    llm_response = await self.query_gemma(prompt, temperature=0.5)

    return f"# Text Summary\n\n{llm_response}\n\n---\n*Powered by Gemma 3 on Cloud Run*"
```

### Step 3: Redeploy with changes

```bash
# Redeploy your updated agent
gcloud run deploy hackathon-agent \
    --source . \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars GEMMA_URL=$GEMMA_URL
```

## 🔍 Part 4: Explore and Interact

### Web Interface

Visit your agent's web interface:

- **Agent Interface**: `$AGENT_URL/adk`
- **API Documentation**: `$AGENT_URL/docs`
- **Health Check**: `$AGENT_URL/health`

### API Examples

Your agent exposes REST endpoints for each tool:

```bash
# Research API
POST $AGENT_URL/api/tools/research_topic
{
  "topic": "quantum computing",
  "focus": "business"
}

# Trends API
POST $AGENT_URL/api/tools/analyze_trends
{
  "domain": "science"
}

# Question API
POST $AGENT_URL/api/tools/ask_question
{
  "question": "What are the benefits of serverless computing?"
}
```

## 📊 Part 5: Monitoring and Optimization

### View Logs

```bash
# Check agent logs
gcloud run services logs tail hackathon-agent --region=us-central1

# Check Gemma logs
gcloud run services logs tail gemma-service --region=us-central1
```

### Performance Monitoring

Your services automatically include:

- **Cloud Logging** - All requests and errors
- **Cloud Monitoring** - Performance metrics
- **Cloud Trace** - Request tracing

## 🎉 Congratulations!

You've successfully:

1. ✅ **Deployed Gemma to Cloud Run with GPU** - Your LLM is running with GPU acceleration
2. ✅ **Built and deployed an AI agent** - Your agent can interact with the deployed LLM
3. ✅ **Created a working AI application** - Your agent is accessible via web interface and API

## 🚀 Next Steps

### Extend Your Agent

- Add more sophisticated tools
- Integrate with external APIs
- Add conversation memory
- Implement user authentication

### Optimize Performance

- Configure auto-scaling
- Add caching layers
- Implement request batching
- Monitor resource usage

### Build Something Amazing

- Create a domain-specific assistant
- Build a research automation tool
- Develop a creative writing helper
- Design a data analysis agent

## 📚 Resources

- [Agent Code](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/hackathon-templates)
- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [ADK Documentation](https://google.github.io/adk-docs/)
- [Gemma Documentation](https://ai.google.dev/gemma)

## 🆘 Troubleshooting

### Common Issues

1. **Agent can't connect to Gemma**: Verify your `GEMMA_URL` environment variable
2. **Cold starts**: Set min-instances to 1 for both services
3. **Out of memory**: Increase memory allocation in deployment commands
4. **GPU quota**: Ensure you're using only 1 GPU per project

### Getting Help

- Check service logs: `gcloud run services logs tail SERVICE_NAME --region=us-central1`
- Visit Cloud Console for detailed monitoring
- Ask mentors for assistance during the hackathon

**Ready to build something amazing? Let's go!** 🚀
