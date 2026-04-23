🔹 Project Title

Social-to-Lead Agentic Workflow – AutoStream AI Agent

🔹 Overview

This project implements a conversational AI agent for a SaaS product called AutoStream. The agent is capable of understanding user intent, answering product-related queries using a knowledge base, and capturing high-intent leads through a structured conversational workflow.

🔹 Features
Intent detection (greeting, pricing, high-intent)
RAG-based knowledge retrieval from local JSON
Multi-turn conversation with state management
Lead capture workflow
Controlled tool execution
🔹 Tech Stack
Python 3.11
LangGraph
LangChain (light usage)
JSON (knowledge base)
🔹 How to Run
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run
python main.py

🔹 Architecture

The system is built using LangGraph to model the conversational workflow as a directed graph. Each stage of the agent—intent detection, response generation, lead collection, and tool execution—is implemented as a separate node. The graph uses conditional routing based on detected user intent to decide the next step in the workflow.

A shared state object is used to maintain context across multiple conversation turns, enabling the agent to remember user inputs such as name, email, and platform. This ensures proper multi-turn interaction and prevents loss of context.

The agent uses a simple Retrieval-Augmented Generation (RAG) approach by fetching pricing and policy information from a local JSON knowledge base. This avoids hardcoded responses and improves maintainability.

Tool execution is handled through a mock function that simulates lead capture. The system ensures that the tool is only triggered after all required user details are collected, preventing premature execution.

This modular design makes the system scalable, maintainable, and suitable for real-world deployment.

🔹 WhatsApp Integration (Webhook Answer)

To integrate this agent with WhatsApp, we can use the WhatsApp Business API along with a backend server (e.g., Flask or FastAPI). Incoming user messages are received via webhooks and forwarded to the agent.

The backend processes the message, passes it through the LangGraph workflow, and generates a response. This response is then sent back to the user via the WhatsApp API.

State management can be handled using a session store (e.g., Redis or database) to track user conversations across messages. This ensures continuity in multi-turn interactions.