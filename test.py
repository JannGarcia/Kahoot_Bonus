import unittest
from main import calculate_bonus_points, \
    POINTS_FOR_BEING_IN_TOP as k, \
    MAX_POINTS_PER_STUDENT as m, \
    MAX_STUDENTS_PER_REPORT as n

def create_report_row(player, rank=0):
    """Creates a report row with the given player and rank. Irrelevant data is set to 0, since they are not needed for the test."""
    return (rank, player, 0, 0, 0)

def create_report_rows_with_n_students(n):
    """Creates a list of report rows with the given amount of students. The students are named john.doe0, john.doe1, etc. and have a rank of 1, 2, etc."""
    return [create_report_row(f"john.doe{i}", i+1) for i in range(n)]

class TestCalculateBonusPoints(unittest.TestCase):

    """
    Definitions:
        n - Number of students who should receive bonus points
        k - Points for being in the top n students
        m - Maximum points a student can have
    """

    def test_calculate__one_student(self):
        name = "john.doe"; points = 0
        rows = [create_report_row(name)]
        points_dict = {name: points}

        calculate_bonus_points(rows, points_dict)

        self.assertEqual(points_dict[name], k, f"Student should receive {k} points for being in the top {n}. \n\t* Expected {k} points, got {points_dict[name]}")

    def test_calculate__multiple_students(self):
        rows = create_report_rows_with_n_students(n)
        points_dict = {}
        for i in range(n):
            name = f"john.doe{i}"
            points_dict[name] = 0

        calculate_bonus_points(rows, points_dict)

        for i in range(n):
            name = f"john.doe{i}"
            self.assertEqual(points_dict[name], k, f"Student should receive {k} points for being in the top {n}. \n\t* Expected {k} points, got {points_dict[name]}")

    def test_calculate__max_points(self):
        name = "john.doe"; points = m
        rows = [create_report_row(name)]
        points_dict = {name: points}

        calculate_bonus_points(rows, points_dict)

        self.assertEqual(points_dict[name], m, f"Student should not exceed {m} points. \n\t* Expected {m} points, got {points_dict[name]}")

    def test_calculate__ignores_students_with_max_points_from_count(self):
        rows = []
        points_dict = {}
        for i in range(n + 1):
            name = f"john.doe{i}"; points = 0
            rows.append(create_report_row(name))
            points_dict[name] = points

        # Set a student with max points
        points_dict["john.doe0"] = m

        calculate_bonus_points(rows, points_dict)

        for i in range(n + 1):
            name = f"john.doe{i}"

            # Check if the first student has the max points
            # The Nth + 1 student should have extra points, since the first student has max points
            if i == 0: self.assertEqual(points_dict[name], m, f"Students with max points should not receive bonus points. \n\t* Expected {m} points, got {points_dict[name]}")
            else: self.assertEqual(points_dict[name], k, f"Student should receive {k} points for being in the top {n}. \n\t* Expected {k} points, got {points_dict[name]}")


    def test_calculate__with_invalid_username(self):
        rows = [create_report_row("johndoe")]
        points_dict = {"johndoe": 0}

        calculate_bonus_points(rows, points_dict)

        self.assertEqual(points_dict["johndoe"], 0, f"Student with invalid username should not receive bonus points. \n\t* Expected 0 points, got {points_dict['johndoe']}")

    def test_calculate__ignores_invalid_usernames_from_count(self):
        rows = []
        points_dict = {}
        for i in range(n):
            name = f"john.doe{i}"; points = 0
            rows.append(create_report_row(name))
            points_dict[name] = points

        # Set an invalid username
        rows.insert(0, create_report_row("johndoe"))
        points_dict["johndoe"] = 0

        calculate_bonus_points(rows, points_dict)

        for i in range(n):
            name = f"john.doe{i}"
            self.assertEqual(points_dict[name], k, f"Student should receive {k} points for being in the top {n}. \n\t* Expected {k} points, got {points_dict[name]}")

        self.assertEqual(points_dict["johndoe"], 0, f"Student with invalid username should not receive bonus points. \n\t* Expected 0 points, got {points_dict['johndoe']}")


    def test_calculate__with_no_students(self):
        rows = []
        points_dict = {}

        calculate_bonus_points(rows, points_dict)

        self.assertEqual(points_dict, {}, "No students should be added to the points dictionary")

    def test_calculate__a_ton_of_students(self):
        rows = []
        points_dict = {}
        for i in range(1000):
            name = f"john.doe{i}"; points = 0
            rows.append(create_report_row(name))
            points_dict[name] = points

        calculate_bonus_points(rows, points_dict)

        for i in range(1000):
            name = f"john.doe{i}"

            if i < n:
                self.assertEqual(points_dict[name], k, f"Student should receive {k} points for being in the top {n}. \n\t* Expected {k} points, got {points_dict[name]}")

            else:
                self.assertEqual(points_dict[name], 0, f"Student should not receive bonus points. \n\t* Expected 0 points, got {points_dict[name]}")

    def test_calculate__with_a_ton_of_students_but_with_invalid_names_and_max_students(self):
        rows = []
        points_dict = {}
        for i in range(1000):
            name = f"john.doe{i}"; points = 0
            rows.append(create_report_row(name))
            points_dict[name] = points

        # Set an invalid username and place it at the top
        rows.insert(0, create_report_row("johndoe"))
        points_dict["johndoe"] = 0

        # Set a student with max points
        points_dict[f"john.doe{n//2}"] = m

        calculate_bonus_points(rows, points_dict)

        counter = 0

        for i in range(1000):
            name = f"john.doe{i}"

            if i == n//2:
                self.assertEqual(points_dict[name], m, f"Students with max points should not receive bonus points. \n\t* Expected {m} points, got {points_dict[name]}")

            elif counter < n:
                self.assertEqual(points_dict[name], k, f"Student should receive {k} points for being in the top {n}. \n\t* Expected {k} points, got {points_dict[name]}")
                counter += 1

            else:
                self.assertEqual(points_dict[name], 0, f"Student should not receive bonus points. \n\t* Expected 0 points, got {points_dict[name]}")

        self.assertEqual(points_dict["johndoe"], 0, f"Student with invalid username should not receive bonus points. \n\t* Expected 0 points, got {points_dict['johndoe']}")
        self.assertEqual(counter, n, f"Expected {n} students to receive bonus points, got {counter}")


if __name__ == '__main__':
    unittest.main()