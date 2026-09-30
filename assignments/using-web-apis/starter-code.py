import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

API_BASE_URL = "https://jsonplaceholder.typicode.com/todos"
REQUEST_TIMEOUT_SECONDS = 10


def fetch_todo(todo_id):
    """Fetch one to-do item and return its decoded JSON data."""
    url = f"{API_BASE_URL}/{todo_id}"

    # TODO: Open the URL with a timeout, read the response, and decode its JSON.
    pass


def display_todo(todo):
    """Print the ID, title, and completion status of a to-do item."""
    # TODO: Display the useful fields from the todo dictionary.
    pass


def main():
    todo_id_text = input("Enter a to-do ID (1-200): ")

    # TODO: Convert the input to an integer and handle non-numeric input.
    todo_id = todo_id_text

    try:
        todo = fetch_todo(todo_id)
        display_todo(todo)
    except HTTPError as error:
        print(f"The server returned an HTTP error: {error.code}")
    except (URLError, TimeoutError) as error:
        print(f"Could not reach the API: {error}")
    except json.JSONDecodeError:
        print("The API response was not valid JSON.")


if __name__ == "__main__":
    main()