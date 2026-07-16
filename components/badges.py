import streamlit as st

def render_badge(text: str, status: str = "neutral"):
    """
    Renders a colored status pill. 
    status options: 'success', 'warning', 'danger', 'info', 'neutral'
    """
    colors = {
        "success": {"bg": "#D1FAE5", "text": "#065F46", "border": "#A7F3D0"},
        "warning": {"bg": "#FEF3C7", "text": "#92400E", "border": "#FDE68A"},
        "danger":  {"bg": "#FEE2E2", "text": "#991B1B", "border": "#FECACA"},
        "info":    {"bg": "#E0F2FE", "text": "#075985", "border": "#BAE6FD"},
        "neutral": {"bg": "#F5F5F4", "text": "#44403C", "border": "#E7E5E4"},
    }
    
    theme = colors.get(status, colors["neutral"])
    
    html = f"""
    <span style="
        background-color: {theme['bg']};
        color: {theme['text']};
        border: 1px solid {theme['border']};
        padding: 4px 10px;
        border-radius: 9999px; /* Fully rounded pill */
        font-family: 'Inter', sans-serif;
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        display: inline-flex;
        align-items: center;
    ">
        {text}
    </span>
    """
    st.markdown(html, unsafe_allow_html=True)