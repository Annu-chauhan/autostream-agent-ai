from agent.graph import build_graph

graph = build_graph()

state = {
    "name": None,
    "email": None,
    "platform": None,
    "mode": None
}

print("AutoStream Agent")

while True:
    user_input = input("User: ")

    state["input"] = user_input

    result = graph.invoke(state)

    state.update(result)

    print("Agent:", result["response"])