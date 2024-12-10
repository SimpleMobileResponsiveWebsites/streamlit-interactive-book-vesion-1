import streamlit as st

# Function to display a single page
def display_page(page_number, book_pages):
    st.title(f"Page {page_number + 1}")
    st.write(book_pages[page_number])

# Main application
def main():
    st.sidebar.title("Book Navigation")

    # Sample book content split into manageable strings
    book_pages = [
        """
        ### Use generative AI coding tools to write the code

        **Use the link below to open up a directory of generative AI tools:**

        [Open The AI Coding Tools Directory](https://aicodingtoolsdirectoryv1.streamlit.app/)
        """,
        """
        ### VCSToPDF Tool for Documentation

        **Use the link below to open the VCSToPDF tool:**

        [Open VCSToPDF Tool](https://vcstopdf1v3.streamlit.app/)
        """,
        """
        ### Using ChatGPT or Other AI Tools to Write Code for Your Application

        AI tools like ChatGPT can assist in writing, debugging, and optimizing code. 
        Here are a few tips on how to leverage these tools effectively:

        1. **Define Clear Objectives:** Clearly state what you want the AI to do. Provide detailed prompts.
        2. **Iterative Development:** Use AI to generate code snippets, then iteratively refine and customize them.
        3. **Learn from Suggestions:** Review the AI-generated code to understand the logic and apply it to similar tasks.

        **Start using ChatGPT for coding assistance here:**
        [Explore ChatGPT](https://chat.openai.com/)
        """,
        """
        ### Using Claude.ai for AI-Powered Coding

        Claude.ai is another powerful AI tool for assisting with your coding needs. 
        Here are some ways to utilize Claude.ai effectively:

        1. **Natural Language Coding:** Provide conversational instructions to generate code snippets.
        2. **Debugging and Testing:** Use Claude.ai to identify and fix issues in your code.
        3. **Documentation Support:** Ask Claude.ai to help create clear and concise documentation for your projects.

        **Start using Claude.ai for your projects here:**
        [Explore Claude.ai](https://claude.ai/)
        """,
        """
        ### Using Meta.ai for Advanced AI Solutions

        Meta.ai offers cutting-edge AI tools for diverse applications, including coding. 
        Here are some benefits of using Meta.ai:

        1. **Scalable AI Models:** Leverage Meta.ai's infrastructure for handling complex coding and data analysis tasks.
        2. **Integration Capabilities:** Easily integrate Meta.ai tools into your existing workflows.
        3. **Comprehensive Support:** Access detailed guides and support to make the most of their tools.

        **Start exploring Meta.ai for your development needs here:**
        [Explore Meta.ai](https://meta.ai/)
        """,
        """
        ### Using Google Gemini for AI-Driven Insights

        Google Gemini combines advanced AI technologies to assist developers in creating innovative applications. 
        Here are key features of Google Gemini:

        1. **Cross-Modal Capabilities:** Work with text, images, and other data seamlessly.
        2. **Integrated Ecosystem:** Leverage the power of Google's AI ecosystem for your projects.
        3. **Efficient Problem-Solving:** Use Gemini to analyze data and generate actionable insights quickly.

        **Discover how Google Gemini can empower your applications here:**
        [Explore Google Gemini](https://ai.google/gemini/)
        """,
        """
        ### Burst Software Methodology

        #### Writing the App

        - Use generational AI to write the code using VCSToPDF.
        - Open up Claude.ai.
        - Visit [ChatGPT](https://chat.openai.com/).
        - Access VCSToPDF: [VCSToPDF](https://vcstopdf1v3.streamlit.app/).
        - Enter the Python application name.
        - Include regression testing notes.

        In the code area, use delimiters for each idea, feature, function, requirement, and graphical user interface functionality.

        #### Testing the App

        - Test the app as quickly as possible.
        - Fast iterations are important in rapid prototyping.
        - Complete end-to-end testing of the application before releasing the product.

        #### Documenting the App for Version Control and Local Storage

        1. Document the end-to-end testing so others can validate and verify what tests have been completed.
        2. Use VCSToPDF to:
           - Document the app version.
           - Include regression testing notes.
           - Capture terminal outputs.
           - Archive code bases.
        """,
        """
        ### Regression Testing and Documentation

        #### App Version

        Ensure that the current application version is properly documented. Include version details in all relevant files and documentation.

        #### Regression Testing Notes

        - Maintain detailed notes of all regression testing performed, including:
          - New features tested.
          - Issues identified and resolved.
          - Performance benchmarks.

        #### Current Terminal Output

        - Capture and save the current terminal output for debugging and documentation purposes.

        #### Codebases

        - Archive the codebase for the current version.
        - Maintain a changelog of updates.

        #### Saving and Generating Documentation

        - Save the current testing documentation to the regression testing Streamlit app.
        - Generate a .pdf file summarizing the current codebase documentation.
        - Provide a download link for the .pdf file for easy access and sharing.

        """
    ]

    # Number of pages in the book
    total_pages = len(book_pages)

    # Table of Contents (TOC)
    st.sidebar.write("**Table of Contents:**")
    for i, content in enumerate(book_pages):
        if st.sidebar.button(f"Page {i + 1}"):
            st.session_state["page_number"] = i

    # Initialize page_number in session state
    if "page_number" not in st.session_state:
        st.session_state["page_number"] = 0

    # Display the selected page
    display_page(st.session_state["page_number"], book_pages)

if __name__ == "__main__":
    main()
