import streamlit as st

def render_kpi(label: str, val: str, delta: str, chart_emoji: str = "📈"):
    """
    Renders a modernized, custom HTML/CSS KPI card to mimic the React frontend.
    """
    # Simple logic to determine if the delta should be green or red
    # You can expand this based on the specific words you use in your app
    delta_color = "#10B981"  # Emerald green for positive
    if "-" in delta or "baisse" in delta.lower() or "rejet" in delta.lower():
        delta_color = "#EF4444"  # Rose red for negative
        
    # The custom HTML and inline CSS payload
    html_content = f"""
    <div style="
        background-color: #FFFFFF;
        padding: 20px 24px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        border: 1px solid rgba(232, 95, 30, 0.1); /* Subtle Hermès Orange border */
        display: flex;
        flex-direction: column;
        gap: 8px;
        margin-bottom: 1rem;
    ">
        <span style="
            font-family: 'Inter', sans-serif; 
            font-size: 0.75rem; 
            color: #78716C; /* Stone 500 */
            font-weight: 600; 
            text-transform: uppercase; 
            letter-spacing: 0.05em;
            display: flex;
            align-items: center;
            gap: 6px;
        ">
            {chart_emoji} {label}
        </span>
        <span style="
            font-family: 'Inter', sans-serif; 
            font-size: 2.5rem; 
            font-weight: 700; 
            color: #1C1917; /* Stone 900 */
            line-height: 1;
            letter-spacing: -0.02em;
        ">
            {val}
        </span>
        <span style="
            font-family: 'Inter', sans-serif; 
            font-size: 0.8rem; 
            font-weight: 600; 
            color: {delta_color};
            margin-top: 4px;
        ">
            {delta}
        </span>
    </div>
    """
    
    # Render the HTML block directly into the Streamlit app
    st.markdown(html_content, unsafe_allow_html=True)