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
        """Use generational ai to write the code: Here's an organized overview discussing writing, testing, and documenting an app with considerations for version control and local storage:

### Use generational ai to write the code

**Use the link below to open up a directory of generative ai tools:**

[Open AI Coding Tools Directory](https://aicodingtoolsdirectoryv1.streamlit.app/)

Clearly articulate the app's goals and the problems it solves.
Identify core features and functionalities.

**Choose the Technology Stack:**

- **Frontend**: Frameworks like React, Angular, or Vue.js.
- **Backend**: Node.js, Python (Django/Flask), or Java (Spring).
- **Database**: SQL (PostgreSQL, MySQL) or NoSQL (MongoDB).
- **Local storage**: Options like IndexedDB, LocalStorage, or file-based storage.

**Architecture and Design Patterns:**

Use scalable and maintainable architecture, e.g., MVC or MVVM.
Plan for modularity and reusable components.
Incorporate APIs for backend communication and third-party integrations.

**Development:**

Adhere to clean code principles.
Use consistent naming conventions and structure.
Implement logging for debugging and monitoring.

**Local Storage Integration:**

Evaluate what data is suitable for local storage (e.g., user preferences, cache).
Use encryption for sensitive information.
Implement synchronization with remote storage when applicable.
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
