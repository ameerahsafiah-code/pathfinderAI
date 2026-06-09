import streamlit as st

def render_swot_card(emoji, title, items, border_color, bg_color):
    """Generates a beautiful, reusable SWOT card."""
    bullet_points = "".join([f"<li style='margin-bottom: 6px;'>{item}</li>" for item in items])
    if not items:
        bullet_points = "<li style='color: #888; font-style: italic;'>Tiada data</li>"
        
    html_layout = f"""
    <div style="
        background: {bg_color};
        border: 1px solid {border_color};
        border-top: 5px solid {border_color};
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px -3px rgba(0, 0, 0, 0.05);
        min-height: 200px;
        margin-bottom: 20px;
    ">
        <h3 style="margin: 0 0 15px 0; color: #111827; font-size: 1.15rem; font-weight: 700;">
            {emoji} {title}
        </h3>
        <ul style="margin: 0; padding-left: 20px; color: #374151; font-size: 0.95rem; line-height: 1.5;">
            {bullet_points}
        </ul>
    </div>
    """
    st.html(html_layout)