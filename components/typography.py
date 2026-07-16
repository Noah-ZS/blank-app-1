import streamlit as st

def render_page_title(title: str, subtitle: str = None):
    """Standardizes the luxury H1 headers across all views."""
    
    # HTML must be flush to the left to prevent Markdown from making it a code block
    html = f"""<div style="margin-bottom: 24px;">
    <h1 style="font-family: 'Cormorant Garamond', serif; color: #1C1917; font-size: 2.5rem; font-weight: 700; margin-bottom: 4px; line-height: 1.1;">
        {title}
    </h1>"""
    
    if subtitle:
        html += f"""
    <p style="font-family: 'Inter', sans-serif; color: #78716C; font-size: 0.9rem; margin-top: 0;">
        {subtitle}
    </p>"""
        
    html += "\n</div>"
    
    st.markdown(html, unsafe_allow_html=True)