from models import Student, Classroom
from pydantic import ValidationError
import json
from pathlib import Path
from datetime import datetime

def create_student_interactive():
    """Interactive student creation with error handling"""
    print("\n📝 ADD NEW STUDENT")
    print("-" * 50)
    
    while True:
        try:
            name = input("Name: ").strip()
            age = int(input("Age (16-25): "))
            student_id = input("Student ID: ").strip()
            email = input("Email: ").strip()
            course = input("Course: ").strip()
            
            # Get grades
            grades_input = input("Grades (comma-separated, e.g., 85,90,78): ").strip()
            grades = [int(g.strip()) for g in grades_input.split(",")]
            
            # Create student
            student = Student(
                name=name,
                age=age,
                student_id=student_id,
                email=email,
                course=course,
                grades=grades,
                enrollment_date=datetime.now().strftime("%Y-%m-%d")
            )
            
            print("\n✅ Student created successfully!")
            return student
            
        except ValidationError as e:
            print("\n❌ Validation Error:")
            for error in e.errors():
                field = error['loc'][0]
                msg = error['msg']
                print(f"  - {field}: {msg}")
            print("\nPlease try again.\n")
            
        except ValueError as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.\n")

def save_classroom(classroom: Classroom, filename: str = "data/students.json"):
    """Save classroom data to JSON"""
    Path("data").mkdir(exist_ok=True)
    
    with open(filename, "w") as f:
        f.write(classroom.model_dump_json(indent=2))
    
    print(f"\n💾 Saved to {filename}")

def load_classroom(filename: str = "data/students.json") -> Classroom:
    """Load classroom data from JSON"""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return Classroom(**data)
    except FileNotFoundError:
        print("⚠️  No existing data found. Creating new classroom.")
        return None

def generate_report(classroom: Classroom):
    """Generate performance report"""
    print("\n" + "="*60)
    print(f"📊 CLASSROOM PERFORMANCE REPORT")
    print("="*60)
    print(f"\nCourse: {classroom.course_name}")
    print(f"Teacher: {classroom.teacher}")
    print(f"Semester: {classroom.semester}")
    print(f"\nTotal Students: {classroom.total_students}")
    print(f"Class Average: {classroom.class_average}%")
    print(f"Passing: {classroom.passing_count}/{classroom.total_students}")
    
    # Top students
    print(f"\n🏆 TOP STUDENTS:")
    for i, student in enumerate(classroom.get_top_students(), 1):
        print(f"  {i}. {student.name}: {student.average}% ({student.letter_grade})")
    
    # Struggling students
    struggling = classroom.get_struggling_students()
    if struggling:
        print(f"\n⚠️  STUDENTS NEEDING SUPPORT:")
        for student in struggling:
            print(f"  - {student.name}: {student.average}% ({student.letter_grade})")
    
    # Individual breakdown
    print(f"\n📋 INDIVIDUAL STUDENT BREAKDOWN:")
    print("-"*60)
    for student in sorted(classroom.students, key=lambda s: s.average, reverse=True):
        print(f"{student.name:20} | {student.student_id:10} | Avg: {student.average:5}% | Grade: {student.letter_grade} | {student.status}")
    
    print("="*60 + "\n")

def main():
    """Main program"""
    print("\n" + "="*60)
    print("🎓 STUDENT PERFORMANCE TRACKER")
    print("="*60)
    
    # Try to load existing data
    classroom = load_classroom()
    
    if not classroom:
        # Create new classroom
        course_name = input("\nCourse Name: ")
        teacher = input("Teacher Name: ")
        classroom = Classroom(course_name=course_name, teacher=teacher)
    
    while True:
        print("\n" + "-"*60)
        print("MENU:")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Generate Report")
        print("4. Add Grade to Student")
        print("5. Save & Exit")
        print("-"*60)
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            student = create_student_interactive()
            if student:
                classroom.students.append(student)
                print(f"\n📊 {student.name}'s Stats:")
                print(f"   Average: {student.average}%")
                print(f"   Letter Grade: {student.letter_grade}")
                print(f"   Status: {student.status}")
        
        elif choice == "2":
            if not classroom.students:
                print("\n⚠️  No students in classroom yet.")
            else:
                print(f"\n📚 STUDENTS IN {classroom.course_name}:")
                print("-"*60)
                for i, student in enumerate(classroom.students, 1):
                    print(f"{i}. {student.name} ({student.student_id}) - Avg: {student.average}%")
        
        elif choice == "3":
            if not classroom.students:
                print("\n⚠️  No students to report on.")
            else:
                generate_report(classroom)
        
        elif choice == "4":
            if not classroom.students:
                print("\n⚠️  No students in classroom.")
            else:
                print("\nStudents:")
                for i, s in enumerate(classroom.students, 1):
                    print(f"{i}. {s.name}")
                
                try:
                    idx = int(input("\nSelect student number: ")) - 1
                    grade = int(input("Enter new grade (0-100): "))
                    
                    classroom.students[idx].add_grade(grade)
                    print(f"✅ Added grade {grade}")
                    print(f"New average: {classroom.students[idx].average}%")
                except (ValueError, IndexError) as e:
                    print(f"❌ Invalid input: {e}")
        
        elif choice == "5":
            save_classroom(classroom)
            print("\n👋 Goodbye!")
            break
        
        else:
            print("\n❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()