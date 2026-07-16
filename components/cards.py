import streamlit as st

def render_list_card(title: str, subtitle: str, metadata: str, icon: str = "📄"):
    # Flushed left to prevent Markdown code block formatting
    html = f"""<div style="padding: 12px 0; display: flex; align-items: center; gap: 16px;">
    <div style="background-color: #FBF6F0; color: #E85F1E; width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; flex-shrink: 0;">
        {icon}
    </div>
    <div style="flex-grow: 1; line-height: 1.3;">
        <div style="font-family: 'Inter', sans-serif; font-weight: 600; color: #1C1917; font-size: 0.95rem;">
            {title}
        </div>
        <div style="font-family: 'Inter', sans-serif; color: #78716C; font-size: 0.75rem; margin-top: 2px;">
            {subtitle}
        </div>
    </div>
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #A8A29E; text-align: right;">
        {metadata}
    </div>
</div>"""
    st.markdown(html, unsafe_allow_html=True)