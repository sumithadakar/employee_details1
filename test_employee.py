from employee import employee_details

def test_employee():
    expected_op = (
        "Employee Name: Sumit\n"
        "Employee ID: 273\n"
        "Department: MCA\n"
        "Salary: 200000"
    )

    assert employee("Sumit", 273, "MCA", 200000) == expected_op
