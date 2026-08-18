from rest_framework.permissions import BasePermission
from .models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.ADMIN
        )


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.DOCTOR
        )


class IsNurse(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.NURSE
        )


class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.PATIENT
        )


class CanViewPatient(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
                User.Role.ADMIN,
                User.Role.DOCTOR,
                User.Role.NURSE,
                User.Role.PATIENT,
            ]
        )

    def has_object_permission(self, request, view, obj):
        if request.user.role in [
            User.Role.ADMIN,
            User.Role.DOCTOR,
            User.Role.NURSE,
        ]:
            return True

        if request.user.role == User.Role.PATIENT:
            return obj.user == request.user

        return False


class IsAdminOrDoctor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
                User.Role.ADMIN,
                User.Role.DOCTOR,
            ]
        )

class CanViewDepartment(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
                User.Role.ADMIN,
                User.Role.DOCTOR,
                User.Role.NURSE,
                User.Role.PATIENT,
            ]
        )

class CanViewDoctor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
            User.Role.ADMIN,
            User.Role.DOCTOR,
            User.Role.NURSE,
            User.Role.PATIENT,

            ]
        )
class CanViewNurse(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
            User.Role.ADMIN,
            User.Role.DOCTOR,
            User.Role.NURSE,
            ]
        )
class CanViewRoom(BasePermission):
    def has_permission(self, request, view):
        return(
            request.user.is_authenticated
            and request.user.role in [
            User.Role.ADMIN,
            User.Role.DOCTOR,
            User.Role.NURSE,
            ]
        )

class CanViewHospitalization(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
            User.Role.ADMIN,
            User.Role.DOCTOR,
            User.Role.NURSE,
            User.Role.PATIENT,
            ]
        )

class CanViewLaboratory(BasePermission):
    def has_permission(self, request, view):
        return(
            request.user.is_authenticated
            and request.user.role in [
            User.Role.ADMIN,
            User.Role.DOCTOR,
            User.Role.NURSE,
            User.Role.PATIENT,
            ]
        )

class CanviewPrescription(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
            User.Role.ADMIN,
            User.Role.DOCTOR,
            User.Role.NURSE,
            User.Role.PATIENT,
            ]
        )

class CanViewPrescriptionMedicine(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
            User.Role.ADMIN,
            User.Role.DOCTOR,
            User.Role.NURSE,
            User.Role.PATIENT,
            ]
        )