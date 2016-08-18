import os
import sys

from atve.log import Log
from atve.exception import *

try :
    from slacker import Slacker
except Exception as e:
    print(str(e))

L = Log("Slack.Library.ATVE")

class Slack(object):

    def __init__(self, token):
        try:
            self.slack = Slacker(token)
        except Exception as e:
            L.warning(str(e))
            raise SlackError("%s is not exists." % token)

    def message(self, message, channels):
        return self.slack.chat.post_message(
            channels,
            message,
            as_user=True)

    def upload(self, filepath, channels):
        return self.slack.files.upload(
            filepath,
            channels=channels)



if __name__ == "__main__":
    slack = Slack("xoxb-70511776391-crpyo9EROmAk1OuEAVTUoWZM")
    print(slack.message('てすと', 'kancolle'))
    """
    slack = Slacker("xoxb-70511776391-crpyo9EROmAk1OuEAVTUoWZM")
    #slack.chat.post_message(
    #    'kancolle',
    #    'こんにちわー',
    #    as_user=True)
    slack.files.upload(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "test.png"),
            channels="kancolle",
            title="drop.png",
            initial_comment='これは私の肖像画です'
    )
    """
