import time

from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, DEFAULT_PORT, PORT, ERROR

INSUFFICIENT_DATA = {
    TIME: time.time(),
    PORT: DEFAULT_PORT,
    USER: {
      ACCOUNT_NAME: "test_user"
    }
  }

BAD_USER = {
    ACTION: PRESENCE,
    TIME: time.time(),
    PORT: DEFAULT_PORT,
    USER: {
      ACCOUNT_NAME: "Guest"
    }
}

CORRECT_MESSAGE = {
    ACTION: PRESENCE,
    TIME: time.time(),
    PORT: DEFAULT_PORT,
    USER: {
        ACCOUNT_NAME: 'test_user'
    }
}

TRUE_REQUEST = {
    ACTION: PRESENCE,
    TIME: 1,
    PORT: DEFAULT_PORT,
    USER: {
        ACCOUNT_NAME: 'test_user'
    }
}

CORRECT_200 = '200 : OK'
CORRECT_400 = '400 : Bad Request'

NOT_CORRECT_ANS = {ERROR: 'Bad Request'}
