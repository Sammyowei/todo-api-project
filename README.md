# Todo API

A simple Todo API built with Django and Django REST Framework (DRF). This API provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on todo items. 

## Features

- **List all todos**
- **Create a new todo**
- **Retrieve a specific todo by ID**
- **Update a specific todo by ID**
- **Partially update a specific todo by ID**
- **Delete a specific todo by ID**

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [List All Todos](#list-all-todos)
  - [Create a New Todo](#create-a-new-todo)
  - [Retrieve a Specific Todo](#retrieve-a-specific-todo)
  - [Update a Specific Todo](#update-a-specific-todo)
  - [Partially Update a Specific Todo](#partially-update-a-specific-todo)
  - [Delete a Specific Todo](#delete-a-specific-todo)
- [Authentication](#authentication)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python** (version 3.7 or higher) - [Download Python](https://www.python.org/downloads/)
- **pip** (Python package installer) - [Installing pip](https://pip.pypa.io/en/stable/installation/)
- **virtualenv** (Optional but recommended for project isolation) - Install via pip:

  ```bash
  pip install virtualenv
  ```

 ## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

    ```bash
    git clonehttps://github.com/Sammyowei/todo-api-project.git
    cd todo-api
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv todoenv
    source todoenv/bin/activate  # On Windows use `todoenv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser to access the Django admin interface:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Your API should now be available at http://127.0.0.1:8000/api/todos/.

## Usage

### Running the Development Server

To run the server, use the following command:

  ```bash
python manage.py runserver
  ```

Visit http://127.0.0.1:8000/api/todos/ in your browser or use a tool like Postman to interact with the API.


## API Endpoints

### List All Todos

- **Endpoint:** `/api/todos/`
- **Method:** `GET`
- **Description:** Retrieves a list of all todos.
- **Request Example:**

  ```http
  GET /api/todos/
  ```

- **Response Example:**

  ```json
  [
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Milk, Bread, Eggs",
      "completed": false,
      "uid": "User-Id"
    },
    {
      "id": 2,
      "title": "Complete Django tutorial",
      "description": "Work through the Django REST Framework documentation",
      "completed": true,
      "uid": "User-Id"
    }
  ]
  ```

### Create a New Todo

- **Endpoint:** `/api/todos/`
- **Method:** `POST`
- **Description:** Creates a new todo.
- **Request Example:**

  ```http
  POST /api/todos/
  ```

- **Request Body:**

  ```json
  {
    "title": "New Task",
    "description": "Description of the new task",
    "completed": false,
    "uid": "Required User Field"
  }
  ```

- **Response Example:**

  ```json
  {
    "id": 3,
    "title": "New Task",
    "description": "Description of the new task",
    "completed": false
  }
  ```

### Retrieve a Specific Todo

- **Endpoint:** `/api/todos/<id>/`
- **Method:** `GET`
- **Description:** Retrieves a specific todo by its ID.
- **Request Example:**

  ```http
  GET /api/todos/1/
  ```

- **Response Example:**

  ```json
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, Bread, Eggs",
    "completed": false
  }
  ```

### Update a Specific Todo

- **Endpoint:** `/api/todos/<id>/`
- **Method:** `PUT`
- **Description:** Updates a specific todo by its ID.
- **Request Example:**

  ```http
  PUT /api/todos/1/
  ```

- **Request Body:**

  ```json
  {
    "title": "Updated Task Title",
    "description": "Updated description",
    "completed": true
  }
  ```

- **Response Example:**

  ```json
  {
    "id": 1,
    "title": "Updated Task Title",
    "description": "Updated description",
    "completed": true
  }
  ```

### Partially Update a Specific Todo

- **Endpoint:** `/api/todos/<id>/`
- **Method:** `PATCH`
- **Description:** Partially updates a specific todo by its ID.
- **Request Example:**

  ```http
  PATCH /api/todos/1/
  ```

- **Request Body:**

  ```json
  {
    "completed": true
  }
  ```

- **Response Example:**

  ```json
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, Bread, Eggs",
    "completed": true
  }
  ```

### Delete a Specific Todo

- **Endpoint:** `/api/todos/<id>/`
- **Method:** `DELETE`
- **Description:** Deletes a specific todo by its ID.
- **Request Example:**

  ```http
  DELETE /api/todos/1/
  ```

- **Response Example:**

  ```http
  HTTP/1.1 204 No Content
  ```

## Authentication

The API uses token-based authentication. You can obtain a token by sending a `POST` request to `/api-token-auth/` with your username and password.

### Get Authentication Token

- **Endpoint:** `/api-token-auth/`
- **Method:** `POST`
- **Description:** Obtain an authentication token.
- **Request Example:**

  ```http
  POST /api-token-auth/
  ```

- **Request Body:**

  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```

- **Response Example:**

  ```json
  {
    "token": "your_generated_token"
  }
  ```

Add the token to the `Authorization` header for all subsequent requests:

```http
Authorization: Token your_generated_token
```

## Testing

To run the test suite, use the following command:

```bash
python manage.py test
```

This will execute the tests defined in `todo/tests.py`.

### Example Tests

The test cases cover:

- **List Todos**
- **Create Todo**
- **Retrieve Todo**
- **Update Todo**
- **Partially Update Todo**
- **Delete Todo**

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your changes are well-documented and tested.

### Steps to Contribute

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Submit a pull request**

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
```
