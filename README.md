# 🚀 Cloud Run Hackathon: Build and Deploy AI Agents

Welcome to the ultimate Cloud Run hackathon experience! This repository contains everything you need to build, deploy, and showcase AI agents on Google Cloud Run with GPU acceleration.

## 🎯 What You'll Build

By the end of this hackathon, you'll have:

- ✅ **Deployed an LLM** (Gemma 3) to Cloud Run with GPU acceleration
- ✅ **Built a custom AI agent** using the Agent Development Kit (ADK)
- ✅ **Deployed your agent** to Cloud Run with full monitoring and observability
- ✅ **Created something amazing** that solves real-world problems

## 🚀 Quick Start (30 minutes)

**New to hackathons?** Start here: [**QUICKSTART_GUIDE.md**](./QUICKSTART_GUIDE.md)

**Want the full experience?** Follow the complete: [**HACKATHON_TUTORIAL.md**](./HACKATHON_TUTORIAL.md)

## 📚 Complete Guide Index

### 🎓 Learning Materials

- [**HACKATHON_TUTORIAL.md**](./HACKATHON_TUTORIAL.md) - Complete step-by-step tutorial
- [**QUICKSTART_GUIDE.md**](./QUICKSTART_GUIDE.md) - Get running in 30 minutes
- [**PARTICIPANT_RESOURCES.md**](./PARTICIPANT_RESOURCES.md) - Tools, examples, and references

### 🏆 Competition Details

- [**JUDGING_CRITERIA.md**](./JUDGING_CRITERIA.md) - How you'll be evaluated
- [**project-overview.md**](./project-overview.md) - Hackathon overview and requirements
- [**core-requirements.md**](./core-requirements.md) - The three core requirements

### 🛠️ Ready-to-Deploy Code

