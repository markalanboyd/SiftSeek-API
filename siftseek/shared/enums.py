import enum


class ApplicationStatus(enum.Enum):
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"
    CLOSED = "closed"


class EducationLevel(enum.Enum):
    NO_FORMAL = "No formal education"
    PRIMARY_EDUCATION = "Primary education"
    LOWER_SECONDARY = "Lower secondary education / Junior high school"
    UPPER_SECONDARY = "Upper secondary education / Senior high school"
    VOCATIONAL = "Vocational training / Trade school"
    ASSOCIATES = "Associate's degree / Foundation degree"
    BACHELORS = "Bachelor's degree"
    POSTGRADUATE_DIPLOMA = "Postgraduate diploma / Professional certification"
    MASTERS = "Master's degree"
    PROFESSIONAL = "Professional degree (e.g., JD, MD)"
    DOCTORATE = "Doctorate (Ph.D.)"
    POSTDOCTORAL = "Post-doctoral training"
