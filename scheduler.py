SLOT_1 = '8:00AM'
SLOT_2 = '9:00AM'
SLOT_3 = '10:00AM'
SLOT_4 = '11:00AM'
SLOT_5 = '1:00PM'
SLOT_6 = '2:00PM'
SLOT_7 = '3:00PM'
SLOT_8 = '4:00PM'
SLOT_9 = '5:00PM'
SLOT_10 = '6:00PM'

CLASS_NAME = 'NAME'
CLASS_APPOINTMENT_INFO = 'APPOINTMENT_INFO'


class Patient(object):
    CLASS_ID = 'ID'
    CLASS_PREV_APPOINTMENTS = 'PREVIOUS_APPOINTMENTS'

    def __init__(self, name, ssn):
        self.ssn = ssn
        self.patient_name = name
        self.patient_id = self.patient_name[:1] + ssn
        self.patient_calendar = {
            CLASS_NAME: self.patient_name,
            self.CLASS_ID: self.patient_id,
            CLASS_APPOINTMENT_INFO: {}
        }
    def get_patient_record(self):
        patient_record =  {
            CLASS_NAME : self.patient_name,
            self.CLASS_ID : self.patient_id,
        }
        return patient_record

    def print_patient_calendar(self):
         print(self.patient_calendar)


class Doctor(object):
    CLASS_DEPARTMENT = 'DEPARTMENT'

    def __init__(self, name, department):
        self.doctor_name = name
        self.department = department
        self.doctor_calendar = {
            CLASS_NAME: self.doctor_name,
            self.CLASS_DEPARTMENT: self.department,
            CLASS_APPOINTMENT_INFO: {},
        }

    def get_doctor_record(self):
        doctor_record =  {
            CLASS_NAME : self.doctor_name,
            self.CLASS_DEPARTMENT: self.department
        }
        return doctor_record

    def print_doctor_calendar(self):
        print(self.doctor_calendar)



class Scheduler(object):

    def schedule(self,doctor,patient,time):
        self.time = time
        self.doctor = doctor
        self.patient = patient
        if (self.docavailable(doctor,time) and self.patavailable(patient,time)):
            self.update_patient_calendar(patient,doctor,time)
            self.update_doctor_calendar(patient,doctor,time)
            print("Appointment Successfully scheduled with Dr. " + doctor.doctor_name +  " for patient " + patient.patient_calendar[CLASS_NAME] + "\n")
            return True

    def docavailable(self,doctor,time):
        if time in doctor.doctor_calendar[CLASS_APPOINTMENT_INFO]:
            print("Sorry, No Appointment Available with Dr. " + doctor.doctor_name + "\n")
            return False
        else:
            return True

    def patavailable(self,patient,time):
        if time in patient.patient_calendar[CLASS_APPOINTMENT_INFO]:
            print("Sorry, The patient " + patient.patient_name +  " already has an appointment with Dr. " + patient.patient_calendar[CLASS_APPOINTMENT_INFO][time][CLASS_NAME] + "\n")
            return False
        else:
            return True

    def update_patient_calendar(self,patient,doctor,time):
        patient.patient_calendar[CLASS_APPOINTMENT_INFO][time] = doctor.get_doctor_record()

    def update_doctor_calendar(self,patient,doctor,time):
        doctor.doctor_calendar[CLASS_APPOINTMENT_INFO][time] = patient.get_patient_record()



D1 = Doctor("R", "Dental")
D2 = Doctor("A","General")
P1 = Patient("W", "1234")
P2 = Patient("W", "1214")

S1 = Scheduler()
S1.schedule(D1,P1,SLOT_10)
S1.schedule(D1,P2,SLOT_1)

P1.print_patient_calendar()
P2.print_patient_calendar()

D1.print_doctor_calendar()
D2.print_doctor_calendar()
