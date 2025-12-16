from employee import employee_details

def test_employee_details():
    expected_op = (
        "Employee Name: Sumit\n"
        "Employee ID: 273\n"
        "Department: MCA\n"
        "Salary: 200000"
    )

    assert employee_details("Sumit", 273, "MCA", 200000) == expected_op
