import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from ..models.students import Student
from ..models.courses import Courses
from flask_jwt_extended import create_access_token



class UserTestCase(unittest.TestCase):
    
    def setUp(self):

        self.app = create_app(config=config_dict['test'])

        self.appctx = self.app.app_context()

        self.appctx.push()

        self.client = self.app.test_client()

        db.create_all()
        

    def tearDown(self):

        db.drop_all()

        self.appctx.pop()

        self.app = None

        self.client = None


    def testStudent(self):

        #Register a student
        token = create_access_token(identity=student.id)

        
        headers = {
            "Authorization": f"Bearer {token}"
        }

        student_signup_data = {
            "student_name": "John Doe",
            "student_email": "johndoe@gmail.com",
            "department": "psychology",
            "password": "password",
            "matric_no": "101001"
        }

        response = self.client.post('/students/students', json=student_signup_data, headers=headers)

        student = Student.query.filter_by(email='johndoe@gmail.com').first()

        assert student.student_name == "John Doe"

        assert student.matric_no == "101001"

        assert response.status_code == 201


        #Retreive a student

        response = self.client.get('/students/students', headers=headers)

        assert response.status_code == 200

        assert response.json == [{
            "id": 2,
            "student_name": "John Doe",
            "student_email": "johndoe@gmail.com",
            "department": "psychology",
            "password": "password",
            "matric_no": "101001"
        }]





        # Update a student's details
        student_update_data = {
            "student_name": "Jane Doe",
            "student_email": "janedoe@gmail.com",
            "department": "Medical Lab Science",
            "password": "password",
        }

        response = self.client.put('/students/2', json=student_update_data, headers=headers)

        assert response.status_code == 200

        assert response.json == {
            "id": 2,
            "student_name": "Jane Doe",
            "student_email": "janedoe@gmail.com",
            "matric_no": "101001"
        }



        # Delete a student
        response = self.client.delete('/students/students/2', headers=headers)
        assert response.status_code == 200\
        


class CourseTestCase(unittest.TestCase):
    
    def setUp(self):

        self.app = create_app(config=config_dict['test'])

        self.appctx = self.app.app_context()

        self.appctx.push()

        self.client = self.app.test_client()

        db.create_all()


    def tearDown(self):

        db.drop_all()

        self.appctx.pop()

        self.app = None

        self.client = None


    def test_courses(self):
        # Register a course
    
        token = create_access_token(identity=lecturer.id)

        headers = {
            "Authorization": f"Bearer {token}"
        }

        course_registration_data = {
            "name": "Test Course",
            "lecturer": "Test lecturer"
        }

        response = self.client.post('/courses/courses', json=course_registration_data, headers=headers)

        assert response.status_code == 201

        courses = Courses.query.all()

        course_id = courses[0].id

        course_code = courses[0].name

        lecturer = courses[0].lecturer

        assert len(courses) == 1

        assert course_id == 1

        assert course_code == "Test Course"

        assert lecturer == "Test Teacher"



        # Get all courses
        response = self.client.get('/courses/courses', headers=headers)

        assert response.status_code == 200

        assert response.json == [{
            "id": 1,
            "name": "Test Course",
            "lecturer": "Test lecturer"            
        }]


        # Retrieve a course by ID
        response = self.client.get('/courses/courses/1', headers=headers)

        assert response.status_code == 200

        assert response.json == {
            "id": 1,
            "name": "Test Course",
            "lecturer": "Test lecturer"            
        }


        # Update a course's details
        course_update_data = {
            "name": "Sample Course",
            "lecurer": "Sample lecturer"
        }

        response = self.client.put('/courses/1', json=course_update_data, headers=headers)

        assert response.status_code == 200

        assert response.json == {
            "id": 1,
            "name": "Sample Course",
            "lecturer": "Sample lecturer"            
        }



        # Get all students enrolled for a course
        response = self.client.get('/courses/courses/1/students', headers=headers)

        assert response.status_code == 200

        assert response.json == [{
            "id": 2,
            "student_name": "John Doe",
            "student_email": "johndoe@gmail.com",
            "matric_no": "101001"
        }]



        # Delete a course
        response = self.client.delete('/courses/courses/1', headers=headers)
        assert response.status_code == 200