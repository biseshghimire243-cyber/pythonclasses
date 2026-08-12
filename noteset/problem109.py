doctors = {}
appointments = {}


def add_doctor():

    doctor_id = input("Doctor ID: ")

    if doctor_id in doctors:
        raise Exception("Doctor already exists.")

    name = input("Doctor Name: ")
    specialization = input("Specialization: ")

    doctors[doctor_id] = {
        "Name": name,
        "Specialization": specialization
    }

    print("Doctor added successfully.")


def view_doctors():

    if len(doctors) == 0:
        print("No doctors available.")
        return

    print("\n========== DOCTORS ==========")

    for doctor_id, doctor in doctors.items():

        print("-----------------------------")
        print("ID:", doctor_id)
        print("Name:", doctor["Name"])
        print("Specialization:", doctor["Specialization"])


def book_appointment():

    doctor_id = input("Doctor ID: ")

    if doctor_id not in doctors:
        raise Exception("Doctor not found.")

    patient = input("Patient Name: ")
    date = input("Appointment Date: ")
    time = input("Appointment Time: ")

    appointment_id = "A" + str(len(appointments) + 1)

    appointments[appointment_id] = {
        "Doctor": doctors[doctor_id]["Name"],
        "Patient": patient,
        "Date": date,
        "Time": time
    }

    print("Appointment booked successfully.")
    print("Appointment ID:", appointment_id)


def view_appointments():

    if len(appointments) == 0:
        print("No appointments.")
        return

    print("\n========== APPOINTMENTS ==========")

    for appointment_id, appointment in appointments.items():

        print("-----------------------------")
        print("Appointment ID:", appointment_id)
        print("Doctor:", appointment["Doctor"])
        print("Patient:", appointment["Patient"])
        print("Date:", appointment["Date"])
        print("Time:", appointment["Time"])


def cancel_appointment():

    appointment_id = input("Appointment ID: ")

    if appointment_id not in appointments:
        raise Exception("Appointment not found.")

    del appointments[appointment_id]

    print("Appointment cancelled successfully.")


while True:

    try:

        print("\n========== DOCTOR APPOINTMENT SYSTEM ==========")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Book Appointment")
        print("4. View Appointments")
        print("5. Cancel Appointment")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_doctor()

        elif choice == 2:
            view_doctors()

        elif choice == 3:
            book_appointment()

        elif choice == 4:
            view_appointments()

        elif choice == 5:
            cancel_appointment()

        elif choice == 6:
            print("Thank you.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid input.")

    except Exception as e:
        print("Error:", e)