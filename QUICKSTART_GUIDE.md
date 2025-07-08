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
# 1. Deploy Gemma 3-4B directly to Cloud Run with one command (secure by default)
gcloud run deploy gemma-service \
    --image us-docker.pkg.dev/cloudrun/container/gemma/gemma3n-e4b \
    --concurrency 4 \
    --cpu 8 \
    --set-env-vars OLLAMA_NUM_PARALLEL=4 \
    --set-env-vars=API_KEY={YOUR_API_KEY} \
    --gpu 1 \
    --gpu-type nvidia-l4 \
    --max-instances 1 \
    --memory 32Gi \
    --no-allow-unauthenticated \
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

# 2. Deploy to Cloud Run (secure by default)
gcloud run deploy hackathon-agent \
    --source . \
    --region us-central1 \
    --no-allow-unauthenticated \
    --set-env-vars GEMMA_URL=$GEMMA_URL

# 3. Get your agent URL
export AGENT_URL=$(gcloud run services describe hackathon-agent --region=us-central1 --format='value(status.url)')
echo "🎉 Agent deployed at: $AGENT_URL"
```

## 🔐 Authentication (Required for Testing)

Since your services are deployed securely (recommended), you need to authenticate to test them:

### Option 1: Command Line Testing

```bash
# 1. Get an authentication token
TOKEN=$(gcloud auth print-identity-token)

# 2. Test your agent with authentication
curl -H "Authorization: Bearer ${TOKEN}" \
  -X POST "$AGENT_URL/api/tools/research_topic" \
  -H "Content-Type: application/json" \
  -d '{"topic": "artificial intelligence", "focus": "technical"}'
```

### Option 2: Python Code (For Your Agent)

Your agent template is already set up to handle authentication automatically. If you want to modify it, here's how authentication works:

```python
import google.auth
import google.auth.transport.requests
from google.oauth2 import id_token
import requests

def get_id_token(cloud_run_url):
    """
    Generates an OIDC identity token for a given Cloud Run URL.
    """
    # Create an authentication request
    auth_req = google.auth.transport.requests.Request()

    # fetch_id_token will use the Application Default Credentials to get a token
    # for the specified audience.
    try:
        identity_token = id_token.fetch_id_token(auth_req, cloud_run_url)
        print("Successfully generated ID token.")
        return identity_token
    except Exception as e:
        print(f"Error generating ID token: {e}")
        return None

# Use the token in requests
token = get_id_token(GEMMA_URL)
headers = {
    "Authorization": f"Bearer {token}"
}

# Make the authenticated request
response = requests.get(cloud_run_url, headers=headers)
```

## ✅ Test Everything Works (5 minutes)

```bash
# Test your agent with authentication
TOKEN=$(gcloud auth print-identity-token)
curl -H "Authorization: Bearer ${TOKEN}" \
  -X POST "$AGENT_URL/api/tools/research_topic" \
  -H "Content-Type: application/json" \
  -d '{"topic": "artificial intelligence", "focus": "technical"}'

# Visit the web interface (you'll need to sign in with Google)
echo "🌐 Open your agent at: $AGENT_URL/adk"
```

## 🔓 Alternative: Public Access (Not Recommended)

If you prefer public access (less secure), you can redeploy with `--allow-unauthenticated`:

```bash
# Redeploy Gemma with public access
gcloud run deploy gemma-service \
   --image us-docker.pkg.dev/cloudrun/container/gemma/gemma3-4b \
   --allow-unauthenticated \
   --region us-central1

# Redeploy agent with public access
gcloud run deploy hackathon-agent \
    --source . \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars GEMMA_URL=$GEMMA_URL

# Test without authentication
curl -X POST "$AGENT_URL/api/tools/research_topic" \
  -H "Content-Type: application/json" \
  -d '{"topic": "artificial intelligence", "focus": "technical"}'
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
