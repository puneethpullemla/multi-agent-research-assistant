import streamlit as st
from graph.workflow import build_graph

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Multi-Agent Research Assistant")
st.write("Research any topic using multiple AI agents.")

query = st.text_input(
    "Enter a research topic:",
    placeholder="Example: Artificial Intelligence in Healthcare"
)

if st.button("Start Research"):

    if not query:
        st.warning("Please enter a topic.")
        st.stop()

    graph = build_graph()

    with st.spinner("Researching..."):

        result = graph.invoke({
            "query": query,
            "research_data": "",
            "summary": "",
            "verified_data": "",
            "final_report": ""
        })

    st.success("Research Complete!")

    st.subheader("Final Report")

    st.markdown(result["final_report"])

    st.download_button(
        label="📥 Download Report",
        data=result["final_report"],
        file_name="research_report.txt",
        mime="text/plain"
    )