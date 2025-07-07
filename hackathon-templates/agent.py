"""
Cloud Run Hackathon Agent - Ready to Deploy!

This is a complete working agent that integrates with your deployed Gemma model.
You can use this as-is or customize it for your specific use case.
"""

import os
import logging
from typing import Optional

import httpx
from adk import (
    BaseAgent,
    BaseModel,
    Field,
    create_adk_app,
    logger,
    tool,
)

# Configure logging
logging.basicConfig(level=logging.INFO)

class ResearchQuery(BaseModel):
    """Model for research queries"""
    topic: str = Field(description="The research topic to investigate")
    focus: str = Field(default="general", description="Focus area: general, technical, business, social")

class TrendAnalysis(BaseModel):
    """Model for trend analysis"""
    domain: str = Field(description="Domain to analyze: technology, business, science")

class HackathonAgent(BaseAgent):
    """
    AI Agent for the Cloud Run Hackathon
    
    This agent demonstrates how to integrate with a deployed LLM on Cloud Run
    and provides useful research and analysis capabilities.
    """
    
    def __init__(self, gemma_url: str):
        super().__init__()
        self.gemma_url = gemma_url.rstrip('/')
        self.client = httpx.AsyncClient(timeout=30.0)
        
    async def query_gemma(self, prompt: str, temperature: float = 0.7) -> str:
        """Query the deployed Gemma model"""
        try:
            request_data = {
                "model": "gemma3:4b",
                "prompt": prompt,
                "stream": False,
                "temperature": temperature
            }
            
            logger.info(f"Querying Gemma at {self.gemma_url}")
            response = await self.client.post(
                f"{self.gemma_url}/api/generate",
                json=request_data,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            
            result = response.json()
            return result.get("response", "No response from model")
            
        except httpx.HTTPError as e:
            logger.error(f"Error querying Gemma: {e}")
            return f"Error connecting to LLM: {str(e)}"
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return f"Unexpected error: {str(e)}"
    
    @tool
    async def research_topic(self, query: ResearchQuery) -> str:
        """
        Research any topic using the deployed Gemma model.
        
        Args:
            query: Research query with topic and focus area
            
        Returns:
            Comprehensive research analysis
        """
        
        prompt = f"""You are a knowledgeable research assistant. Provide a comprehensive analysis of the following topic:

Topic: {query.topic}
Focus: {query.focus}

Please structure your response with:
1. Overview and key concepts
2. Current state and developments
3. Key challenges and opportunities
4. Future outlook and trends

Keep your response informative and well-organized (under 400 words)."""
        
        logger.info(f"Researching topic: {query.topic} with focus: {query.focus}")
        
        # Query the deployed Gemma model
        llm_response = await self.query_gemma(prompt, temperature=0.7)
        
        # Format the response
        formatted_response = f"""# Research Analysis: {query.topic}

**Focus Area:** {query.focus}

{llm_response}

---
*Research powered by Gemma 3 on Cloud Run*"""
        
        return formatted_response
    
    @tool
    async def analyze_trends(self, analysis: TrendAnalysis) -> str:
        """
        Analyze trends in any domain using the deployed Gemma model.
        
        Args:
            analysis: Trend analysis request with domain
            
        Returns:
            Detailed trend analysis
        """
        
        prompt = f"""You are a trend analyst. Provide a comprehensive trend analysis for the {analysis.domain} domain.

Please structure your analysis with:
1. Top 3 current trends
2. Emerging patterns and innovations
3. Market impacts and opportunities
4. Predictions for the next 2-3 years

Keep your response focused and actionable (under 350 words)."""
        
        logger.info(f"Analyzing trends in domain: {analysis.domain}")
        
        # Query the deployed Gemma model
        llm_response = await self.query_gemma(prompt, temperature=0.8)
        
        # Format the response
        formatted_response = f"""# Trend Analysis: {analysis.domain}

{llm_response}

---
*Analysis powered by Gemma 3 on Cloud Run*"""
        
        return formatted_response
    
    @tool
    async def ask_question(self, question: str) -> str:
        """
        Ask any question to the AI agent.
        
        Args:
            question: Your question
            
        Returns:
            AI-generated response
        """
        
        prompt = f"""You are a helpful AI assistant. Please answer the following question clearly and informatively:

Question: {question}

Please provide a helpful, accurate, and well-structured response."""
        
        logger.info(f"Answering question: {question}")
        
        # Query the deployed Gemma model
        llm_response = await self.query_gemma(prompt, temperature=0.6)
        
        # Format the response
        formatted_response = f"""# AI Assistant Response

**Question:** {question}

{llm_response}

---
*Powered by Gemma 3 on Cloud Run*"""
        
        return formatted_response

# Create the agent instance
def create_agent():
    """Create and configure the agent"""
    gemma_url = os.getenv("GEMMA_URL")
    if not gemma_url:
        raise ValueError("GEMMA_URL environment variable is required. Please set it to your deployed Gemma service URL.")
    
    return HackathonAgent(gemma_url)

# Create the ADK app
agent = create_agent()
app = create_adk_app(agent)

# Add health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "hackathon-agent"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port) 