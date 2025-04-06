# task_api

## Introduction

This project uses django-rest-framework(drf), Postgresql database.

## Installation

Just run the command: `docker-compose up`

Assuming you have docker installed on your machine.

## Usage

Fire up postman/insomnia/curl(best) and try API below.

# Task Management API Documentation

This document describes the API endpoints for managing tasks.

## Base URL

`http://localhost:8000/api/`

## Authentication

All endpoints except `/signup/`, `/login/` and `/token/` require JWT authentication.

* **Authorization Header:** `Authorization: Bearer <access_token>`

## Endpoints

### 1. User Registration (`/signup/`)

* **Method:** `POST`
* **Description:** Registers a new user.
* **Request Body (JSON):**

    ```json
    {
      "username": "example",
      "email": "example@example.com",
      "password": "securepassword"
    }
    ```

* **Response (201 Created):**

    ```json
    {
      "username": "example",
      "email": "example@example.com"
    }
    ```

* **Response (400 Bad Request):**
    * Returns validation errors if any of the fields are invalid.

### 2. Token Obtain (`/token/`)

* **Method:** `POST`
* **Description:** Obtains access and refresh tokens.
* **Request Body (JSON):**

    ```json
    {
      "username": "existinguser",
      "password": "existingpassword"
    }
    ```

* **Response (200 OK):**

    ```json
    {
      "access": "<access_token>",
      "refresh": "<refresh_token>"
    }
    ```

* **Response (401 Unauthorized):**
    * Returns an error if the credentials are invalid.

### 3. Token Refresh (`/token/refresh/`)

* **Method:** `POST`
* **Description:** Refreshes an access token.
* **Request Body (JSON):**

    ```json
    {
      "refresh": "<refresh_token>"
    }
    ```

* **Response (200 OK):**

    ```json
    {
      "access": "<new_access_token>"
    }
    ```

* **Response (401 Unauthorized):**
    * Returns an error if the refresh token is invalid.

### 4. Create Task (`/tasks/create/`)

* **Method:** `POST`
* **Description:** Creates a new task for the logged-in user.
* **Request Body (JSON):**

    ```json
    {
      "title": "My Task",
      "description": "Task description", // optional
      "status": "pending"  // or "in-progress", "completed", defaults to "pending" if blank
    }
    ```

* **Response (201 Created):**

    ```json
    {
      "id": 1,
      "title": "My Task",
      "description": "Task description",
      "status": "pending",
      "created_at": "2025-04-06T10:00:00Z",
      "updated_at": "2025-04-06T10:00:00Z"
    }
    ```

* **Response (400 Bad Request):**
    * Returns validation errors if any of the fields are invalid.

### 5. List Tasks (`/tasks/`)

* **Method:** `GET`
* **Description:** Retrieves all tasks for the logged-in user.
* **Response (200 OK):**

    ```json
    [
      {
        "id": 1,
        "title": "My Task",
        "description": "Task description (optional)",
        "status": "pending",
        "created_at": "2025-04-06T10:00:00Z",
        "updated_at": "2025-04-06T10:00:00Z"
      },
      {
        "id": 2,
        "title": "Another Task",
        "description": null,
        "status": "in-progress",
        "created_at": "2025-04-06T10:00:00Z",
        "updated_at": "2025-04-06T10:00:00Z"
      }
    ]
    ```

### 6. Retrieve, Update, Delete Task (`/tasks/{task_id}/`)

* **Methods:** `GET`, `PUT`, `PATCH`, `DELETE`
* **Description:** Retrieves, updates, or deletes a specific task.
* **`GET` (Retrieve):**
    * Retrieves the task with the given `task_id`.
    * **Response (200 OK):** Same as the single task object in the list response.
* **`PUT` (Update):**
    * Updates the task with the given `task_id`.
    * **Request Body (JSON):** Same as the create task request body.
    * **Response (200 OK):** Updated task object.
* **`PATCH` (Partial Update):**
    * Partially updates the task.
    * **Request Body (JSON):** Only the fields to be updated.
    * **Response (200 OK):** Updated task object.
* **`DELETE` (Delete):**
    * Deletes the task.
    * **Response (204 No Content):** Empty response.
* **Response (404 Not Found):**
    * Returned if the task does not exist or does not belong to the user.
* **Response (400 Bad Request):**
    * Returned on invalid input.

## Assignment Checklist

 - [x] GitHub Repository
   -  [x] A clean, well-organized repo with clear commit history.
	 -  [x] A README.md file with:
	 -  [x] Project setup instructions.
 	 -  [x] Deployment details.

 - [ ] Postman Collection
 - [ ] Deployed URL
