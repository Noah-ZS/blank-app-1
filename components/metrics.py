import streamlit as st

def render_kpi(label: str, val: str, delta: str, chart_emoji: str = "📈"):
    """Visual metric component that closely tracks design structure."""
    with st.container(border=True):
        st.caption(f"{chart_emoji} {label.upper()}")
        st.markdown(f"## {val}")
        st.caption(delta)