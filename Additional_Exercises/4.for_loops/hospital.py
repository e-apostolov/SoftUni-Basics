period = int(input())

treated_patients = 0
untreated_patients = 0
doctors = 7

for i in range(1, period + 1):
    if i % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    patient_count = int(input())
    if patient_count <= doctors:
        treated_patients += patient_count
        untreated_patient = 0
    else:
        treated_patients += doctors
        untreated_patients += abs(doctors - patient_count)

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
