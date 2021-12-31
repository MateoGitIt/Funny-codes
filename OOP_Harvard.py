import random
import logging
import time


class Applicant:

    def __init__(self, full_name, gpa, nationality, sat, act, good_extras,
                 uniqueness, target):

        self.full_name = full_name
        self.gpa = gpa
        self.nationality = nationality
        self.sat = sat
        self.act = act
        self.good_extras = good_extras
        self.uniqueness = uniqueness
        self.target = target
        self.is_accepted = None
        self.is_waitlist = None
        self.is_rejected = None

    def get_sat(self):
        return self.sat

    def get_act(self):
        return self.act

    def get_gpa(self):
        return self.gpa

    def get_nation(self):
        return self.nationality

    def get_gextras(self):
        return self.good_extras

    def get_uniq(self):
        return self.uniqueness

    def get_tarcourse(self):
        return self.target

    def waitlist(self):
        return self.is_waitlist

    def acceptance(self):
        return self.is_accepted

        # Full name selection -> Person generator list of names.


def choose_ran_name(a):
    chosen_name = random.choice(a)
    return chosen_name


names_list = ["Diego", "Eda", "Christopher", "Velva", "Zina", "Voncile",
              "Wally", "Deirdre", "Van", "Kent", "Erinn", "Orville", "Zane",
              "Malia", "Audria", "Rebekah", "Violet", "Milan", "Franklyn",
              "Brenda", "Tricia", "Mateo"]

# GPA selection


def chosen_ran_gpa():
    chosen_gpa = random.uniform(2, 5)
    return chosen_gpa


# Nationality selection

nat_list = ["United States", "Colombia", "Canada", "Mexico", "Spain",
            "Ethiopia", "Australia", "Argentina", "United Kingdom"]


def chosen_ran_nat(nations):
    chosen_nat = random.choice(nations)
    return chosen_nat

# SAT selection


def chosen_ran_sat():
    chosen_sat = random.randint(1000, 1600)
    return chosen_sat

# ACT selection


def chosen_ran_act():
    chosen_act = random.randint(20, 35)
    return chosen_act


# Good extracurriculars are determined by your GPA, SAT and ACT average.

elements_used = [chosen_ran_sat(), chosen_ran_gpa(),
                 chosen_ran_act()]


def average_calculations(elements):
    average = sum(elements) / len(elements)
    if average >= 400:
        return True
    elif average <= 399:
        return False


# Uniqueness selection...


def ran_uniqueness():

    if average_calculations(elements_used):
        uniqueness = True
    else:
        uniqueness = False
    return uniqueness

# Course selection


courses_list = ["Computer Sciences", "Physics", "E. engineering",
                "Economics", "Law School"]


def ran_course(x):
    chosen_course = random.choice(x)
    return chosen_course


# Students


s1 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s2 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s3 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s4 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s5 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s6 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s7 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s8 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s9 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s10 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s11 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s12 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s13 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s14 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s15 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s16 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s17 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s18 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s19 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s20 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s21 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s22 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s23 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s24 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

s25 = Applicant(choose_ran_name(names_list), chosen_ran_gpa(),
               chosen_ran_nat(nat_list), chosen_ran_sat(), chosen_ran_act(),
               average_calculations(elements_used), ran_uniqueness(),
               ran_course(courses_list))

# Only accepted students are inside the course. Uniqueness is the first filter.


class Course:

    def __init__(self, max_students, min_sat, min_act, min_gpa):
        self.max_students = max_students
        self.min_sat = min_sat
        self.min_act = min_act
        self.min_gpa = min_gpa
        self.students_enrolled = []

    def log(self, name, location):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s / %(levelname)s /"
                                      "%(message)s")
        if logger.hasHandlers():
            logger.handlers.clear()
        file_handler = logging.FileHandler(location)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

