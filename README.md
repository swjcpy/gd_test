# gd_test

Since I don't have access to database,
here I assume policyholders are stored in a list called policyholders
events are stored in a list called events
each element of these two lists is a class object
event is a child of policyholder

[policyholders.py](https://github.com/swjcpy/gd_test/blob/master/policyholders.py) defines each policyholder,
everytime a new policy holder is created, it will be stored into policyholders list

same as [events.py](https://github.com/swjcpy/gd_test/blob/master/events.py)

 ## Design a schema for policyholders

 The answer can be found at [Schema.png](https://github.com/swjcpy/gd_test/blob/master/Schema.png)

 ## Design a data structure

 The answer can be found at [gd_test](https://github.com/swjcpy/gd_test/blob/master/gd_test.py)

 ```python
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
```

## Methods
### Adds an insured individual and returns the unique identifier of that individual
```python
# Method that adds an insured individual and returns the unique identifier of that insured individual
    @classmethod
    def createHolder_id(cls, gender, DOB, ssn, smoking, allergies, med_history):
        ph = cls(gender, DOB, ssn, smoking, allergies, med_history)
        return (ph, ph.policyholder_id)
```

### Adds an insurance event for a specific user identified by unique identifier
```python
@classmethod
    # This method adds an insurance event for a specific user identified by unique identifier
    def from_parent(cls, id, date_of_incidence, issue_type, billed_amount, covered_amount):
        for ph in policyholder.policyholders:
            if id == ph.policyholder_id:
                print("Ready to insert event")
                return cls(date_of_incidence, issue_type, billed_amount, covered_amount, ph.policyholder_id)
        print("Error: no information for this policy holder ID")
```

### List all insured individuals
```python
    def display_policyholders():
        return policyholder.policyholders
```

### List all events associated with a specific user by unique identifier
```python
    def display_event_by_id(id):
        return [x for x in event.events if x.policyholder_id == id]
```

## What considerations should take into account when storing confidential information

Of course the best way is don't. However if have to, storing just last 4 digits.

Also no hashing is good enough to keep the number secure if a hacker gets the hashed version.

Symmetric key encryption is a bit better, unless the hacker also steals the key used to decrypt numbers.

