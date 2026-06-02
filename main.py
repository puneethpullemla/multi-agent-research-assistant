from graph.workflow import build_graph

graph = build_graph()

query = input("Enter your research topic: ")

result = graph.invoke({
    "query": query,
    "research_data": "",
    "summary": "",
    "verified_data": "",
    "final_report": ""
})

print("\n")
print("=" * 80)
print("FINAL REPORT")
print("=" * 80)
print("\n")

print(result["final_report"])