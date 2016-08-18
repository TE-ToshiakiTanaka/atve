import sys
import traceback

from atve import STRING_SET

class AtveError(Exception):
    details = None # {<string>:<base type>, ... }

    def __init__(self, details):
        if not type(details) == dict:
            raise Exception('AtveError : details must be a dictionary')
        for key in details:
            if type(key) not in STRING_SET:
                raise Exception('AtveError : details key must be strings')
        if 'message' not in details:
            raise Exception('AtveError : details must have mesage field')
        if 'type' not in details:
            details['type'] = type(self).__name__
        self.details = details

    def __str__(self):
        message = self.message.encode('utf8')
        trace = self.format_trace()
        if trace:
            trace = trae.encode('utf8')
            return '%s\n Server side traceback:\n%s' % (message, trace)
        return str(message)

    def __getattr__(self, attribute):
        return self.details[attribute]

    @property
    def message(self):
        return self.details['message']

    def json(self):
        return self.details

    def has_trace(self):
        return 'trace' in self.details and self.trace != None

    def format_trace(self):
        if self.has_trace():
            convert = []
            for entry in self.trace:
                convert.append(tuple(entry))
            formatted = traceback.format_list(convert)
            return ''.join(formatted)
        return ''

    def print_trace(self):
        sys.stderr.write(self.format_trace())
        sys.stderr.flush()

class TimeoutError(AtveError):
    def __init__(self, details):
        if type(details) in STRING_SET:
            details = {
                'message': details
            }
        AtveError.__init__(self, details)

class RunError(AtveError):
    def __init__(self, cmd, out, message=''):
        details = {
            'cmd'       : cmd     or '',
            'ptyout'    : out     or '',
            'out'       : out     or '',
            'message'   : message or ''
        }
        AtveError.__init__(self, details)

    def __str__(self):
        return '%s:\n%s:\n%s' % (
            self.cmd, self.message, self.out
        )

class LogError(AtveError):
    def __init__(self, details):
        if type(details) in STRING_SET:
            details = {
                'message': details
            }
        AtveError.__init__(self, details)

class WorkspaceError(AtveError):
    def __init__(self, details):
        if type(details) in STRING_SET:
            details = {
                'message': details
            }
        AtveError.__init__(self, details)


class TestRunnerError(AtveError):
    def __init__(self, details):
        if type(details) in STRING_SET:
            details = {
                'message': details
            }
        AtveError.__init__(self, details)

class LibraryError(AtveError):
    def __init__(self, details):
        if type(details) in STRING_SET:
            details = {
                'message' : details
            }
        AtveError.__init__(self, details)

class SeleniumError(AtveError):
    def __init__(self, details):
        if type(details) in STRING_SET:
            details = {
                'message' : details
            }
        AtveError.__init__(self, details)

class PictureError(AtveError):
    def __init__(self, details):
        if type(details) in STRING_SET:
            details = {
                'message' : details
            }
        AtveError.__init__(self, details)

class AndroidError(AtveError):
    def __init__(self, details):
        if type(details) in STRING_SET:
            details = {
                'message' : details
            }
        AtveError.__init__(self, details)

class SlackError(AtveError):
    def __init__(self, details):
        if type(details) in STRING_SET:
            details = {
                'message' : details
            }
        AtveError.__init__(self, details)
