# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import asyncio
from pathlib import Path
from typing import Dict, Any

import httpx
import google.auth
import google.auth.transport.requests
from google.oauth2 import id_token
from dotenv import load_dotenv
from google.adk.agents import Agent

# Load environment variables from .env file in root directory
root_dir = Path(__file__).parent.parent
dotenv_path = root_dir / ".env"
load_dotenv(dotenv_path=dotenv_path)


class GemmaClient:
    """Client for interacting with the deployed Gemma model."""

    def __init__(self, gemma_url: str):
        self.gemma_url = gemma_url.rstrip('/')
        self.client = httpx.AsyncClient(timeout=30.0)

    async def get_auth_headers(self) -> Dict[str, str]:
        """Get authentication headers for Cloud Run service-to-service calls."""
        headers = {"Content-Type": "application/json"}
        
        # Try to get identity token for authenticated requests
        try:
            auth_req = google.auth.transport.requests.Request()
            identity_token = id_token.fetch_id_token(auth_req, self.gemma_url)
            headers["Authorization"] = f"Bearer {identity_token}"
        except Exception:
            # If authentication fails, proceed without auth (for local testing)
            pass
            
        return headers

    async def query_gemma(self, prompt: str, temperature: float = 0.7) -> str:
        """Query the deployed Gemma model."""
        try:
            request_data = {
                "model": "gemma3:4b",
                "prompt": prompt,
                "stream": False,
                "temperature": temperature
            }
            
            headers = await self.get_auth_headers()
            
            response = await self.client.post(
                f"{self.gemma_url}/api/generate",
                json=request_data,
                headers=headers
            )
            response.raise_for_status()
            
            result = response.json()
            return result.get("response", "No response from model")
            
        except Exception as e:
            return f"Error querying Gemma: {str(e)}"

    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()


# Global Gemma client instance
gemma_client = None


def get_gemma_client() -> GemmaClient:
    """Get or create the Gemma client instance."""
    global gemma_client
    if gemma_client is None:
        gemma_url = os.getenv("GEMMA_URL")
        if not gemma_url:
            raise ValueError("GEMMA_URL environment variable is required")
        gemma_client = GemmaClient(gemma_url)
    return gemma_client


def ask_gemma(question: str, context: str = "") -> Dict[str, Any]:
    """Ask a question to the deployed Gemma model.

    Args:
        question (str): The question to ask
        context (str): Optional context to provide with the question

    Returns:
        Dict[str, Any]: Response from Gemma with status information
    """
    try:
        client = get_gemma_client()
        
        # Build the prompt
        if context:
            prompt = f"Context: {context}\n\nQuestion: {question}\n\nPlease provide a helpful and informative answer."
        else:
            prompt = f"Question: {question}\n\nPlease provide a helpful and informative answer."
        
        # Since we're in a synchronous function, we need to run the async query
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            response = loop.run_until_complete(client.query_gemma(prompt, temperature=0.7))
        finally:
            loop.close()
        
        return {
            "status": "success",
            "question": question,
            "answer": response,
            "context_provided": bool(context)
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Failed to query Gemma: {str(e)}",
            "question": question
        }


def generate_code(description: str, language: str = "python") -> Dict[str, Any]:
    """Generate code based on a description using Gemma.

    Args:
        description (str): Description of what the code should do
        language (str): Programming language (default: python)

    Returns:
        Dict[str, Any]: Generated code with explanation
    """
    try:
        client = get_gemma_client()
        
        prompt = f"""Please generate {language} code based on this description:

{description}

Please provide:
1. Clean, well-commented code
2. A brief explanation of how it works
3. Any important notes or considerations

Format your response with the code in a code block and explanation afterwards."""
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            response = loop.run_until_complete(client.query_gemma(prompt, temperature=0.5))
        finally:
            loop.close()
        
        return {
            "status": "success",
            "description": description,
            "language": language,
            "generated_code": response
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Failed to generate code: {str(e)}",
            "description": description
        }


def brainstorm_ideas(topic: str, num_ideas: int = 5) -> Dict[str, Any]:
    """Brainstorm creative ideas for a given topic using Gemma.

    Args:
        topic (str): The topic to brainstorm ideas for
        num_ideas (int): Number of ideas to generate (default: 5)

    Returns:
        Dict[str, Any]: List of brainstormed ideas
    """
    try:
        client = get_gemma_client()
        
        prompt = f"""Please brainstorm {num_ideas} creative and practical ideas for: {topic}

For each idea, provide:
1. A clear title
2. A brief description
3. Why it would be useful or interesting

Format your response as a numbered list with clear structure."""
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            response = loop.run_until_complete(client.query_gemma(prompt, temperature=0.8))
        finally:
            loop.close()
        
        return {
            "status": "success",
            "topic": topic,
            "requested_ideas": num_ideas,
            "ideas": response
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Failed to brainstorm ideas: {str(e)}",
            "topic": topic
        }


def explain_concept(concept: str, level: str = "intermediate") -> Dict[str, Any]:
    """Explain a concept at different levels of complexity.

    Args:
        concept (str): The concept to explain
        level (str): Complexity level - "beginner", "intermediate", or "advanced"

    Returns:
        Dict[str, Any]: Explanation tailored to the specified level
    """
    try:
        client = get_gemma_client()
        
        level_descriptions = {
            "beginner": "as if explaining to someone new to the field, using simple language and analogies",
            "intermediate": "assuming some background knowledge, with moderate technical detail",
            "advanced": "with comprehensive technical depth and nuance"
        }
        
        level_desc = level_descriptions.get(level, level_descriptions["intermediate"])
        
        prompt = f"""Please explain the concept of "{concept}" {level_desc}.

Structure your explanation with:
1. A clear definition
2. Key characteristics or components
3. Real-world examples or applications
4. Why it's important or relevant

Keep the explanation engaging and informative."""
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            response = loop.run_until_complete(client.query_gemma(prompt, temperature=0.6))
        finally:
            loop.close()
        
        return {
            "status": "success",
            "concept": concept,
            "level": level,
            "explanation": response
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Failed to explain concept: {str(e)}",
            "concept": concept
        }


# Create the ADK agent
root_agent = Agent(
    name="hackathon_agent",
    model="gemini-2.5-flash",
    instruction="""You are a helpful AI assistant designed for the Cloud Run Hackathon. 

You can help participants by:
1. Answering questions and providing information on various topics
2. Generating code in different programming languages
3. Brainstorming creative ideas for projects
4. Explaining complex concepts at different levels of detail

You have access to a deployed Gemma model that you can query for additional insights and information. Always try to be helpful, creative, and supportive of hackathon participants' goals.

Your tools connect to a deployed Gemma model, so you can provide rich, detailed responses powered by that model while maintaining the conversational interface through your own capabilities.""",
    tools=[ask_gemma, generate_code, brainstorm_ideas, explain_concept],
) 