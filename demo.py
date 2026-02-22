# demo.py - Quick test without the full CLI
from models import Student, Classroom

# Create some students
student1 = Student(
    name="Sameer Ahmed",
    age=18,
    student_id="AE2025",
    email="sameer@university.edu",
    grades=[85, 92, 88, 90],
    course="Aerospace Engineering"
)

student2 = Student(
    name="Ali Khan",
    age=19,
    student_id="AE2024",
    email="ali@university.edu",
    grades=[78, 82, 75, 80],
    course="Aerospace Engineering"
)

student3 = Student(
    name="Sara Ahmed",
    age=18,
    student_id="AE2026",
    email="sara@university.edu",
    grades=[95, 98, 92, 96],
    course="Aerospace Engineering"
)

# Create classroom
classroom = Classroom(
    course_name="Introduction to Python",
    teacher="Dr. Smith",
    students=[student1, student2, student3]
)

# Display info
print(f"\n📚 Course: {classroom.course_name}")
print(f"👨‍🏫 Teacher: {classroom.teacher}")
print(f"👥 Total Students: {classroom.total_students}")
print(f"📊 Class Average: {classroom.class_average}%")

print("\n🏆 Top Students:")
for s in classroom.get_top_students():
    print(f"  - {s.name}: {s.average}% ({s.letter_grade})")

# Export to JSON
print("\n💾 Exporting to JSON...")
with open("classroom_demo.json", "w") as f:
    f.write(classroom.model_dump_json(indent=2))

print("✅ Saved to classroom_demo.json")