# For logging to different files, always use a setup function with parameters
# name (name of the logger) and location (log file) and clear handlers.

    def add_attempt(self, student):
        if len(self.students_enrolled) < self.max_students:
            if student.uniqueness:
                if student.sat() > self.min_sat:  # Don't forget parenthesis
                    if student.act() > self.min_act:
                        if student.gpa() > self.min_gpa:
                            student.is_accepted = True
                            self.students_enrolled.append(student)
                            print("")
                            print(f"{student.full_name} has "
                                  f"been accepted to {student.target}."
                                  " Congratulations, welcome to"
                                  " Harvard University!")
                            time.sleep(0.1)
                            self.log("accepted_lgr", "Accepted_log").info(
                                            f"{student.full_name} accepted to "
                                            f"{student.target}.")
                            time.sleep(0.1)

                        else:
                            student.is_waitlist = True
                            student.is_accepted = False
                            print("")
                            print(f"{student.full_name} has"
                                  " been added to the waitlist of "
                                  f"{student.target}.You will be notified for"
                                  " any change.")
                            time.sleep(0.1)
                            self.log("waitlist_lgr", "Waitlist_log").info(
                                            f"{student.full_name} in waitlist"
                                            f" for {student.target}")
                            time.sleep(0.1)

                            if len(self.students_enrolled) < self.max_students:
                                student.is_waitlist = False
                                student.is_accepted = True
                                self.students_enrolled.append(student)
                                print(f"{student.full_name} has been accepted "
                                      f"to {student.target} from the wailist. "
                                      "Congratulations, welcome to Harvard"
                                      " University!")
                                self.log("accepted_lgr", "Accepted_log").info(
                                         f"{student.full_name} accepted from "
                                         f"the waitlist to {student.target}.")
                    else:
                        student.is_accepted = False
                        student.is_waitlist = False
                        print("")
                        print(f"We are sorry to inform "
                              f"{student.full_name} has not been"
                              f" accepted to {student.target}.")
                        time.sleep(0.1)
                        self.log("rejected_lgr", "Rejected_log").info(
                                        f"{student.full_name} rejected from "
                                        f"{student.target}.")
                        time.sleep(0.1)
                else:
                    student.is_accepted = False
                    student.is_waitlist = False
                    print("")
                    print(f"We are sorry to inform {student.full_name}"
                          f" has not been accepted to {student.target}.")
                    time.sleep(0.1)
                    self.log("rejected_lgr", "Rejected_log").info(
                                    f"{student.full_name} rejected from "
                                    f"{student.target}")
                    time.sleep(0.1)
            else:
                student.is_accepted = False
                student.is_waitlist = False
                print("")
                print(f"We are sorry to inform {student.full_name}"
                      f" has not been accepted to {student.target}.")
                time.sleep(0.1)
                self.log_rejected("rejected_lgr", "Rejected_log").info(
                                f"{student.full_name} rejected from "
                                f"{student.target}")
                time.sleep(0.1)

        else:
            x = len(self.students_enrolled)
            print("")
            print(f"{x} students have enrolled already. The maximum amount of"
                  f" students for {student.target} has been reached.")


# Adding students to courses attempts


course1 = Course(5, 1350, 25, 3.5)
course2 = Course(4, 1450, 28, 3.5)
course3 = Course(3, 1550, 32, 3.8)
course4 = Course(2, 1300, 30, 3.3)
course5 = Course(6, 1390, 30, 3.5)


course1.add_attempt(s1)
course2.add_attempt(s2)
course5.add_attempt(s3)
course3.add_attempt(s4)
course4.add_attempt(s5)

course5.add_attempt(s6)
course3.add_attempt(s7)
course2.add_attempt(s8)
course4.add_attempt(s9)
course1.add_attempt(s10)

course2.add_attempt(s11)
course4.add_attempt(s12)
course5.add_attempt(s13)
course1.add_attempt(s14)
course3.add_attempt(s15)

course4.add_attempt(s16)
course4.add_attempt(s17)
course1.add_attempt(s18)
course2.add_attempt(s19)
course3.add_attempt(s20)

course5.add_attempt(s21)
course1.add_attempt(s22)
course2.add_attempt(s23)
course4.add_attempt(s24)
course3.add_attempt(s25)
