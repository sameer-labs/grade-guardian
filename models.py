from pydantic import BaseModel, Field, field_validator, computed_field
from typing import Optional, List
from datetime import datetime

class Student(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=16, le=25)
    student_id: str = Field(min_length=5, max_length=10)
    email: str
    grades: List[int]
    course: str = "General Studies"
    enrollment_date: Optional[str] = None

    model_config = {
        "extra": "forbid",
        "str_strip_whitespace": True
    }

    @field_validator("grades")
    @classmethod
    def validate_grades(cls, grades):
        if not grades:
            raise ValueError("Grades list cannot be empty.")
        
        for g in grades:
            if g < 0 or g > 100:
                raise ValueError(f"Grade {g} is invalid. Must be between 0-100")
        
        return grades
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, email):
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")
        return email.lower()
    
    @field_validator("student_id")
    @classmethod
    def validate_student_id(cls, student_id):
        if not student_id.isalnum():
            raise ValueError("Student ID must be alphanumeric.")
        return student_id.upper()
    
    @computed_field
    @property
    def average(self) -> float:
        # Calculate grade average
        return round(sum(self.grades) / len(self.grades), 2) 

    
    @computed_field
    @property
    def letter_grade(self) -> str:
        # Convert average grade to letter grade
       avg = self.average
       if avg >= 90:
           return "A"
       elif avg >= 80:
           return "B"
       elif avg >= 70:
           return "C"
       elif avg >= 60:
           return "D"
       else:
           return "F"
       
    @computed_field
    @property
    def status(self) -> str:
        # Determine pass/fail status
        return "Passing" if self.average >= 60 else "Failing"
    
    def add_grade(self, grade: int):
        # Add a new grade to the student's record
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0-100.")
        self.grades.append(grade)

    class Classroom(BaseModel):
        # Collection of students in a classroom
        course_name: str
        teacher: str
        students: List[Student] = []
        semester: str = "Spring 2025"

        @computed_field
        @property
        def class_average(self) -> float:
            # Calculate class average
            if not self.students:
                return 0.0
            return round(sum(s.average for s in self.students) / len(self.students), 2)
        
        @computed_field
        @property
        def total_students(self) -> int:
            # Count total students
            return len(self.students)
        
        @computed_field
        @property
        def passing_count(self) -> int:
            # Count passing students
            return sum(1 for s in self.students if s.average >= 60)
        
        def get_top_student(self, n: int = 3) -> List[Student]:
            # Get top N students by average grade
            return sorted(self.students, key=lambda s: s.average, reverse=True)[:n]
        
        def get_struggling_students(self) -> List[Student]:
            # Get students with average < 60
            return [s for s in self.students if s.average < 60]
        