- [**hackathon-templates/**](./hackathon-templates/) - Complete working agent and deployment files
- [**researcher-agent/**](./researcher-agent/) - Example production-ready agent

## 🎯 Core Requirements

You must complete these three requirements to be eligible for prizes:

### 1. 🤖 Deploy LLM to Cloud Run with GPU

- Deploy Gemma 3 to Cloud Run using GPU acceleration
- Enable public access with `--allow-unauthenticated`
- Test and verify the deployment works

### 2. 🔧 Build Agent with ADK

- Create an AI agent using the Agent Development Kit
- Integrate with your deployed LLM
- Add custom tools and functionality

### 3. 🚀 Deploy Agent to Cloud Run

- Deploy your agent to Cloud Run
- Ensure it's accessible via ADK web interface
- Include monitoring and observability

## 🏅 Prizes & Recognition

### 🥇 Grand Prize: $2,000 + Cloud Credits

Best overall project across all categories

### 🥈 Cloud Run Excellence: $1,000 + Swag

Best use of Cloud Run features and GPU capabilities

### 🥉 Innovation Award: $500 + Mentorship

Most creative and novel application

### 🎖️ Special Recognition

- Best Beginner Project
- Best Team Collaboration
- Most Impactful Solution
- Best Technical Documentation

## 🛠️ Technology Stack

### Core Technologies

- **Google Cloud Run** - Serverless container platform
- **Cloud Run GPUs** - NVIDIA L4 GPU acceleration
- **Agent Development Kit (ADK)** - Google's agent framework
- **Gemma 3** - Google's lightweight LLM
- **Ollama** - Local LLM serving platform

### Optional Integrations

- **Gemini API** - Google's advanced AI models
- **Cloud Logging** - Application monitoring
- **Cloud Trace** - Performance monitoring
- **Streamlit/Gradio** - Web UI frameworks

## 🚀 Getting Started

### Prerequisites

```bash
# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash

# Authenticate and set project
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable run.googleapis.com cloudbuild.googleapis.com
```

### Option 1: Quick Start (30 minutes)

Perfect for getting up and running quickly:

```bash
# Deploy Gemma LLM with single command
export PROJECT_ID="your-project-id"
gcloud config set project $PROJECT_ID

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

# Deploy your agent
mkdir hackathon-agent && cd hackathon-agent
for file in agent.py server.py Dockerfile pyproject.toml; do
  curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/main/hackathon-templates/$file
done

export GEMMA_URL=$(gcloud run services describe gemma-service --region=us-central1 --format='value(status.url)')
gcloud run deploy hackathon-agent --source . --region us-central1 --allow-unauthenticated --set-env-vars GEMMA_URL=$GEMMA_URL
```

### Option 2: Complete Tutorial (1 hour)

For full understanding and customization:

```bash
# Follow the complete tutorial
open HACKATHON_TUTORIAL.md
```

## 🎨 Project Ideas

### 🔰 Beginner-Friendly

- **Smart FAQ Bot** - Answer questions about your domain
- **Content Summarizer** - Summarize articles, papers, or documents
- **Code Reviewer** - Analyze code and provide feedback
- **Meeting Assistant** - Process meeting notes and action items

### 🌟 Intermediate

- **Research Assistant** - Multi-step research with web search
- **Data Analyzer** - Process and visualize datasets
- **Creative Writer** - Generate stories, poems, or scripts
- **Language Tutor** - Interactive language learning

### 🚀 Advanced

- **Autonomous Workflow** - Chain multiple agents together
- **Multi-Modal Agent** - Process text, images, and audio
- **Real-Time Assistant** - Handle streaming data and events
- **Collaborative System** - Multiple agents working together

## 📊 Example Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Request  │ -> │  Your Agent     │ -> │  Gemma LLM      │
│                 │    │  (Cloud Run)    │    │  (Cloud Run+GPU)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              v
                       ┌─────────────────┐
                       │  External APIs  │
                       │  (Optional)     │
                       └─────────────────┘
```

## 🔍 What Makes a Winning Project?

### Technical Excellence (30%)

- ✅ All core requirements completed
- 🔧 Clean, well-structured code
- 🛡️ Proper error handling and security
- 📈 Performance optimization

### Innovation & Creativity (25%)

- 💡 Novel use of Cloud Run capabilities
- 🎨 Creative problem-solving
- 🌟 Unique features and functionality
- 🎯 Great user experience

### Cloud Run Utilization (20%)

- 🚀 Effective use of GPU capabilities
- 📊 Proper monitoring and observability
- ⚡ Smart scaling configuration
- 🏗️ Good architectural practices

### Real-World Impact (15%)

- 🎯 Solves actual problems
- 📈 Shows business value
- 🌍 Potential for production use
- 🔮 Future scalability

### Presentation & Demo (10%)

- 📱 Clear, engaging demonstration
- 🎤 Good communication skills
- 🎯 Effective use of time
- 🤝 Team coordination

## 🆘 Getting Help

### During the Hackathon

- **💬 Slack**: #cloud-run-hackathon channel
- **🙋 Mentors**: Available at help stations
- **⏰ Office Hours**: Scheduled Q&A sessions
- **📖 Documentation**: All guides in this repository

### Online Resources

- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [ADK Documentation](https://google.github.io/adk-docs/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/google-cloud-run)
- [Google Cloud Community](https://cloud.google.com/support/community)

## 📅 Timeline

### Day 1

- **Morning**: Setup and tutorials
- **Afternoon**: Core requirements implementation
- **Evening**: Technical review checkpoint

### Day 2

- **Morning**: Feature development and testing
- **Afternoon**: Presentations and demos
- **Evening**: Judging and awards ceremony

## 🎉 Success Stories

This hackathon builds on the success of previous Cloud Run events where participants have:

- 🚀 Built production-ready applications
- 💼 Started successful startups
- 🏆 Won major prizes and recognition
- 🤝 Formed lasting professional relationships

## 🌟 Community

### Join the Community

- **AI Tinkerers NYC** - Host community
- **Google Cloud Developers** - Technical community
- **Cloud Run Users** - Platform-specific community

### Stay Connected

- Follow [@GoogleCloud](https://twitter.com/GoogleCloud) on Twitter
- Join [Google Cloud Community](https://cloud.google.com/community)
- Subscribe to [Cloud Run Newsletter](https://cloud.google.com/run)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

**Organizers**

- Google Cloud Team
- AI Tinkerers NYC
- Cloud Run Engineering
- ADK Development Team

**Sponsors & Partners**

- Google Cloud
- NVIDIA
- Betaworks (Venue)

**Special Thanks**

- All mentors and volunteers
- Previous hackathon participants
- The open-source community

---

## 🚀 Ready to Start?

Choose your path:

1. **🏃 Quick Start** - [QUICKSTART_GUIDE.md](./QUICKSTART_GUIDE.md)
2. **📚 Complete Tutorial** - [HACKATHON_TUTORIAL.md](./HACKATHON_TUTORIAL.md)
3. **🛠️ Download Files** - All code is ready in [hackathon-templates/](./hackathon-templates/)

**Remember**: The best project is the one you actually finish and demo! Start simple, iterate quickly, and have fun building something amazing.

**Good luck, and may the best agent win!** 🏆

---

_Built with ❤️ by the Google Cloud and AI Tinkerers communities_
