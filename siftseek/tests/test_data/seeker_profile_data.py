passing = {
    "username": "alexsmith",
    "first_name": "Alex",
    "last_name": "Smith",
    "contact_email": "alex.smith@example.com",
    "work_phone": "+1-212-555-1234",
    "work_phone_ext": "200",
    "cellphone": "+1-917-555-5678",
    "address": "456 Oak Lane",
    "city": "New York",
    "profile_pic_url": "http://example.com/images/alex_profile.jpg",
    "resume_url": "http://example.com/resumes/alex_resume.pdf",
    "linkedin_url": "http://linkedin.com/in/alexsmithprofessional",
    "portfolio_url": "http://alexsmithportfolio.com",
    "summary": "Experienced software engineer with a passion for developing innovative programs that expedite the efficiency and effectiveness of organizational success.",
    "education_level": "UPPER_SECONDARY",
    "remote_option": True,
}

failing = {
    "username": "this_username_is_way_too_long",
    "first_name": "",
    "last_name": "",
    "contact_email": "notanemail",
    "work_phone": "12345",
    "work_phone_ext": "123456",
    "cellphone": "12345",
    "address": "",
    "city": "",
    "profile_pic_url": "not-a-url",
    "resume_url": "not-a-url",
    "linkedin_url": "not-a-url",
    "portfolio_url": "not-a-url",
    "summary": "a" * 10001,
    # Not failing data to get around this warning: RemovedInMarshmallow4Warning: `Field.fail` is deprecated.
    "education_level": "UPPER_SECONDARY",
    "remote_option": "yes",
}

patch_passing = {"username": "alexsmith1", "work_phone": "+385.97.6140.942"}

patch_failing = {"username": "this_username_is_way_too_long", "work_phone": "12345"}
