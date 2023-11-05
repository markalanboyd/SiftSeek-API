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
    "education_level_id": 4,
    "remote_option": True,
}

failing = {
    "username": "",  # Fails min length of 1
    "first_name": "A" * 256,  # Fails max length of 255
    "last_name": "Smith" * 51,  # Fails max length of 255
    "contact_email": "not-an-email",  # Fails email format
    "work_phone": "12345",  # Fails phone number format
    "work_phone_ext": "123456",  # Fails max length of 5
    "cellphone": "12345",  # Fails phone number format
    "address": "A" * 256,  # Fails max length of 255
    "city": "A" * 256,  # Fails max length of 255
    "profile_pic_url": "htt:/malformed.url",  # Fails URL format
    "resume_url": "ftp://wrong-protocol.com/resume",  # Fails URL format
    "linkedin_url": "linkedin.com/in/noscheme",  # Fails URL format
    "portfolio_url": "http://thisisaveryverylongurlthatexceedsthemaximumallowedlengthforaurl.com/alongpath?with=verylongqueryparametersandstuffthatmakesittoolong",  # Fails URL format
    "summary": "A" * 10001,  # Fails max length of 10,000
    "education_level_id": 0,  # Fails min value of 1
    "remote_option": "not-a-boolean",  # Fails boolean field check
}

patch_passing = {"username": "alexsmith2", "work_phone_ext": "100"}
