# API Development and Deployment for a Task Management Backend

## Overview

Your task is to create a backend-only API for managing tasks. The focus is on building RESTful APIs, deploying the service, and documenting the API endpoints. There is no frontend or UI development required—the deliverable is a working API.  
Once completed, you must provide:

* A GitHub repository with the source code.  
* A Postman collection with all API endpoints and example requests/responses.  
* The deployed URL to test the API live.

## Requirements

* API Requirements  
1. Authentication (JWT-based):  
   * Implement a simple user registration and login API.  
   * Use JWT for securing endpoints.  
   * Protect all task-related endpoints so only authenticated users can access them.  
2. Task Management:  
   * Create CRUD (Create, Read, Update, Delete) operations for tasks.  
   * Each task should have the following fields:  
   * id: Unique identifier for the task.  
   * title: A short title for the task.  
   * description: A detailed description of the task (optional).  
   * status: One of pending, in-progress, completed.  
   * Endpoints:  
     1. Create a new task.  
     2. Retrieve all tasks for the logged-in user.  
     3. Update a task’s title, description, or status.  
     4. Delete a task.

## Technical Requirements

* Use python with flask library (most preferred) or any other framework.  
* Use a database of your choice (e.g., MongoDB, PostgreSQL, SQLite, etc.).  
* Follow RESTful API design principles.  
* Protect sensitive data (e.g., JWT secret) using environment variables.

## Deployment

	•	Deploy the API to any cloud platform (e.g., Render, Railway, AWS, Azure, Vercel).  
	•	Ensure the deployed API is publicly accessible.

## Documentation

* Provide a Postman collection:

	•	Include all API endpoints with example requests and responses. Also the collection to read or list all tasks example should have a sample  authorization header to check.

* Include a README.md in your GitHub repo with:

	•	Project overview.  
	•	Steps to set up and run the project locally.  
	•	Details of the deployed API (base URL).

## Deliverables

* GitHub Repository:

	•	A clean, well-organized repo with clear commit history.  
	•	A README.md file with:  
	•	Project setup instructions.  
	•	Deployment details.

* Postman Collection:

	•	A collection containing all API endpoints and example requests/responses.

* Deployed URL:

	•	Provide the live URL of the deployed API.

## Evaluation Criteria

	•	API Design: Proper use of RESTful principles.  
	•	Functionality: Fully functional and secure APIs.  
	•	Code Quality: Clean, modular, and well-documented code.  
	•	Deployment: Accessible deployed API.  
	•	Documentation: Clear and complete Postman collection and README.md.  
	•	Extra Points:  
	•	Python usage.  
	•	Error handling with proper status codes.

## Timeline

	•	Deadline: 1 days.  
