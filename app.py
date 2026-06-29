import streamlit as st
from graph.workflow import app

st.set_page_config(
    page_title="Deep Research Agent",
    page_icon="🔍",
    layout="wide"
)

st.title("Deep Research Agent")
st.write("Generate comprehensive research reports using a multi-agent AI workflow.")
topic = st.text_input("Research Topic")

if st.button("🚀 Generate Report"):
    if not topic:
        st.warning("Please enter a research topic")
    else:
        initial_state ={
            "user_query": topic,
            "research_plan" :[],
            "search_results":{},
            "analysis": "",
            "final_report": "",
        }


        with st.spinner("Generating research report..."):
            result =app.invoke(initial_state)
        
        col1,col2 =st.columns(2)
        with col1:
            st.metric("Sections",len(result["research_plan"]))
        with col2:
            st.metric("Sources",sum(
                len(results)
                for results in result["search_results"].values()
            ))

        tab1,tab2,tab3 =st.tabs(
            ["📄 Final Report", "📊 Analysis", "🧠 Research Plan"]
        )
        with tab1:
            st.markdown(result["final_report"])
        with tab2:
            st.write(result["analysis"])
        with tab3:
            st.write(result["research_plan"])
        
        st.download_button(
            "📥 Download Report",
            result["final_report"],
            file_name="research_report.md"
        )
