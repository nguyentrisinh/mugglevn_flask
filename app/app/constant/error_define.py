class ErrorDefine:
    def __init__(self):
        pass

    # 9999: Error server
    # 9998: Error Database

    # 10xx: Error user
    USER_NOT_FOUND = {"errorMessage": "User not found", "errorCode": 1000}

    # 11xx: Error company
    COMPANY_NOT_FOUND = {"errorMessage": "Company not found", "errorCode": 1100}

    # 12xx: Error CompanyType
    COMPANY_TYPE_NOT_FOUND = {"errorMessage": "CompanyType not found", "errorCode": 1200}

    # 13xx: Error Skill
    SKILL_NOT_FOUND = {"errorMessage": "Skill not found", "errorCode": 1300}

    # 14xx: Error Benefit
    BENEFIT_NOT_FOUND = {"errorMessage": "Benefit not found", "errorCode": 1400}

    # 15xx: Error Review
    REVIEW_NOT_FOUND = {"errorMessage": "Review not found", "errorCode": 1500}

    # 16xx: Error JobSkill
    JOB_SKILL_NOT_FOUND = {"errorMessage": "JobSkill not found", "errorCode": 1600}

    # 17xx: Error Job
    JOB_NOT_FOUND = {"errorMessage": "Job not found", "errorCode": 1700}

    # 18xx: Error JobBenefit
    JOB_BENEFIT_NOT_FOUND = {"errorMessage": "JobBenefit not found", "errorCode": 1800}

