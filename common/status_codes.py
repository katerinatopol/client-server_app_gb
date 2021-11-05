from common.variables import RESPONSE, ERROR, BAD_RESPONSE


class StatusCodes:

    ok = {RESPONSE: 200}
    bad_request_srv = {
        BAD_RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    bad_request_cl = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    # not_found = 404
    # created = 201
