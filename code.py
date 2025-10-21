class Hospital:
    def __init__(self, name, total_beds):
        self.name = name
        self.total_beds = total_beds
        self.available_beds = total_beds
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient_id, name, age, diagnosis):
        patient = self.Patient(patient_id, name, age, diagnosis)
        if self.available_beds > 0:
            self.patients.append(patient)
            self.available_beds -= 1
            print(f"\033[92mPatient {patient.name} admitted to hospital.\033[0m")
        else:
            print("\033[91mNo beds available. Patient cannot be admitted.\033[0m")

    def discharge_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            self.available_beds += 1
            print(f"\033[92mPatient {patient.name} discharged from hospital.\033[0m")
        else:
            print("\033[91mPatient not found in hospital.\033[0m")

    def add_doctor(self, doctor_id, name, specialty):
        doctor = self.Doctor(doctor_id, name, specialty)
        self.doctors.append(doctor)
        print(f"\033[92mDr. {doctor.name} added to hospital staff.\033[0m")

    def schedule_appointment(self, patient, doctor, date, time):
        appointment = self.Appointment(patient, doctor, date, time)
        self.appointments.append(appointment)
        print(f"\033[92mAppointment scheduled for {patient.name} with Dr. {doctor.name} on {date} at {time}.\033[0m")

    def view_appointments(self):
        for appointment in self.appointments:
            print(appointment)

    def view_patients(self):
        for patient in self.patients:
            print(patient.name)

    def view_doctors(self):
        for doctor in self.doctors:
            print(doctor.name)

    class Patient:
        def __init__(self, patient_id, name, age, diagnosis):
            self.patient_id = patient_id
            self.name = name
            self.age = age
            self.diagnosis = diagnosis

    class Doctor:
        def __init__(self, doctor_id, name, specialty):
            self.doctor_id = doctor_id
            self.name = name
            self.specialty = specialty
            self.appointments = []

        def view_appointments(self):
            for appointment in self.appointments:
                print(appointment)

    class Appointment:
        def __init__(self, patient, doctor, date, time):
            self.patient = patient
            self.doctor = doctor
            self.date = date
            self.time = time

        def __str__(self):
            return f"Appointment for {self.patient.name} with Dr. {self.doctor.name} on {self.date} at {self.time}"

