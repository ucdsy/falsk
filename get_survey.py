

from limesurveyrc2api.limesurveyrc2api import LimeSurveyRemoteControl2API as LimeSurvey

from pathlib import Path
from limepy import download


def python_get_response(url, username, password):
    # point to the limeserver server
    url = 'http://132.249.238.41/limesurvey/index.php/admin/remotecontrol'
    username = "admin"
    password = "ecrr"

    # open a session
    api = LimeSurvey(url=url)

    # get the session key
    key=api.sessions.get_session_key(username=username,password=password)['result']

    result = api.surveys.list_surveys(session_key=key,username=username)['result']

    # list surveys. The 499414 is the survey we are playing with for survey in result:
    for survey in result:
        print(survey.get("sid"))

    # close the session
    api.sessions.release_session_key(key)


    # get responses for the survey we need
    csv = download.get_responses(url, username, password, 1, 499414)

    path = Path('data.csv')

    # write out the responses
    path.write_text(csv)

