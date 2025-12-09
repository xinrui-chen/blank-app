import streamlit as st

# Page setup
st.set_page_config(page_title="Tech4Good Idea Generator", page_icon="🌱")

st.title("🌱 Tech4Good Idea Generator")
st.write(
    "Welcome! This simple demo helps you brainstorm project ideas that use technology "
    "to create social impact. Choose a problem area, describe what you're interested in, "
    "and generate a few ideas to spark inspiration."
)

# Sidebar
st.sidebar.header("Project Settings")
problem_area = st.sidebar.selectbox(
    "Choose a problem area:",
    ["Education", "Health", "Environment", "Accessibility", "Community Support", "Other"],
)

user_description = st.sidebar.text_area(
    "Describe the community or problem you're interested in:"
)

project_scope = st.sidebar.selectbox(
    "Preferred project scope:",
    ["Beginner-friendly", "Intermediate", "Ambitious"],
)

generate_button = st.sidebar.button("Generate Ideas")


# Generate placeholder ideas (no API needed)
def generate_placeholder_ideas(area, desc, scope):
    base_ideas = {
        "Education": [
            "A tutoring-matching platform for underserved students.",
            "A study habit tracker tailored to different learning styles.",
            "A classroom feedback tool that lets students anonymously submit needs."
        ],
        "Health": [
            "A mood + habit tracker that sends early wellness alerts.",
            "A simple web-app that connects users to local health resources.",
            "A chatbot that provides mental health grounding exercises."
        ],
        "Environment": [
            "A neighborhood carbon footprint dashboard.",
            "A recycling guide that scans items with your camera.",
            "A wildfire safety tips app tailored to your location."
        ],
        "Accessibility": [
            "A tool that converts complex text into simplified reading levels.",
            "A navigation helper for visually impaired pedestrians.",
            "An app that adds auto-captions to short videos."
        ],
        "Community Support": [
            "A volunteering-opportunity finder based on your schedule.",
            "A food bank donation and inventory tracker.",
            "A mentorship-matching tool for local youth."
        ],
        "Other": [
            "A storytelling tool that captures stories from community elders.",
            "An issue-reporting platform for local neighborhoods.",
            "A digital gratitude wall for community well-being."
        ]
    }

    # If user writes something, personalize one idea
    custom_text = ""
    if desc.strip():
        custom_text = (
            f"- A project that specifically addresses: **{desc.strip()}**.\n"
        )

    ideas = base_ideas.get(area, [])
    formatted = "\n".join([f"- {idea}" for idea in ideas])

    header = f"### Here are some {scope.lower()} ideas for **{area}**:\n\n"
    return header + formatted + ("\n\n" + custom_text if custom_text else "")

# Output area
if generate_button:
    st.subheader("💡 Your Project Ideas")
    st.write(generate_placeholder_ideas(problem_area, user_description, project_scope))
else:
    st.info("Use the sidebar to configure your project area, then click **Generate Ideas**.")
