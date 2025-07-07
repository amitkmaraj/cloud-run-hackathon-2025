3 Core Requirements

1. Deploy own LLM to cloud run using GPU
   1. Get a small model to work with (gemma 3n) and get hackers to deploy it to Cloud Run using a Cloud Run GPU.
   2. Make sure this deployment has the `--allow-unauthenticated` flag so it can be interacted with easily.
2. Interact with LLM through a created Agent.
   1. Create an Agent using ADK and have it interact with the deployed LLM instance (through the above Cloud Run url)
3. Deploy agent to cloud run
   1. Deploy the developed Agent to Cloud Run and ensure it is working through adk web.
