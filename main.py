from dotenv import load_dotenv
from typing import List
from langchain_core.messages import BaseMessage, ToolMessage
from langgraph.graph import END, MessageGraph
from chains import revisor, first_responder
from tool_executor import execute_tools

load_dotenv()

if __name__ == "__main__":
    print("Welcome to the Reflexion Agent Project")

    MAX_ITERATION = 2
    builder = MessageGraph()
    builder.add_node("draft",first_responder)
    builder.add_node("execute_tools", execute_tools)
    builder.add_node("revise",revisor)

    builder.add_edge("draft","execute_tools")
    builder.add_edge("execute_tools","revise")
    builder.add_edge("revise","draft")

    def event_loop(state: List[BaseMessage]):
        count_tool_visits = sum(isinstance(item, ToolMessage) for item in state)
        num_iterations = count_tool_visits
        if num_iterations > MAX_ITERATION:
            return END
        return "execute_tools"

    builder.add_conditional_edges("revise", event_loop, {END: END, "execute_tools": "execute_tools"})
    builder.set_entry_point("draft")
    graph = builder.compile()
    graph.get_graph().draw_mermaid_png(output_file_path="graph.png")

    res = graph.invoke(
       "Write about how the India sensex will behave in upcoming a week or a month's time based on the trending geopolitical and economical matters. List down the possible ranges that it can move and the provide the suggestions on some of the stocks that could provide enormous returns in a week or a month's time."
    )
    print(res[-1].tool_calls[0]['args']['answer'])
