# Smart Campus
## A student management system for making school administration easier

This is a student management API that allows you to manage student data in a database. With this API, you can create, read, update, and delete student data, as well as perform various queries to retrieve specific information about the students.

It also allows admins to create, read, update and delete courses


Getting Started
To get started with the API, you will need to do the following:

- clone the project
- set up virtual environment
- install dependencies by running `pip install -r requirements.txt`
- run the app : `flask run`

API Endpoints
The following endpoints are available in the API:

- **HTTP Method:** POST
- **Endpoint:** `/auth/signup`
- **Description:** This endpoint allows users to create an account
---
- **HTTP Method:** POST
- **Endpoint:** `/auth/login`
- **Description:** This endpoint allows users to login to their account
---
- **HTTP Method:** POST
- **Endpoint:** `/auth/refresh`
- **Description:** This endpoint allows users to refresh their access token
---
- **HTTP Method:** GET
- **Endpoint:** `/students/students`
- **Description:** This endpoint retrieves all the student data in the database
---
- **HTTP Method:** POST
- **Endpoint:** `/students/students`
- **Description:** This endpoint creates a new student in the database. You need to send a JSON object with the following fields:

`
{
    "student_name": "John Doe",
    "student_email": "johndoe@example.com",
    "department" : "Psychology"
    "courses_registered": ["PSY 101", "MTH 101", "PHY 101"]
}
`
---
- **HTTP Method:** GET
- **Endpoint:** `/students/students/student_id`
- **Description:** This endpoint retrieves a specific student's data by their ID
---
- **HTTP Method:** GET
- **Endpoint:** `/students/students/student_id`
- **Description:** This endpoint retrieves all courses registered by a specific student
---
- **HTTP Method:** PUT
- **Endpoint:** `/students/students_student_id`
- **Description:** This endpoint updates student's data using their ID
---

- **HTTP Method:** DELETE
- **Endpoint:** `/students/students/students_id`
- **Description:** This endpoint deletes a specific student's data by their ID
---
- **HTTP Method:** GET
- **Endpoint:** `/courses/courses`
- **Description:** This endpoint retrieves all the courses offered in the school
---

- **HTTP Method:** POST
- **Endpoint:** `/courses/courses`
- **Description:** This endpoint registers a new course by admin
---


- **HTTP Method:** GET
- **Endpoint:** `/students/students`
- **Description:** This endpoint retrieves all the student data in the database
GET /courses/course_id
This endpoint retrieves a specific course by its ID.


PUT /courses/course_id
This endpoint updates a specific course by its ID. Admins only.

DELETE /courses/course_id
This endpoint deletes a specific course by its ID. Admins only.


GET /courses/course_id/students
This endpoint retrieves all the students offering a particular course.

This API uses JWT authentication

---

### Built with
    Flask
    Flask-RESTX
    Flask-SQLALCHEMY





