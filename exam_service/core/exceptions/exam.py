from .abc import AbstractException, NotFoundException, ConflictException


class ExamException(AbstractException):
    """Base exam exception."""


class ExamNotFoundException(ExamException, NotFoundException):
    """Exam not found."""

    detail = "Exam not found"


class ExamNameAlreadyExistsException(ExamException, ConflictException):
    """Exam name already exists."""

    auto_additional_info_fields = ["name"]

    detail = "Exam with name {name} already exists, please use another name"
