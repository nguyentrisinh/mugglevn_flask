from sqlalchemy import exc

class ApiBase:
    def __init__(self):
        pass

    @staticmethod
    def as_success(data):
        return ApiBase.build_response(data, None)

    @staticmethod
    def as_error(errors):
        return ApiBase.build_response(None, errors)

    @staticmethod
    def build_response(data, errors):
        if errors is None:
            return {
                "data": data,
                "errors": None
            }

        if errors is list:
            return {
                "data": data,
                "errors": errors
            }

        if type(errors) is Exception:
            return ApiBase.return_message(data, errors, 9999)

        if type(errors) is exc.SQLAlchemyError:
            return ApiBase.return_message(data, errors, 1101)

        return {
            "data": data,
            "errors": [errors]
        }

    @staticmethod
    def return_message(data, errors, error_code):
        if type(errors.message) is str:
            return {
                "data": data,
                "errors": [
                    {"errorMessage": errors.message, "errorCode": error_code}
                ]
            }

        return {
            "data": data,
            "errors": [
                errors.message
            ]
        }
