from policyholders import policyholder

class event:
    events = []

    def __init__(self, date_of_incidence, issue_type, billed_amount, covered_amount, policyholder_id):
        self.event_id = id(self)
        self.policyholder_id = policyholder_id
        self.date_of_incidence = date_of_incidence
        self.issue_type = issue_type
        self.billed_amount = billed_amount
        self.covered_amount = covered_amount

        event.events.append(self)

    @classmethod
    # This method adds an insurance event for a specific user identified by unique identifier
    def from_parent(cls, id, date_of_incidence, issue_type, billed_amount, covered_amount):
        for ph in policyholder.policyholders:
            if id == ph.policyholder_id:
                print("Ready to insert event")
                return cls(date_of_incidence, issue_type, billed_amount, covered_amount, ph.policyholder_id)
        print("Error: no information for this policy holder ID")

    def display_event_by_id(id):
        return [x for x in event.events if x.policyholder_id == id]
