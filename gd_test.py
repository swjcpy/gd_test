from policyholders import policyholder
from events import event
from datetime import date, datetime

#Since I don't have access to database,
# here I assume policyholders are stored in a list called policyholders
# events are stored in a list called events
# each element of these two lists is a class object
# event is a child of policyholder
print("policyholders: {}".format(policyholder.policyholders))

ph1 = policyholder("Male", "1/1/1990", "***-**-1234", "yes", 'N/A', 'N/A')
ph2 = policyholder("Female", "2/2/1990", "***-**-2345", "no", 'peanut', 'N/A')
ph3 = policyholder("Male", "3/3/1990", "***-**-3456", "no", 'N/A', 'diabetes')

print("policyholders: {}".format(policyholder.policyholders))

print("events: {}".format(event.events))

event1 = event.from_parent(ph1.policyholder_id, '5/5/2009', 'WC', 1000, 500)
event2 = event.from_parent(ph1.policyholder_id, '4/5/2010', 'Crime', 2000, 500)
event3 = event.from_parent(ph2.policyholder_id, '1/5/2010', 'GL', 1000, 500)

print("events: {}".format(event.events))

# 1. Example of "Adds an insured individual and returns the unique identifier of that individual"

ph4, ph4_id = policyholder.createHolder_id("Male", "4/4/1990", "***-**-5432", "no", 'N/A', 'N/A')
print("ph4 policy holder ID: {}".format(ph4.policyholder_id))
print("ph4 policy holder ID: {}".format(ph4_id))

# 2. Example of "adds an insurance event for a specific user identified by unique identifier"
# a. if the unique identifier matches the policyholder in policyholders list, then it will be added to events list
event4 = event.from_parent(ph4_id, '1/5/2010', 'WC', 1000, 500)
print("events: {}".format(event.events))

# b. if the unique identifier doesn't match to elements in policyholders list, then it will not be added to events list
event5 = event.from_parent(1, '1/5/2010', 'WC', 1000, 500)

# 3. List all insured individuals
print("policyholders: {}".format(policyholder.display_policyholders()))

# 4. List all events associated with a specific user by unique identifier
# display events associated with ph1
print("events for ph1: {}".format(event.display_event_by_id(ph1.policyholder_id)))

# Data structure that contains aggregated metrics for all insured people
ds = {'Total Covered Amount':0, 'Avg age':0}
for x in event.events:
    ds['Total Covered Amount'] += x.covered_amount
    year = x.date_of_incidence.split('/')[-1]
    if year in ds.keys():
        ds[year] += 1
    else:
        ds[year] = 1

def calculate_age(DOB):
    today = date.today()
    return today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))

for x in policyholder.policyholders:
    ds['Avg age'] += calculate_age(x.DOB) / len(policyholder.policyholders)

print(ds)