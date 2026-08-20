Hospital Management System

A professional Hospital Management System REST API built with Django and Django REST Framework. The system provides a centralized backend for managing patients, doctors, nurses, departments, rooms, hospitalizations, laboratory records, prescriptions, prescription medicines, and billing.

The project implements JWT authentication, role-based authorization, custom permissions, filtering, searching, ordering, pagination, validation, and Swagger/OpenAPI documentation.

Project Overview

The Hospital Management System is designed to digitize and simplify hospital operations through a secure and structured REST API.

The system allows different hospital users to access and manage information according to their assigned roles.

Main Objectives
Digitize hospital management operations
Provide a secure RESTful API
Implement role-based access control
Protect patient-specific data
Manage hospital resources from a centralized system
Support filtering, searching, ordering, and pagination
Provide interactive API documentation
Maintain data integrity through validation
Provide a modular and maintainable backend architecture
Features
Authentication and Authorization
Custom User model
User registration
User login
JWT authentication
Access and refresh tokens
Logout functionality
Token blacklisting
Role-based permissions
Protected API endpoints
User Roles
Role	Access
Admin	Full system access
Doctor	Access to relevant medical and patient records
Nurse	Access to operational hospital and patient information
Patient	Access only to their own records
Modules
1. Accounts

Handles authentication and user management.

Features
User registration
User login
JWT authentication
Logout
User roles
Custom permissions
2. Patients

Manages patient information and profiles.

Features
Patient registration
Patient profiles
CNIC validation
Phone number validation
Role-based access
Patient-specific data filtering

Patients can only access their own relevant records.

3. Doctors

Manages doctor information and professional details.

Doctor Information
User account
Department
Specialization
License number
Qualification
Experience

Doctors can access their own profile and relevant medical records according to their permissions.

4. Nurses

Manages hospital nursing staff.

Nurse Information
User account
Department
CNIC
Nurse number
Profile picture

Nurses can access hospital information required for their role.

5. Departments

Manages hospital departments.

Department Information
Department name
Description
Location
Phone number
Active/inactive status
Created date
Updated date
6. Rooms

Manages hospital rooms.

Features
Unique room numbers
Room types
Room status
Department assignment
Room capacity

Example room statuses include:

Available
Occupied
Maintenance
7. Hospitalization

Manages patient admissions and hospital stays.

Features
Patient admission
Admission type
Department
Room
Admission date
Discharge date
Hospitalization status
Admission Types
Emergency
Scheduled
Referral
Validation

The system validates that:

Discharge date cannot be earlier than admission date
Selected room belongs to the selected department

Patients can view their own hospitalization records while authorized staff can access broader hospitalization data.

8. Laboratory

Manages laboratory test records.

Information
Patient
Doctor
Test information
Test status
Results

Access is controlled based on the user's role.

Patients can view their own laboratory records, while doctors and authorized staff can access relevant laboratory information.

9. Prescriptions

Manages patient prescriptions.

Features
Patient association
Doctor association
Prescription management
Role-based access
Create/update/delete restrictions
Patient-specific prescription access

Doctors can manage prescriptions according to their permissions, while patients can view their own prescriptions.

10. Prescription Medicines

Manages medicines associated with prescriptions.

Information
Prescription
Medicine name
Dosage
Frequency
Duration
Instructions

Access is restricted according to the user's role and prescription ownership.

11. Billing

Manages hospital billing information.

Features
Billing records
Bill items
Role-based access
Protected billing operations
Administrative control
Role-Based Access Control

A major feature of this project is role-based authorization.

Authentication alone does not determine what a user can access. The system also checks the user's role and, where required, filters the queryset according to ownership.

Admin

Administrators have the highest level of access.

They can manage:

Users
Patients
Doctors
Nurses
Departments
Rooms
Hospitalizations
Laboratory records
Prescriptions
Prescription medicines
Billing
Doctor

Doctors can access information relevant to their work, such as:

Their doctor profile
Relevant patients
Laboratory records
Prescriptions
Medical information permitted by the system
Nurse

Nurses can access operational hospital information, including permitted:

