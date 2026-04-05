import streamlit as st
import requests

st.title("📝 AI Blog Writer (Gemini)")

# Inputs
topic = st.text_input("Enter blog topic")
tone = st.selectbox("Tone", ["professional", "casual", "funny"])
length = st.selectbox("Length", ["short", "medium", "long"])

if st.button("Generate Blog"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        data = {
            "topic": topic,
            "tone": tone,
            "length": length
        }

        try:
            res = requests.post(
                "http://127.0.0.1:8000/generate_blog",
                json=data,
                timeout=60
            )

            if res.status_code == 200:
                response_json = res.json()

                if "blog" in response_json:
                    st.subheader("Generated Blog")
                    st.write(response_json["blog"])
                else:
                    st.error(response_json.get("error", "Unknown error"))

            else:
                st.error(f"Error: {res.status_code}")

        except Exception as e:
            st.error(f"Connection error: {str(e)}")