# API Documentation

This document provides documentation for the Rest API. The API allows you to perform CRUD operations on a "Person" resource.

## Endpoints

### Create a Person

- **URL**: `/api/people/`
- **Method**: POST
- **Request Body**:
  - Example:
    ```json
    {
      "name": "John Doe",
      "age": 30
    }
    ```
- **Response**:
  - HTTP Status: 201 Created
  - Example Response Body:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "age": 30
    }
    ```

### List People

- **URL**: `/api/people/`
- **Method**: GET
- **Query Parameters**:
  - `name` (optional): Filter people by name (case-insensitive).
- **Response**:
  - HTTP Status: 200 OK
  - Example Response Body (if filtered by name="John"):
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "age": 30
      },
      {
        "id": 2,
        "name": "John Smith",
        "age": 25
      }
    ]
    ```

### Retrieve a Person

- **URL**: `/api/people/{id}/`
- **Method**: GET
- **Response**:
  - HTTP Status: 200 OK
  - Example Response Body:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "age": 30
    }
    ```

### Update a Person

- **URL**: `/api/people/{id}/`
- **Method**: PUT
- **Request Body**:
  - Example:
    ```json
    {
      "name": "Updated Name",
      "age": 35
    }
    ```
- **Response**:
  - HTTP Status: 200 OK
  - Example Response Body:
    ```json
    {
      "id": 1,
      "name": "Updated Name",
      "age": 35
    }
    ```

### Delete a Person

- **URL**: `/api/people/{id}/`
- **Method**: DELETE
- **Response**:
  - HTTP Status: 204 No Content

## Sample Usage

### Create a New Person

**Request:**

```http
POST /api/people/
Content-Type: application/json

{
  "name": "Alice Johnson",
  "age": 28
}

Response:

HTTP/1.1 201 Created

{
  "id": 3,
  "name": "Alice Johnson",
  "age": 28
}

List People by Name 
Request:

GET /api/people/?name=John

HTTP/1.1 200 OK

[
  {
    "id": 1,
    "name": "John Doe",
    "age": 30
  },
  {
    "id": 2,
    "name": "John Smith",
    "age": 25
  }
]

Limitations and Assumptions
Was a bit difficult to implement 'GET' requests via url. 

Setup and Deployment
To set up and deploy the API locally or on a server, follow these steps:**

Clone the repository from GitHub:*

git clone https://github.com/Amo-494/rest_api
Navigate to the project directory:


cd your-repo
Install the required dependencies:


pip install -r requirements.txt
Configure the database settings in settings.py if you are using a database other than the default SQLite.

Run migrations to create the database tables:


python manage.py migrate
Start the development server:

python manage.py runserver
Access the API at http://localhost:8000/api/people/

Test with Postman and the browser and host with ngrok.


+--------------------------+           +--------------------------+
|       <<Model>>         |           |       <<Serializer>>     |
|        Person            |           |     PersonSerializer      |
+--------------------------+           +--------------------------+
| - id: IntegerField       |           | - model: Person           |
| - name: CharField        |           | - fields: list            |
| - age: IntegerField      |           |   - name                   |
|                          |           |   - age                    |
|                          |           |                            |
| + __str__(): str         |           | + validate_name(value)   |
|                          |           | + validate_age(value)    |
|                          |           |                            |
+--------------------------+           +--------------------------+
            |                                   |
            |                                   |
            |                                   |
+--------------------------+           +--------------------------+
|       <<View>>          |           |       <<View>>            |
|   PersonCreateView      |           |   PersonRetrieveUpdate-   |
|                        |           |   DestroyView              |
+--------------------------+           +--------------------------+
| - queryset: Person     |           | - queryset: Person        |
| - serializer_class:     |           | - serializer_class:       |
|   PersonSerializer      |           |   PersonSerializer        |
|                        |           |                            |
|                        |           |                            |
+--------------------------+           +--------------------------+
            |                                   |
            |                                   |
            |                                   |
+--------------------------+           +--------------------------+
|       <<URL Pattern>>   |           |       <<URL Pattern>>     |
|   '/api/people/'       |           |   '/api/people/<int:pk>/' |
+--------------------------+           +--------------------------+