Patient records
Rooms
Hospitalizations
Laboratory information
Other hospital resources
Patient

Patients have restricted access and can view their own:

Patient profile
Hospitalization records
Laboratory records
Prescriptions
Prescription medicines
Other permitted personal records

This prevents patients from accessing another patient's private information.

Custom Permissions

The project uses custom Django REST Framework permission classes.

Examples include:

IsAdmin
IsDoctor
IsNurse
IsPatient
IsAdminOrDoctor
CanViewPatient
CanViewLaboratory
CanViewPrescription
CanViewBilling

Permissions are combined with queryset filtering.

For example:

if user.role == User.Role.PATIENT:
    return Model.objects.filter(patient__user=user)

This ensures that patients can only retrieve records belonging to themselves.

Filtering, Search and Ordering

The API supports filtering, searching, and ordering using Django REST Framework and django-filter.

Filtering

Example:

/api/patients/?gender=MALE
Search

Example:

/api/patients/?search=Ali
Ordering

Ascending:

/api/patients/?ordering=created_at

Descending:

/api/patients/?ordering=-created_at

These features make it easier to work with large datasets.

Pagination

The project uses a custom DRF pagination class.

Instead of returning all records at once, the API divides records into pages.

Example:

/api/patients/?page=2

Pagination improves:

API performance
Response size
Frontend usability
Scalability
API Documentation

The project uses drf-spectacular for OpenAPI schema generation and Swagger documentation.

Swagger allows developers to:

View available endpoints
View request parameters
View serializers
Test API endpoints
Authenticate using JWT
Inspect API responses

Typical documentation routes are:

/api/schema/
/api/docs/

The exact URLs depend on the project's URL configuration.

JWT Authentication

The project uses JSON Web Tokens for authentication.

Authentication Flow
Register
   |
   v
Login
   |
   v
Access Token + Refresh Token
   |
   v
Authenticated API Requests
   |
   v
Refresh Token
   |
   v
Logout / Token Blacklist

Authenticated requests use:

Authorization: Bearer <access_token>
Project Architecture

The project follows a modular Django application architecture.

HospitalManagementSystem/
|
├── manage.py
|
├── HospitalManagementSystem/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
|
├── accounts/
├── patients/
├── doctors/
├── nurse/
├── departments/
├── rooms/
├── hospitalization/
├── laboratory/
├── prescriptions/
├── prescription_medicine/
├── billing/
|
└── ...

Each Django application is responsible for a specific hospital domain.

This makes the project:

Modular
Maintainable
Scalable
Easier to debug
Easier to extend
Data Relationships

Simplified relationships between the major entities:

User
 ├── Patient
 ├── Doctor
 └── Nurse


Department
 ├── Doctors
 ├── Nurses
 └── Rooms


Patient
 ├── Hospitalizations
 ├── Laboratory Records
 ├── Prescriptions
 └── Billing


Doctor
 ├── Laboratory Records
 └── Prescriptions


Prescription
 └── Prescription Medicines


Hospitalization
 ├── Patient
 ├── Department
 └── Room
Hospital Workflow

A typical hospital workflow can look like this:

User Registration
       |
       v
Authentication
       |
       v
Patient Registration
       |
       v
Doctor Assignment
       |
       v
Department Selection
       |
       v
Room Assignment
       |
       v
Hospitalization
       |
       v
Laboratory Tests
       |
       v
Prescription
       |
       v
Prescription Medicines
       |
       v
Billing
       |
       v
Discharge
Validation

The system contains validation to maintain data integrity.

The system validates:

Discharge date cannot be before admission date
Room must belong to the selected department

These validations prevent invalid hospital records.

Technologies Used
Backend
Python
Django
Django REST Framework
django-filter
Simple JWT
drf-spectacular
SQLite for development
API Features
RESTful APIs
ModelViewSet
DefaultRouter
JWT authentication
Custom permissions
Filtering
Searching
Ordering
Pagination
Swagger/OpenAPI
Installation
1. Clone the Repository
git clone https://github.com/waqaralisoomro915-cloud/Hospital_Management_System.git
cd HospitalManagementSystem
2. Create Virtual Environment
Windows
python -m venv .venv

