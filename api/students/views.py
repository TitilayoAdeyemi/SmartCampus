from flask_restx import Namespace, Resource, fields, Api
from flask_jwt_extended import jwt_required
from models.students import Student
from models.courses import Courses
from models.students_courses import StudentCourse
from http import HTTPStatus
from utils import db



student_namespace = Namespace('students' ,description='A namespace for students')

student_model = student_namespace.model(
    'Student', {
    'student_name' : fields.String(required = True, description = "Student's name"),
    'student_email' : fields.String(required = True, description = "Student's email account"),
    'department' : fields.String(required = True, description = "Student's department"),
    'matric_no' : fields.Integer(required = True, description = "Student's matric number"),
    'courses_registered' : fields.String(required = True, description = "Student's courses")
    }
)



course_model = student_namespace.model(
    'Course', {
    'id' : fields.Integer(required = True, description = 'Course unique id'),
    'course_code' : fields.String(required = True, description = 'Course code'),
    'course_unit' : fields.Integer(required = True, description = 'Course units'),
    'lecturer_name' : fields.String(required = True, description = 'Lecturer for a particular course'),
    'course_description' : fields.String(required = True, description = "Course description")
    }
)

@student_namespace.route('/students')
class GetAndAddStudents(Resource):           
    @student_namespace.marshal_with(student_model)
    @student_namespace.doc(description = 'Retrieves all students')
    @jwt_required()
    def get(self):
        """Get all students"""
        orders=Student.query.all()

        return orders, HTTPStatus.OK
    


    def post():
        """Register a student for a course"""
        student = student_namespace.payload['student']
        course = student_namespace.payload['course']

        student_namespace.add_resource

        student_namespace.add_resource(StudentCourse, '/students')

    

        return {'message': f'{student["name"]} has been registered for {course["name"]}'}
    

@student_namespace.route('/students/<int:student_id>')
class GetUpdateDeleteStudent(Resource):
    @student_namespace.marshal_with(student_model)
    @student_namespace.doc(
    description = 'Retrieves a student by its ID',
    params = {
        'student_id' : 'An ID for a given student'
        }
            )
    @jwt_required()
    def get(self, student_id):
        """Retrieves a student by id"""
        

        student = Student.get_by_id(student_id)

        return student, HTTPStatus.OK
    


    @student_namespace.expect(student_model)
    @student_namespace.doc(
        description = 'Update a student info given a student id',
        params = {
        'student_id' : 'An ID for a given student'
        }
        )
    @student_namespace.marshal_with(student_model)
    @jwt_required()
    def put(self, student_id):
        """Updates a student using is id"""
        update_student = Student.get_by_id(student_id)

        data = student_namespace.payload

        update_student.student_name = data['student_name']
        update_student.student_email = data['student_email']
        update_student.department = data['department']
        update_student.martic_no = data['martic_no']
        update_student.courses_registered = data['courses_registered']

        db.session.commit()

        return update_student, HTTPStatus.OK



    @jwt_required()
    @student_namespace.doc(
        description = 'Deletes a student using its id',
        params = {
        'student_id' : 'An ID for a given student'
        }
        )
    @student_namespace.marshal_with(student_model)
    def delete(self, student_id):
        """Deletes an student using its id"""

        student_to_delete = Student.get_by_id(student_id)

        student_to_delete.delete()

    

        return student_to_delete, HTTPStatus.NO_CONTENT







@student_namespace.route('/students/<int:student_id>/courses')
class GetStudentsCourses(Resource):
    def get(self, student_id):
        """Gets all courses registered by a student using student id"""
        courses = StudentCourse.get(student_id)
        response = []

        for course in courses:
            student_course = {}
            student_course['id'] = course.id
            student_course['course_code'] = course.course_code
            student_course['course_unit'] = course.course_unit
            student_course['course_description'] = course.course_description

            response.append(student_course)

        return response, HTTPStatus.OK








