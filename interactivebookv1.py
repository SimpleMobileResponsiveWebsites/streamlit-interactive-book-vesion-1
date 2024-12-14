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
        ### Burst Softare Methodology Written By Nathan Rossow - Fast Prototyping With Github, Streamlit Cloud, Python And Pycharm Professional
            
        ### Step 1 - Getting Started With Github
        1. **Ensure you have a GitHub account. If you have a Github.com account, please sign in now.  If not, sign up and create a github account.  Ensure you are logged in.**
        2. **Create a new repository for your streamlit web application.**
        3. **Next, enter a name for the repository, choose the gitignore for python and choose next.**
            
        ### Step 2 - Getting Started with Streamlit and GitHub
        
        1. **Sign up at streamlit.io and share.streamlit.io.**
        2. **Log in to your Streamlit account.**
        3. **To link your github account, open the cloud menu in streamlit and select workspaces.**
        4. **Choose Connect GitHub account from the dropdown.**
        5. **Enter your GitHub credentials and authorize Streamlit to access your repositories.**
        6. **To access private repositories (optional), Go to Settings > Linked accounts in github.**
        7. **Click Connect here under Source control and reauthorize Streamlit.**
        
        ### Third Step:
        1.  **Download and install pycharm professional**
        2.  **Link your pycharm professional softare with your github account.  Linking pycharm professional with the github account allows developers to pull the entire project into pycharm professional from the github repostiory.**
        3.  **Once changes to the codebase are made locally on your computer while using pycharm professional, as a developer, you can push and commit those changes to the github repository and deploy the application using streamlit cloud.**

        ### Fourth Step:
        1. [Open VCSToPDF Tool](https://vcstopdf1v3.streamlit.app/)
        2. **Enter the app version.**
        3. **The app version is the file name for your application.**
        4. **Use a # as a deliminter for each:**
        5. **idea**
        6. **feature**
        7. **function**
        8. **requirement**
        9. **graphical user interface ideas**
        10. **Save your inputs to VCSToPDFv1-3.py.**
        11.  **Generate and download the .pdf file containing all of the steps for (2-9).**
        12.  **Open the newly downloaded .pdf file.**
        13.  **Copy all of the contents of the .pdf file.**
        
        ### Fifth Step:  
        1. Open your favoriate AI Chat Model.
        1. Using Grok [Explore X.ai](https://x.ai/)
        2. Using Meta.ai [Explore Meta.ai](https://meta.ai/)
        3. Using Gemini [Explore Google Gemini](https://ai.google/gemini/)
        4. Using DeepAi [Explore Deepai.org/chat](https://deepai.org/chat)
        5. Using Claude.ai [Explore Claude.ai](https://claude.ai/)
        6. Using Chatgpt [Explore ChatGPT](https://chat.openai.com/)
            
       
        """,   
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
