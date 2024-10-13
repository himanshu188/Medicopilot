import streamlit as st
import json
import time
import requests

def beautify_response(response_data):
    data = response_data['items']
    st.markdown(data)  # This will render the markdown content


st.title(":robot_face: Medicopilot")
file = st.file_uploader("Choose a file to index...", type=["docx", "pdf", "txt"])
# Create tabs
tab1, tab2, tab3 = st.tabs(["Agent1", "Agent2", "Agent3"])


def create_agent_tab(agent_name, api_endpoint):
    with st.container():

        # Create a placeholder for the submit button and response
        submit_button_placeholder = st.empty()
        response_placeholder = st.empty()
        submit_button = st.button(f"Submit to {agent_name}", key=f"submit_{agent_name}")
        if submit_button:
            # if file is not None:
            url = "http://localhost:8000/agent1"
            # files = {"file": (file.name, file.getvalue(), file.type)}

            submit_button_placeholder.empty()
            progress_bar = st.progress(0)
            status_text = st.empty()
            try:
                # response = requests.post(url, files=files)
                for i in range(100):
                    time.sleep(0.05)  # Adjust this value to match your actual processing time
                    progress_bar.progress(i + 1)
                    status_text.text(f"Processing: {i + 1}%")

                response = requests.get(url)
                if response.status_code == 200:
                    st.success("File submitted successfully!")
                    st.write("Response from server:")
                    # Parse the JSON response
                    response_data = response.json()

                    # Display the response in the placeholder
                    with response_placeholder.container():
                        st.subheader("Response from server:")
                        beautify_response(response_data)
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
        # else:
        #     st.warning("Please upload a file before submitting.")

with tab1:
    create_agent_tab("Agent1", "/agent1")

with tab2:
    create_agent_tab("Agent2", "/agent2")

with tab3:
    create_agent_tab("Agent3", "/agent3")

# output_container = st.empty()
# answer_container = output_container.chat_message("assistant", avatar="🦜")
# answer_container.write('test')
