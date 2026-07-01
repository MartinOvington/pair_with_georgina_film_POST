from playwright.sync_api import Page, expect

"""
Visiting the / endpoint
Has all the expected films listed
"""
def test_films_page_all_films_listed(clean_db, page: Page):
    page.goto("http://127.0.0.1:5001/films")

    films = page.locator("li")

    expected_films = [
        "Jaws, 1987",
        "Scream, 1999",
        "Project Hail Mary, 2026"
    ]
    actual_films = films.all_inner_texts()
    assert actual_films == expected_films