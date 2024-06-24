import gradio as gr
import difflib

# Define the knowledge base as a dictionary
knowledge_base = {
    "CDA" : "Citizen Development Program",
    "CDP" : "Citizen Development Program",
    "ITSC" : "IT Service Continuity",
    "GMAA" : "GMs Accountability Audit",
    "GBCM" : "Global Business Continuity Management",
    "PFP":"Pay for Performance",
    "HORECA":"Hotel,Restaurants,Cafe",
    "GT" : "General Trade",
    "TLP":"Trade Loyalty Platform",
    "MVP":"Most Valued Partners",
    "VP":"Valued Partners",
    "P":"Partners",
    "OMR":"Open Market Rate","ZA04" :  "BAT South Africa - Heidelberg",
    "ZLJM" :  "Zero Loss Journey Map",
    "ZW06" :  "BAT Zimbabwe - Harare",
    "SDLW" : "Same day last week",
}

# Define the Gradio interface function
def chatbot_interface(acronym):
    acronym = acronym.strip().toUpperCase()  # Remove leading/trailing whitespace and convert to uppercase
    if acronym in knowledge_base:
        response = f"Answer: {knowledge_base[acronym]}"
    else:
        closest_match = difflib.get_close_matches(acronym, knowledge_base.keys(), n=1)
        if closest_match:
            response = f"No exact match found in BATCCAPEDIA. Did you mean '{closest_match[0]}'?"
        else:
            response = "Not found in BATCCAPEDIA"
    return response

# Create the Gradio interface
css = """
.gradio-container {
    background: rgb(14, 43, 99);
    display: flex;
    flex-direction: column;
    align-items: center;
}
footer {
    display: none !important;
}
"""

# HTML content for the logo
html_content = """
<div style="text-align: center; margin-bottom: 20px;">
    <img src="https://i.ibb.co/82Qf4rc/APMEA-CENTRAL-White.png" border="0" alt='BAT Bangladesh Logo' style='max-width: 300px;'>
</div>
"""

with gr.Blocks(css=css) as demo:
    gr.HTML(html_content)
    gr.Interface(
        fn=chatbot_interface,
        inputs=gr.Textbox(label="Acronym", placeholder="Enter Acronym Here"),
        outputs=gr.Textbox(label="Answer"),
        theme='default',
    )

demo.launch()
