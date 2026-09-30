# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing books with FastAPI. Practice defining HTTP endpoints, validating request data with Pydantic, and returning appropriate status codes.

## 📝 Tasks

### 🛠️ List and Retrieve Books

#### Description
Start the provided FastAPI application and implement endpoints for listing all books and retrieving one book by its ID.

#### Requirements
Completed program should:

- Start with `uvicorn starter-code:app --reload`
- Return all books from `GET /books`
- Return one matching book from `GET /books/{book_id}`
- Return HTTP 404 when the requested book ID does not exist


### 🛠️ Create Books with Validated Data

#### Description
Use the provided `BookCreate` Pydantic model to accept and validate new book data, then add a `POST /books` endpoint.

#### Requirements
Completed program should:

- Accept a book's `title`, `author`, and `year` as JSON fields
- Assign each new book a unique ID and store it in the in-memory collection
- Return the created book with HTTP 201
- Let FastAPI return a validation error for requests with invalid field types or missing required fields


### 🛠️ Update and Delete Books

#### Description
Complete the API's update and delete operations so clients can manage existing books by ID.

#### Requirements
Completed program should:

- Update a book with `PUT /books/{book_id}` using the validated request model
- Delete a book with `DELETE /books/{book_id}` and return HTTP 204
- Return HTTP 404 when an update or delete request uses an unknown book ID
- Verify the endpoints using FastAPI's interactive API docs at `/docs`