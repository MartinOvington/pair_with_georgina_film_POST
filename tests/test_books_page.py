from playwright.sync_api import Page, expect

"""
Visiting the /books endpoint
Has the right heading
"""
def test_books_page_heading(clean_db, page: Page):
    page.goto("http://127.0.0.1:5001/books")

    h1 = page.locator("h1")

    expect(h1).to_have_text("All your books")

"""
Visiting the /books endpoint
Has all the expected books listed
"""
def test_books_page_all_books_listed(clean_db, page: Page):
    page.goto("http://127.0.0.1:5001/books")

    books = page.locator("li")

    expected_books = [
        "The Gruffalo by Julia Donaldson",
        "Ada Twist, Scientist by Andrea Beaty",
        "The Girl Who Drank the Moon by Kelly Barnhill",
        "Dragons in a Bag by Zetta Elliott"
    ]
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books

"""
Adding a new book via the /book page form
Adds the book to the page
"""
def test_book_page_create_book_form(clean_db, page: Page):
    page.goto("http://127.0.0.1:5001/books")

    page.get_by_placeholder("Title").fill("Test title")
    page.get_by_placeholder("Author").fill("Test author")
    page.get_by_role("button", name="Submit").click()

    books = page.locator("li")

    expected_books = [
        "The Gruffalo by Julia Donaldson",
        "Ada Twist, Scientist by Andrea Beaty",
        "The Girl Who Drank the Moon by Kelly Barnhill",
        "Dragons in a Bag by Zetta Elliott",
        "Test title by Test author"
    ]
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books