import streamlit as st

# Function to display a single page
def display_page(page_number, book_pages):
    st.title(f"Page {page_number + 1}")
    st.write(book_pages[page_number])

# Main application
def main():
    st.sidebar.title("Book Navigation")

    # Sample book content
    book_pages = [
        "Writing the app: This involves creating the structure and functionality of the application. Streamlit makes it easy to build interactive apps with minimal code. Plan out your app's purpose and features before diving into coding.",
        "Testing the app: Ensure that your app works as intended by thoroughly testing each feature. Streamlit's live preview feature helps you quickly identify and fix issues during development.",
        "Documenting the app: Good documentation is key for version control and local storage. Include clear instructions on how to use the app, maintain it, and collaborate with others. Use tools like Git for version control to track changes and manage updates.",
        "On the fourth page, the story takes an unexpected turn.",
        "The fifth page starts to bring things toward a climax.",
        "Finally, the last page wraps up the story with a satisfying conclusion."
    ]

    # Number of pages in the book
    total_pages = len(book_pages)

    # Sidebar navigation
    st.sidebar.write("Navigate through the pages:")
    page_number = st.sidebar.number_input(
        "Go to page:", min_value=1, max_value=total_pages, value=1, step=1
    )

    # Display the selected page
    display_page(page_number - 1, book_pages)

if __name__ == "__main__":
    main()
