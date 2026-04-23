from langgraph.graph import StateGraph
from agent.intent import detect_intent
from agent.rag import get_pricing_info
from agent.tools import mock_lead_capture


def intent_node(state):
    user_input = state["input"]

    # Stay in lead collection mode
    if state.get("mode") == "lead":
        state["intent"] = "lead"
        return state

    intent = detect_intent(user_input)
    state["intent"] = intent

    if intent == "high_intent":
        state["mode"] = "lead"

    return state


def greeting_node(state):
    state["response"] = "Hello! How can I help you with AutoStream?"
    return state


def rag_node(state):
    pricing = get_pricing_info()
    state["response"] = (
        f"Basic Plan: {pricing['basic']['price']}\n"
        f"Pro Plan: {pricing['pro']['price']}"
    )
    return state


def lead_node(state):
    user_input = state["input"]

    # First entry into lead flow
    if not state.get("name") and state.get("intent") == "high_intent":
        state["response"] = "What is your name?"
        return state

    # Collect name
    if not state.get("name"):
        state["name"] = user_input
        state["response"] = "Please provide your email."
        return state

    # Collect email
    if not state.get("email"):
        state["email"] = user_input
        state["response"] = "Which platform do you create content on?"
        return state

    # Collect platform
    if not state.get("platform"):
        state["platform"] = user_input
        return state

    return state


def tool_node(state):
    if state.get("name") and state.get("email") and state.get("platform"):
        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        state["response"] = "Your details have been recorded. Let me know if you need anything else."

        # Reset after completion
        state["name"] = None
        state["email"] = None
        state["platform"] = None
        state["mode"] = None

    return state


def build_graph():
    builder = StateGraph(dict)

    builder.add_node("intent", intent_node)
    builder.add_node("greeting", greeting_node)
    builder.add_node("rag", rag_node)
    builder.add_node("lead", lead_node)
    builder.add_node("tool", tool_node)

    builder.set_entry_point("intent")

    builder.add_conditional_edges(
        "intent",
        lambda state: state["intent"],
        {
            "greeting": "greeting",
            "pricing": "rag",
            "high_intent": "lead",
            "lead": "lead",
            "general": "greeting"
        }
    )

    builder.add_edge("lead", "tool")

    return builder.compile()