import wikipedia
import warnings
from bs4 import GuessedAtParserWarning

warnings.filterwarnings("ignore", category=GuessedAtParserWarning)  # Remove the beautifulsoup error text


def main():
    """Prompt user for wikipedia searches in a loop and display page details, title, summary and url."""
    prompt = "Enter page title: "
    query = input(prompt)
    while query != "":
        try:
            page = wikipedia.page(query, auto_suggest=False)
            print(page.title)
            print(wikipedia.summary(page.title, sentences=3, auto_suggest=False))
            print(page.url)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{query}" does not match any pages. Try another id!')
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10])
        query = input(f"\n{prompt}")

    print("Thank you.")


main()
