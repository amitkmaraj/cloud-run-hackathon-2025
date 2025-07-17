# 🚀 Agentic AI App Hackathon with Google Cloud Run GPUs

Welcome to the **Agentic AI App Hackathon with Google Cloud Run GPUs**! Join us for a two-day hackathon event to build and deploy your own agentic applications on Google Cloud with Cloud Run, leveraging open models hosted on Cloud Run's serverless NVIDIA L4 GPUs.

## 📅 Event Details

**When:** July 19-20, 2025 (Saturday-Sunday)  
**Location:** 29 Little W 12th St, New York, NY  
**Host:** AI Tinkerers NYC

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

## 🎯 Core Requirements

You must complete these three requirements to be eligible for judging:

### 1. 🤖 Deploy LLM to Cloud Run with GPU

- Deploy one of the supported models (Gemma 3, DeepSeek-r1, Llama 2, SDXL, etc.) to Cloud Run using GPU acceleration
- Use secure authentication (recommended) or public access
- Test and verify the deployment works

### 2. 🔧 Build an Agentic Application

- Create an agentic AI application using any framework (ADK, LangChain, CrewAI, etc.)
- Integrate with your deployed LLM or other AI services
- Add autonomous behavior and decision-making capabilities
- Focus on solving real-world problems

### 3. 🚀 Deploy Application to Cloud Run

- Deploy your agentic application to Cloud Run
- Ensure it's accessible via web interface or API
- Include monitoring and observability

## 📅 Schedule

### Day 1 - July 19 (Saturday)

| Time              | Activity                                         |
| ----------------- | ------------------------------------------------ |
| 8:00 AM           | Doors open · Registration                        |
| 9:00 AM           | Opening and Cloud Run Serverless GPU walkthrough |
| 10:00 AM          | Team-formation lock-in Session                   |
| 12:00 PM          | Lunch                                            |
| 1:00 PM - 6:00 PM | Mentoring available (sponsors & judges)          |
| 6:00 PM           | Dinner break                                     |
| 8:00 PM           | Day-one doors close                              |

### Day 2 - July 20 (Sunday)

| Time     | Activity                                                                                       |
| -------- | ---------------------------------------------------------------------------------------------- |
| 8:00 AM  | Doors open                                                                                     |
| 9:00 AM  | Breakfast & networking                                                                         |
| 10:00 AM | Project submission deadline · Judging starts (live demos from teams who make the final rounds) |
| 1:15 PM  | Awards & closing ceremony                                                                      |
| 2:00 PM  | Farewell networking                                                                            |

## 🛠️ Technology Stack

### Core Technologies

- **Google Cloud Run** - Serverless container platform
- **Cloud Run GPUs** - NVIDIA L4 GPU acceleration
- **Serverless AI Models** - Gemma 3, DeepSeek-r1, Llama 2, SDXL, and more
- **Agentic Frameworks** - Build autonomous, decision-making applications

### Agent Frameworks (Choose One)

- **Agent Development Kit (ADK)** - Google's agent framework
- **LangChain** - Popular Python framework for LLM applications
- **CrewAI** - Multi-agent orchestration framework
- **AutoGen** - Microsoft's multi-agent conversation framework
- **Custom Framework** - Build your own agent system

### Optional Integrations

- **Gemini API** - Google's advanced AI models
- **Cloud Logging** - Application monitoring
- **Cloud Trace** - Performance monitoring
- **Streamlit/Gradio** - Web UI frameworks

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

## 🔍 What Makes a Winning Project?

### Technical Excellence (30%)

- ✅ All core requirements completed
- 🔧 Clean, well-structured code
- 🛡️ Proper error handling and security
- 📈 Performance optimization
- 🤖 Effective use of agentic capabilities

### Innovation & Creativity (25%)

- 💡 Novel use of Cloud Run GPU capabilities
- 🎨 Creative problem-solving
- 🌟 Unique agentic behaviors and functionality
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

- **🙋 Mentors**: Available July 19, 1:00 PM - 6:00 PM
- **👥 Sponsors & Judges**: On-site support and guidance
- **📖 Documentation**: All guides in this repository
- **🤝 Team Formation**: Saturday morning lock-in session

### Online Resources

- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Gemma on Cloud Run Cookbook](https://github.com/google-gemini/gemma-cookbook/blob/main/Demos/Gemma-on-Cloudrun/README.md) - Complete guide to deploying different Gemma models on Cloud Run
- [ADK Documentation](https://google.github.io/adk-docs/)
- [LangChain Documentation](https://python.langchain.com/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/google-cloud-run)
- [Google Cloud Community](https://cloud.google.com/support/community)

## 🎉 Success Stories

This hackathon builds on the success of previous Cloud Run events where participants have:

- 🚀 Built production-ready agentic applications
- 💼 Started successful AI-powered startups
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

- AI Tinkerers NYC
- Google Cloud Team
- Cloud Run Engineering

**Sponsors & Partners**

- Google Cloud
- NVIDIA
- AI Tinkerers NYC Community

**Special Thanks**

- All mentors and volunteers
- Previous hackathon participants
- The open-source community

---

## 🚀 Ready to Start?

**Get started now**: [QUICKSTART_GUIDE.md](./QUICKSTART_GUIDE.md)

**Remember**: The best project is the one you actually finish and demo! Start simple, iterate quickly, and have fun building something amazing with agentic AI.

**Good luck, and may the best agentic application win!** 🏆

---

_Built with ❤️ by the AI Tinkerers NYC and Google Cloud communities_
