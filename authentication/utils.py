from profiles.serializers import UserSerializerWithProfileFormat
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'payload': UserSerializerWithProfileFormat(user, context={'request': request}).data
    }