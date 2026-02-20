#Prompt: Generate Python code for an OnlineCourse class with attributes:course_id, course_title, instructor, duration_hours, and enrolled_students.Include methods:display_details(), add_student(name), and show_updated_details().Create an object, enroll at least three students, and show updated details.
#TASK_A:
class OnlineCourse:
    def __init__(self, course_id, course_title, instructor, duration_hours):
        self.course_id = course_id
        self.course_title = course_title
        self.instructor = instructor
        self.duration_hours = duration_hours
        self.enrolled_students = []

    def display_details(self):
        print("\nCourse Details:")
        print("Course ID:", self.course_id)
        print("Course Title:", self.course_title)
        print("Instructor:", self.instructor)
        print("Duration (Hours):", self.duration_hours)
        print("Enrolled Students:", self.enrolled_students)

    def add_student(self, name):
        self.enrolled_students.append(name)

    def convert_duration(self):
        minutes = self.duration_hours * 60
        seconds = self.duration_hours * 3600
        print("Duration in Minutes:", minutes)
        print("Duration in Seconds:", seconds)


if __name__ == "__main__":
    # Dynamic input
    course_id = input("Enter Course ID: ")
    course_title = input("Enter Course Title: ")
    instructor = input("Enter Instructor Name: ")
    duration_hours = float(input("Enter Duration in Hours: "))

    course = OnlineCourse(course_id, course_title, instructor, duration_hours)

    n = int(input("Enter number of students to enroll: "))
    for _ in range(n):
        name = input("Enter student name: ")
        course.add_student(name)

    # Show updated details
    course.display_details()
    course.convert_duration()

        
#Task-B:
def convert_hours(hours):
    minutes = hours * 60
    seconds = hours * 3600
    return minutes, seconds


if __name__ == "__main__":
    hrs = float(input("Enter number of hours: "))
    mins, secs = convert_hours(hrs)

    print("Minutes:", mins)
    print("Seconds:", secs)
