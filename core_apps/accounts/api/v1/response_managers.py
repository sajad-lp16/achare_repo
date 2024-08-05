from rest_framework import status
from rest_framework.response import Response


class LoginRequestResponseManager:
    '''Respects the response interface no matter what!'''
    RESPONSE_INTERFACE = {
        'status': None,
        'message': None,
        'next_step': None
    }

    REGISTER_STEP = 1
    LOGIN_STEP = 2

    STEP_2_MESSAGE = {
        REGISTER_STEP: 'welcome to the app, please enter verification code',
        LOGIN_STEP: 'welcome to the app, please enter your password',
    }

    def get_login_step_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'success'
        response['message'] = self.STEP_2_MESSAGE[self.LOGIN_STEP]
        response['next_step'] = self.LOGIN_STEP

        response.update(data)

        return Response(response, status=status.HTTP_200_OK)

    def get_register_step_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'success'
        response['message'] = self.STEP_2_MESSAGE[self.REGISTER_STEP]
        response['next_step'] = self.REGISTER_STEP

        response.update(data)

        return Response(response, status=status.HTTP_201_CREATED)

    def get_invalid_phone_number_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'error'
        response['message'] = 'invalid phone number'

        response.update(data)

        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def get_throttle_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'error'
        response['message'] = 'request limit exceeded'

        response.update(data)

        return Response(response, status=status.HTTP_429_TOO_MANY_REQUESTS)


class RegisterResponseManager:
    RESPONSE_INTERFACE = {
        'status': None,
        'message': None,
    }

    def get_register_ok_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'success'
        response['message'] = 'successful registration, profile info is now updated'

        response.update(data)

        return Response(response, status=status.HTTP_200_OK)

    def get_not_found_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'error'
        response['message'] = 'not registered yet'

        response.update(data)

        return Response(response, status=status.HTTP_404_NOT_FOUND)

    def get_invalid_phone_number_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'error'
        response['message'] = 'invalid phone number'

        response.update(data)

        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def get_already_registered_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'error'
        response['message'] = 'already registered, you should login instead'

        response.update(data)

        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def get_throttle_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'error'
        response['message'] = 'request limit exceeded'

        response.update(data)

        return Response(response, status=status.HTTP_429_TOO_MANY_REQUESTS)


class LoginResponseManager:
    RESPONSE_INTERFACE = {
        'status': None,
        'message': None,
        'access': None,
        'refresh': None,
    }

    def get_login_ok_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'success'
        response['message'] = 'logged in successfully'

        response.update(data)

        return Response(response, status=status.HTTP_200_OK)

    def get_invalid_phone_number_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'error'
        response['message'] = 'invalid phone number'

        response.update(data)

        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def get_throttle_response(self, data: dict={}):
        response = self.RESPONSE_INTERFACE.copy()
        response['status'] = 'error'
        response['message'] = 'request limit exceeded'

        response.update(data)

        return Response(response, status=status.HTTP_429_TOO_MANY_REQUESTS)
