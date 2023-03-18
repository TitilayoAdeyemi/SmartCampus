from flask import Flask, request
from flask_restx import Namespace, fields, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.users import User
from ..models.courses import Courses
from models.students_courses import StudentCourse
from http import HTTPStatus
from utils import db
from api.utils.decorators import admin_required
from werkzeug.exceptions import Conflict

course_namespace = Namespace('courses', description='A namespace for the courses')

course_model = course_namespace.model(
    'Course', {
    'id' : fields.Integer(required = True, description = 'Course unique id'),
    'course_code' : fields.String(required = True, description = 'Course code'),
    'course_unit' : fields.Integer(required = True, description = 'Course units'),
    # 'lecturer_name' : fields.String(required = True, description = 'Lecturer for a particular course'),
    'course_description' : fields.String(required = True, description = "Course description")
    }
)




@course_namespace.route('/courses/')
class RegisterCourses(Resource):
    @course_namespace.marshal_with(course_model)
    @course_namespace.doc(description = 'Get all courses')
    @jwt_required()
    def get(self):
        """Get all Courses"""
        courses = Courses.query.all()

        return courses, HTTPStatus.OK


    @course_namespace.expect(course_model)
    @course_namespace.doc(description='Register for a course')
    @course_namespace.marshal_with(course_model)
    @jwt_required()
    @admin_required()
    def post(self):
        """Register a course """

        name=get_jwt_identity()


        current_user=User.query.filter_by(name=name).first()

        data = request.json

        new_course=Courses(
            course_code=data['course_code'],
            course_unit=data['course_unit'],
            course_description=data['course_description']
        )

        new_course.user=current_user
        
        new_course.save()

        return new_course, HTTPStatus.CREATED



@course_namespace.route('/courses/<int:course_id>/students')
class GetStudentsForACourse(Resource):
    @course_namespace.marshal_with(course_model)
    @course_namespace.doc(description = 'Retrieve all students registered for a course')
    @jwt_required()
    def get(self, course_id):
        """Get all Students registered for a course"""
    
        course = Courses.get_by_id(course_id)

        students_registered = course.students_registered
        
        return students_registered, HTTPStatus.OK



@course_namespace.route('/courses/<int:course_id>')
class GetUpdateDeleteCourse(Resource):
    
    @course_namespace.marshal_with(course_model)
    @course_namespace.doc(
        description = "Retrieve a Course's Details by ID - Admins Only",
        params = {
            'course_id': "The Course's ID"
        }
    )
    @admin_required()
    def get(self, course_id):
        """
            Retrieve a Course by ID - Admins Only
        """
        course = Courses.get_by_id(course_id)
        
        return course, HTTPStatus.OK
    
    @course_namespace.expect(course_model)
    @course_namespace.marshal_with(course_model)
    @course_namespace.doc(
        description = "Update a Course by ID - Admins Only",
        params = {
            'course_id': "The Course's ID"
        }
    )
    @admin_required()
    def put(self, course_id):
        """
            Update a Course by ID - Admins Only
        """
        updated_course = Courses.get_by_id(course_id)

        data = course_namespace.payload

        updated_course.course_code = data['course_code']
        updated_course.course_unit = data['course_unit']
        updated_course.course_description = data['course_description']

        db.session.commit()

        return updated_course, HTTPStatus.OK
    
    @course_namespace.doc(
        description = "Delete a Course by ID - Admins Only",
        params = {
            'course_id': "The Course's ID"
        }
    )
    @admin_required()
    def delete(self, course_id):
        """
            Delete a Course by ID - Admins Only
        """
        course = Courses.get_by_id(course_id)

        course.delete()

        return {"message": "Course Successfully Deleted"}, HTTPStatus.OK




@course_namespace.route('/courses/<int:course_id>/students')
class GetAllCourseStudents(Resource):

    @course_namespace.doc(
        description = "Get all Students Enrolled for a Course - Admins Only",
        params = {
            'course_id': "The Course's ID"
        }
    )
    @admin_required()
    def get(self, course_id):
        """
            Get all Students Enrolled for a Course - Admins Only
        """
        students = StudentCourse.get_students_in_course(course_id)
        response = []

        for student in students:
            student_resp = {}
            student_resp['id'] = student.id
            student_resp['name'] = student.name
            student_resp['department'] = student.department
            student_resp['matric_no'] = student.matric_no

            response.append(student_resp)

        return response, HTTPStatus.OK
    

