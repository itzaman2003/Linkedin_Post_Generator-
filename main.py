import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Main app layout
def main():
    # Add custom CSS for background and styling
    st.markdown(
        """
        <style>
        body {
            background-color: f0f2f6; /* Light gray background */
            color: 333333; /* Dark text color */
        }
        .main-container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            border-radius: 15px;
            background-color: white; /* White container */
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        }
        h1 {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #2e86de; /* Blue header color */
        }
        </style>
        <div class="main-container">
            <h1>LinkWrite<h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)

    # Generate Button
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)

        # Display the post in a text box
        st.text_area("Generated Post", value=post, height=200)

        # Add a copy button
        st.code(post, language="text")

# Run the app
if __name__ == "__main__":
    main()

