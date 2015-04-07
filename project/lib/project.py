from process import Process

class Project:

    def __init__(self, options):
        self.options = options
        self.process = Process()

    def date(self):
        self._get_date()

    def _get_date(self):
        # prints stdout of subprocess with command "date"
        # strips tailing endoflines because print adds one
        print self.process.execute("date").rstrip('\n')

    def print_example_arg(self):
        print self.options.example
