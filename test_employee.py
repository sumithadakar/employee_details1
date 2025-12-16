from employee import employee

def test_employee():
    expected_op = (
        "Employee name: Sumit\n"
        "Employee id: 273\n"
        "Department: MCA\n"
        "Salary: 200000"
    )

    assert employee("Sumit", 273, "MCA", 200000) == expected_op