Activate:

.venv\Scripts\activate
Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies

If requirements.txt exists:

pip install -r requirements.txt

You can generate it with:

pip freeze > requirements.txt
4. Configure Environment Variables

Create a .env file if your project uses environment variables.

Example:

SECRET_KEY=your-secret-key
DEBUG=True

Never commit sensitive information such as:

Secret keys
Passwords
API keys
Database credentials
Email credentials

Add .env to .gitignore.

5. Run Migrations
python manage.py makemigrations
python manage.py migrate
6. Create Superuser
python manage.py createsuperuser

Follow the prompts.

7. Start Server
python manage.py runserver

The development server will normally be available at:

http://127.0.0.1:8000/
API Testing

The API can be tested using:

Swagger UI
Postman
Insomnia
Thunder Client
cURL
Frontend applications

Example:
curl http://127.0.0.1:8000/api/
For authenticated endpoints:
Authorization: Bearer <access_token>
API Endpoint Structure

The project follows RESTful endpoint conventions.

Examples:
/api/accounts/
/api/patients/
/api/doctors/
/api/nurses/
/api/departments/
/api/rooms/
/api/hospitalizations/
/api/laboratories/
/api/prescriptions/
/api/prescription-medicines/
/api/billing/
The exact URLs depend on your router configuration.

Security
Security-related features include:
JWT authentication
Authenticated endpoints
Role-based authorization
Custom permission classes
User-specific querysets
Protected delete operations
Data ownership restrictions
Django password hashing
Token blacklisting
Serializer and model validation

For production deployment, configure:
DEBUG=False

and use:

HTTPS
Strong secret keys
Environment variables
Production database
Secure CORS configuration
Secure cookies where applicable
Proper logging
Production server configuration
Scalability

The system is structured to support future expansion.
Pagination, filtering, search, and ordering help reduce unnecessary API responses and improve performance as the number of records increases.
The modular Django architecture also makes it possible to add new hospital modules without restructuring the entire project.

Future Improvements

Potential future extensions include:
React frontend
Flutter mobile application
PostgreSQL
Docker
Automated testing
CI/CD
Appointment management
Pharmacy management
Inventory management
Email notifications
SMS notifications
Medical records
Blood bank management
Ambulance management
Staff attendance
Advanced reporting
Analytics dashboards
Audit logging
Cloud deployment
Project Structure

HospitalManagementSystem/
|
├── accounts/
├── billing/
├── departments/
├── doctors/
├── hospitalization/
├── laboratory/
├── nurse/
├── patients/
├── prescription_medicine/
├── prescriptions/
├── rooms/
|
├── HospitalManagementSystem/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

The core Hospital Management System backend has been implemented.
Implemented Features
Authentication
JWT authentication
Custom User Model
Role-based authorization
Patients
Doctors
Nurses
Departments
Rooms
Hospitalization
Laboratory
Prescriptions
Prescription Medicines
Billing
CRUD APIs
Custom permissions
Queryset-level access control
Validation
Pagination
Filtering
Search
Ordering
Swagger/OpenAPI documentation
Learning Outcomes

This project demonstrates practical experience with:
Django
Django REST Framework
REST API development
JWT authentication
Custom User Models
Role-Based Access Control
Django ORM
Model relationships
Queryset filtering
Custom permissions
Serializer validation
Model validation
Pagination
Searching
Filtering
Ordering
Swagger/OpenAPI
Database migrations
API architecture
Git/GitHub
Author
Waqar Ali

Software Engineer | Django & Flutter Developer | Python | SQL | AI/ML
Passionate about building scalable backend systems, REST APIs, mobile applications, and AI-powered software solutions.

Support
If you find this project useful for learning Django, Django REST Framework, or backend development, consider giving the repository a star on GitHub.

License
This project can be released under the MIT License.

Acknowledgements
Built using the Django ecosystem and open-source Python technologies.
Django, Django REST Framework, Simple JWT, django-filter, and drf-spectacular.
