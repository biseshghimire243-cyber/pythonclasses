class Patient:

    def __init__(self, name, age, problem):
        self.name = name
        self.age = age
        self.problem = problem

    def show_patient(self):

        print("Name:", self.name)
        print("Age:", self.age)
        print("Problem:", self.problem)


class Doctor:

    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def show_doctor(self):

        print("Doctor:", self.name)
        print("Specialization:", self.specialization)


class Appointment:

    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def show_appointment(self):

        print("\n========== APPOINTMENT ==========")

        print("Patient:", self.patient.name)
        print("Doctor:", self.doctor.name)
        print("Date:", self.date)


patient = Patient(
    "Bishesh",
    23,
    "General Checkup"
)

doctor = Doctor(
    "Dr. Sharma",
    "General Physician"
)

appointment = Appointment(
    patient,
    doctor,
    "2026-08-20"
)

patient.show_patient()

print()

doctor.show_doctor()

appointment.show_appointment()