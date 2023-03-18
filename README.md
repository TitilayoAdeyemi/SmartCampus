# Student Management API
---

This is a student management API that allows you to manage student data in a database. With this API, you can create, read, update, and delete student data, as well as perform various queries to retrieve specific information about the students.

It also allows admins to create, read, update and delete courses


Getting Started
To get started with the API, you will need to do the following:

Clone the repository to your local machine.
Install all the required dependencies by running the following command: npm install
Start the server by running the command: npm start
API Endpoints
The following endpoints are available in the API:

POST /auth/signp
This enpoint allows users to register on the app

Post /auth/login
This enpoint allows users to login to the app

Post /auth/refresh
This enpoint allows users to refresh their access token

GET /students/students
This endpoint retrieves all the student data in the database.



POST /students/students
This endpoint creates a new student in the database. You need to send a JSON object with the following fields:

`
{
    "student_name": "John Doe",
    "student_email": "johndoe@example.com",
    "department" : "Psychology"
    "courses_registered": ["PSY 101", "MTH 101", "PHY 101"]
}
`

GET /students/students/student_id
This endpoint retrieves a specific student's data by their ID.

GET /students/students/student_id/courses
This endpoint retrieves all courses registered by a specific student.


PUT /students/students/student_id
This endpoint updates student's data using their ID.

DELETE /students/students/student_id
This endpoint deletes a specific student's data by their ID.



GET /courses/courses
This endpoint retrieves all the courses offered in the school.

POST /courses/courses
This endpoint registers a new course by admin.


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





