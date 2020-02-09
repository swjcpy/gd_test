from datetime import datetime, date

class policyholder:
    policyholders = []

    def __init__(self, gender, DOB, ssn, smoking, allergies, med_history):
        self.policyholder_id = id(self)
        self.gender = gender
        self.DOB = datetime.strptime(DOB, '%m/%d/%Y')
        self.ssn = ssn
        self.smoking = smoking
        self.allergies = allergies
        self.med_history = med_history
        policyholder.policyholders.append(self)


    # Method that adds an insured individual and returns the unique identifier of that insured individual
    @classmethod
    def createHolder_id(cls, gender, DOB, ssn, smoking, allergies, med_history):
        ph = cls(gender, DOB, ssn, smoking, allergies, med_history)
        return (ph, ph.policyholder_id)

    def display_policyholders():
        return policyholder.policyholders
