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
""",
        """Testing the App:

Ensure that your app works as intended by thoroughly testing each feature. Streamlit's live preview feature helps you quickly identify and fix issues during development.

**Plan the Test Strategy:**
- Outline unit tests, integration tests, end-to-end tests, and performance tests.
- Prioritize critical paths for rigorous testing.

**Automated Testing:**
- Use frameworks like Jest, Mocha, or Selenium for automated testing.
- Integrate CI/CD pipelines for regular test execution.

**Manual Testing:**
- Perform exploratory testing to identify edge cases.
- Test on diverse platforms, browsers, and devices.

**Error Handling and Reporting:**
- Ensure comprehensive error messages and logs.
- Implement real-time monitoring using services like Sentry or Datadog.

It's critically important to finish the testing end-to-end for the application before you release the product.
""",
        """Documenting the app:

Good documentation is key for version control and local storage. Include clear instructions on how to use the app, maintain it, and collaborate with others. Use tools like Git for version control to track changes and manage updates.

**Local Storage Documentation:**
- Specify data storage mechanisms, structure, and retrieval logic.
- Include guidelines on how to safely update or clear local storage without data loss.
- Document encryption methods for stored data.

**API Documentation:**
- Use tools like Swagger or Postman to auto-generate API documentation.
- Include examples of requests and responses for each endpoint.

**Version Control and Documentation:**
- Ensure you document the end-to-end testing so others can validate and verify what end-to-end tests have been completed, keeping everyone included in the project up to date on the project's status.
- Use VCSTopdf to document the app version, regression testing notes, terminal outputs, and codebases.
""",
        """On the fourth page, the story takes an unexpected turn.""",
        """The fifth page starts to bring things toward a climax.""",
        """Finally, the last page wraps up the story with a satisfying conclusion."""
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
