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
