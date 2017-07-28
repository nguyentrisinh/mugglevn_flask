class ErrorDefine:
    def __init__(self):
        pass

    # 9999: Error server
    # 9998: Error Database

    # 10xx: Error user
    USER_NOT_FOUND = {"errorMessage": "User not found", "errorCode": 1000}

    # 11xx: Error company
    COMPANY_NOT_FOUND = {"errorMessage": "Company not found", "errorCode": 1100}

    # 11xx: Error School
