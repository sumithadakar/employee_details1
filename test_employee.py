from emp import emp_details

def test_emp():
    expected_op = (
        "Employee name: Queen\n"
        "Employee id: 900\n"
        "Department: MCA\n"
        "Salary: 200000"
    )

    assert emp_details("Queen", 900, "MCA", 200000) == expected_op
