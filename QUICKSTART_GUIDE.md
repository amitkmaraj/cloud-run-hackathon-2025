# 🚀 Cloud Run Hackathon - Quick Start Guide

**Get your AI agent running in 30 minutes!**

## ⚡ Prerequisites (5 minutes)

```bash
# 1. Set your project ID
export PROJECT_ID="your-project-id"
gcloud config set project $PROJECT_ID

# 2. Enable APIs
gcloud services enable run.googleapis.com cloudbuild.googleapis.com
```

## 🤖 Deploy Gemma LLM (10 minutes)

```bash
# 1. Deploy Gemma 3-4B directly to Cloud Run with one command
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

# 2. Get your Gemma URL
export GEMMA_URL=$(gcloud run services describe gemma-service --region=us-central1 --format='value(status.url)')
echo "🎉 Gemma deployed at: $GEMMA_URL"
```

## 🛠️ Deploy Your Agent (10 minutes)

```bash
# 1. Download the complete agent files
mkdir hackathon-agent && cd hackathon-agent
curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/main/hackathon-templates/agent.py
curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/main/hackathon-templates/server.py
curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/main/hackathon-templates/Dockerfile
curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/main/hackathon-templates/pyproject.toml

# 2. Deploy to Cloud Run
gcloud run deploy hackathon-agent \
    --source . \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars GEMMA_URL=$GEMMA_URL

# 3. Get your agent URL
export AGENT_URL=$(gcloud run services describe hackathon-agent --region=us-central1 --format='value(status.url)')
echo "🎉 Agent deployed at: $AGENT_URL"
```

## ✅ Test Everything Works (5 minutes)

```bash
# Test your agent
curl -X POST "$AGENT_URL/api/tools/research_topic" \
  -H "Content-Type: application/json" \
  -d '{"topic": "artificial intelligence", "focus": "technical"}'

# Visit the web interface
echo "🌐 Open your agent at: $AGENT_URL/adk"
```

## 🎯 Next Steps

1. **Customize your agent** - Edit `agent.py` to add your own tools
2. **Test locally** - Set `GEMMA_URL` and run `uv run python server.py`
3. **Add features** - Extend with new capabilities for your domain
4. **Build something amazing!** 🚀

## 🆘 Need Help?

- Check the full [HACKATHON_TUTORIAL.md](./HACKATHON_TUTORIAL.md) for detailed instructions
- Visit `$AGENT_URL/docs` to see your agent's API documentation
- Ask mentors for help with deployment issues

**Ready to hack!** 🎉
