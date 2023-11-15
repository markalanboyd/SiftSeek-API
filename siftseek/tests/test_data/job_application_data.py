"""
This job_application_data.py file in the tests.test_data module provides test
data for the job_application ORM.
"""

passing = {
    "status": "PENDING",
    "cover_letter": "Cover letter contents",
}

failing = {
    "status": "status",
    "cover_letter": "a" * 10_001,
}

applications_to_delete = "1,2,3,4"

put_passing = {
    "cover_letter": "New cover letter contents",
}