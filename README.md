The codebase snippet below demonstrates how the page design is structured for the application. You can use this template to create additional pages by modifying the book_pages list or dynamically loading content. Here's the relevant part for page rendering:

python
Copy code
# Function to display a single page
def display_page(page_number, book_pages):
    st.title(f"Page {page_number + 1}")
    st.write(book_pages[page_number])
Explanation:
st.title(f"Page {page_number + 1}"): Sets the title of the page dynamically based on the current page number.
st.write(book_pages[page_number]): Displays the content of the selected page using Streamlit's write method.
Extending for Additional Pages:
To add more pages, you can:

Append content to the book_pages list in the main() function:
python
Copy code
book_pages.append("""
### New Page Title

Add your new content here.

[Click here to access additional resources.](https://example.com)
""")
Use the display_page() function to render new pages dynamically:
python
Copy code
new_page_number = len(book_pages)  # Assign a number for the new page
display_page(new_page_number, book_pages)
This snippet is reusable and adaptable for designing additional pages or sections for your application.
