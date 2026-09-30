# 📘 Assignment: Using Web APIs with Python

## 🎯 Objective

Learn how a Python program requests data from a web API and reads its JSON response. Use only Python's standard library to retrieve and display a to-do item.

## 📝 Tasks

### 🛠️ Fetch and Decode JSON

#### Description
Complete `fetch_todo(todo_id)` to request a to-do item from the JSONPlaceholder API and decode the response as JSON.

#### Requirements
Completed program should:

- Request `https://jsonplaceholder.typicode.com/todos/{todo_id}` using `urllib.request.urlopen()`
- Set a timeout so the program does not wait forever
- Read the response and convert its JSON text into a Python dictionary
- Return the decoded dictionary from `fetch_todo(todo_id)`


### 🛠️ Display the To-Do Item

#### Description
Complete `display_todo(todo)` to show the useful fields returned by the API.

#### Requirements
Completed program should:

- Display the item's ID and title
- Display whether the item is complete
- Call `fetch_todo()` and `display_todo()` from `main()`

Example output:

```text
To-do #1: delectus aut autem
Completed: No
```


### 🛠️ Handle Input and Request Errors

#### Description
Make the program respond clearly when the user enters an invalid ID or the request cannot be completed.

#### Requirements
Completed program should:

- Ask the user for a to-do ID and report non-numeric input without a traceback
- Handle an HTTP error such as a 404 response for an unknown ID
- Handle a network or timeout error with a helpful message
- Use only Python's standard library; do not install third-party packages