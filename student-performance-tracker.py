class Student:
    def __init__(self, name, scores):
        """
        Initialize a Student object with a name and scores.
        :param name: str - Name of the student
        :param scores: list - List of scores in subjects
        """
        self.name = name
        self.scores = scores

    def calculate_average(self):
        """
        Calculate and return the average score of the student.
        :return: float - Average score
        """
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        """
        Check if the student is passing all subjects.
        :param passing_score: int - Minimum score to pass
        :return: bool - True if passing, False otherwise
        """
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        """
        Initialize a PerformanceTracker with an empty dictionary of students.
        """
        self.students = {}

    def add_student(self, name, scores):
        """
        Add a new student to the tracker.
        :param name: str - Name of the student
        :param scores: list - List of scores in subjects
        """
        if name in self.students:
            print(f"Student '{name}' already exists. Data not added.")
        else:
            self.students[name] = Student(name, scores)
            print(f"Student '{name}' added successfully.")

    def calculate_class_average(self):
        """
        Calculate and return the average score of the entire class.
        :return: float - Class average score
        """
        if not self.students:
            return 0
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)

    def display_student_performance(self):
        """
        Display the performance of each student, including their average score
        and whether they are passing or failing.
        """
        if not self.students:
            print("No student data available.")
            return

        print("\nStudent Performance:")
        print("-" * 40)
        for student in self.students.values():
            avg_score = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"Name: {student.name}")
            print(f"  Average Score: {avg_score:.2f}")
            print(f"  Status: {status}")
        print("-" * 40)


def main():
    tracker = PerformanceTracker()
    print("Welcome to the Student Performance Tracker!")
    print("Follow the prompts to add students and their scores.")

    while True:
        name = input("Enter the student's name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        try:
            scores = [
                int(input(f"Enter score for subject {i + 1}: ").strip())
                for i in range(3)
            ]
        except ValueError:
            print("Invalid input. Scores must be integers. Try again.")
            continue

        tracker.add_student(name, scores)

    print("\nData entry complete.")
    tracker.display_student_performance()

    class_avg = tracker.calculate_class_average()
    print(f"\nClass Average Score: {class_avg:.2f}")


if __name__ == "__main__":
    main()
