# 🚀 Agentic AI App Hackathon with Google Cloud Run GPUs

Welcome to the **Agentic AI App Hackathon with Google Cloud Run GPUs**! Join us for a two-day hackathon event to build and deploy your own agentic applications on Google Cloud with Cloud Run, leveraging open models hosted on Cloud Run's serverless NVIDIA L4 GPUs.

---

## UPDATE Notice - Jul. 19 7:30PM

The agent now supports the connection to the deployed Gemma service, utilizing the python requests library. Feel free to take a look at the changes through the following commits and integrate within your agentic application. Good luck! 

Commit: [Update to use python requests package](https://github.com/amitkmaraj/cloud-run-hackathon-2025/commit/6c52d13808a5d74acfd0eb4b49b1f87e7198b3e4)
Commit: [Update the payload and URL](https://github.com/amitkmaraj/cloud-run-hackathon-2025/commit/102d4567eaba1d2e2bbf43680974dc26efd325f6)
Commit: [Update the Agent prompt to support the response from Gemma](https://github.com/amitkmaraj/cloud-run-hackathon-2025/commit/6f0c51bc99bf100cbf393e97d66f5b970783905e)

---

## 🎯 What You'll Build

Build and deploy agentic applications on Google Cloud with Cloud Run, leveraging these open models hosted on Cloud Run's serverless NVIDIA L4 GPUs:

- ✅ **Gemma 3** (1B/4B/12B) - Google's lightweight LLM
- ✅ **DeepSeek-r1 7B** - Advanced reasoning model
- ✅ **Llama 2 7B** - Meta's popular language model
- ✅ **Stable Diffusion XL (SDXL)** - Image generation model
- ✅ **And more open models** available on Cloud Run GPUs

**Each team gets one GPU allocated per Google Cloud project!**

## 🚀 Why Cloud Run GPUs?

Developers love Cloud Run, Google Cloud's serverless runtime, for its simplicity, flexibility, and scalability. Now, with NVIDIA L4 GPU support, Cloud Run offers a powerful environment for AI inference, perfectly suited for lightweight open models hosted directly on our serverless GPUs.

## 🛠️ Repository Contents

- [**QUICKSTART_GUIDE.md**](./QUICKSTART_GUIDE.md) - Get running in 30 minutes
- [**hackathon-agent/**](./hackathon-agent/) - Complete working agent and deployment files

## 🎨 Project Ideas

_Build agentic applications using any framework you prefer (ADK, LangChain, CrewAI, AutoGen, or your own)_

### 🔰 Beginner-Friendly

- **Autonomous Customer Support Agent** - AI that can handle complex inquiries and escalate when needed
- **Smart Content Moderator** - Agent that analyzes and categorizes content automatically
- **Intelligent Task Scheduler** - Agent that optimizes workflows and resource allocation
- **Adaptive Learning Assistant** - Agent that adjusts teaching methods based on student progress

### 🌟 Intermediate

- **Multi-Modal Research Agent** - Combines text, image, and data analysis capabilities
- **Autonomous Code Reviewer** - Agent that analyzes, tests, and suggests improvements
- **Dynamic Pricing Agent** - Real-time market analysis and pricing optimization
- **Intelligent Customer Journey Agent** - Personalizes experiences across touchpoints

### 🚀 Advanced

- **Autonomous Business Process Manager** - Orchestrates complex workflows across systems
- **Self-Healing Infrastructure Agent** - Monitors and automatically fixes system issues
- **Adaptive Security Agent** - Continuously learns and responds to threats
- **Collaborative Multi-Agent System** - Multiple specialized agents working together

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

### Online Resources

- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Gemma on Cloud Run Cookbook](https://github.com/google-gemini/gemma-cookbook/blob/main/Demos/Gemma-on-Cloudrun/README.md) - Complete guide to deploying different Gemma models on Cloud Run
- [ADK Documentation](https://google.github.io/adk-docs/)
- [LangChain Documentation](https://python.langchain.com/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/google-cloud-run)
- [Google Cloud Community](https://cloud.google.com/support/community)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🚀 Ready to Start?

**Get started now**: [QUICKSTART_GUIDE.md](./QUICKSTART_GUIDE.md)

**Remember**: The best project is the one you actually finish and demo! Start simple, iterate quickly, and have fun building something amazing with agentic AI.

**Good luck, and may the best agentic application win!** 🏆
