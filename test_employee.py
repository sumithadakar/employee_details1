from employee import emp_details

def test_emp():
    expected_op = (
        "Employee name: Sumit\n"
        "Employee id: 273\n"
        "Department: MCA\n"
        "Salary: 200000"
    )

    assert emp_details("Sumit", 273, "MCA", 200000) == expected_op