def main():
    hospital = Hospital("SJM Wellness Crew", 100)

    while True:
        print("\n\033[1m  ██╗   ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗     ██████╗ ███████╗███████╗███████╗███████╗\033[0m")
        print("\033[1m  ██║   ██║██╔════╝██║     ██╔═══██╗██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝\033[0m")
        print("\033[1m  ██║   ██║█████╗  ██║     ██║   ██║██████╔╝██╔████╔██║███████╗    ██║   ██║███████╗███████╗███████╗█████╗  \033[0m")
        print("\033[1m  ╚██╗ ██╔╝██╔══╝  ██║     ██║   ██║██╔══██╗██║╚██╔╝██║╚════██║    ██║   ██║╚════██║╚════██║╚════██║██╔══╝  \033[0m")
        print("\033[1m   ╚████╔╝ ███████╗███████╗╚██████╔╝██║  ██║██║ ╚═╝ ██║███████║    ╚██████╔╝███████║███████║███████║███████╗\033[0m")
        print("\033[1m    ╚═══╝  ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝\033[0m")

        print("\033[91mMenu Options\033[0m")
        print("\033[94m1. Add Patient\033[0m")
        print("\033[94m2. Discharge Patient\033[0m")
        print("\033[94m3. Add Doctor\033[0m")
        print("\033[94m4. Schedule Appointment\033[0m")
        print("\033[94m5. View Appointments\033[0m")
        print("\033[94m6. View Patients\033[0m")
        print("\033[94m7. View Doctors\033[0m")
        print("\033[94m8. View Bed Availability\033[0m")
        print("\033[94m9. Exit\033[0m")

        choice = input("\033[92mEnter your choice: \033[0m")

        if choice == "1":
            patient_id = int(input("\033[96mEnter patient ID: \033[0m"))
            name = input("\033[96mEnter patient name: \033[0m")
            age = int(input("\033[96mEnter patient age: \033[0m"))
            diagnosis = input("\033[96mEnter patient diagnosis: \033[0m")
            hospital.add_patient(patient_id, name, age, diagnosis)

        elif choice == "2":
            name = input("\033[96mEnter patient name: \033[0m")
            for patient in hospital.patients:
                if patient.name == name:
                    hospital.discharge_patient(patient)
                    break
            else:
                print("\033[91mPatient not found in hospital.\033[0m")

        elif choice == "3":
            doctor_id = int(input("\033[96mEnter doctor ID: \033[0m"))
            name = input("\033[96mEnter doctor name: \033[0m")
            specialty = input("\033[96mEnter doctor specialty: \033[0m")
            hospital.add_doctor(doctor_id, name, specialty)

        elif choice == "4":
            patient_name = input("\033[96mEnter patient name: \033[0m")
            doctor_name = input("\033[96mEnter doctor name: \033[0m")
            date = input("\033[96mEnter appointment date: \033[0m")
            time = input("\033[96mEnter appointment time: \033[0m")
            for patient in hospital.patients:
                if patient.name == patient_name:
                    for doctor in hospital.doctors:
                        if doctor.name == doctor_name:
                            hospital.schedule_appointment(patient, doctor, date, time)
                            break
                    else:
                        print("\033[91mDoctor not found in hospital.\033[0m")
                    break
            else:
                print("\033[91mPatient not found in hospital.\033[0m")

        elif choice == "5":
            hospital.view_appointments()
            while True:
                print("\033[95mDoctor Availability\033[0m")
                print("1. Dr. Vikram Singh (Ortho)")
                print("2. Dr. Ananya Sharma - Cardiology")
                print("3. Dr. Priya Patel - Pediatrics")
                print("4. Dr. Rajesh Kumar - Neurology")
                print("5. Dr. Meera Desai - Dermatology")
                print("6. Dr. Sanjay Gupta - Oncology")
                print("7. Dr. Niharika Rao - Gynecology")
                print("8. Dr. Arjun Reddy - Psychiatry")
                print("9. Dr. Sneha Joshi - Ophthalmology")
                print("10. Dr. Rahul Mehta - Internal Medicine")
                choice = input("\033[92mEnter your choice: \033[0m")

                if choice == "1":
                    print("\033[92mDr. Vikram Singh (Ortho):\nAvailable: Tuesday, Thursday, Saturday\nTimings: 10:00 AM - 2:00 PM IST\033[0m")

                elif choice == "2":
                    print("\033[92mDr. Ananya Sharma (Cardiology):\nAvailable: Monday, Wednesday, Friday\nTimings: 9:00 AM - 1:00 PM IST\033[0m")

                elif choice == "3":
                    print("\033[92mDr. Priya Patel (Pediatrics):\nAvailable: Monday to Friday\nTimings: 10:30 AM - 4:30 PM IST\033[0m")

                elif choice == "4":
                    print("\033[92mDr. Rajesh Kumar (Neurology):\nAvailable: Monday, Wednesday, Friday\nTimings: 11:00 AM - 3:00 PM IST\033[0m")

                elif choice == "5":
                    print("\033[92mDr. Meera Desai (Dermatology):\nAvailable: Tuesday, Thursday, Saturday\nTimings: 9:30 AM - 1:30 PM IST\033[0m")

                elif choice == "6":
                    print("\033[92mDr. Sanjay Gupta (Oncology):\nAvailable: Monday to Friday\nTimings: 12:00 PM - 6:00 PM IST\033[0m")

                break

        elif choice == "6":
            hospital.view_patients()

        elif choice == "7":
            print("\033[95mAvailable Doctors\033[0m")
            print("1. Dr. Sridhar (Neuro)")
            print("2. Dr. Ananya Sharma - Cardiology")
            print("3. Dr. Priya Patel - Pediatrics")
            print("4. Dr. Rajesh Kumar - Neurology")
            print("5. Dr. Meera Desai - Dermatology")
            print("6. Dr. Sanjay Gupta - Oncology")
            print("7. Dr. Niharika Rao - Gynecology")
            print("8. Dr. Arjun Reddy - Psychiatry")
            print("9. Dr. Sneha Joshi - Ophthalmology")
            print("10. Dr. Rahul Mehta - Internal Medicine")
            hospital.view_doctors()

        elif choice == "8":
            print(f"\033[96mAvailable beds: {hospital.available_beds}/{hospital.total_beds}\033[0m")

        elif choice == "9":
            break

        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")


if __name__ == "__main__":
    main()
