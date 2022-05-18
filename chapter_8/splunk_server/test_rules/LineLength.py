from ansiblelint import AnsibleLintRule

class LineLength(AnsibleLintRule):
    id = 'ANSWERS01'
    shortdesc = 'Line too long'
    description = 'Python Code Style Guidelines Recommend Line Length Under 80 Characters'
    tags = ['formatting']

    def match(self, file, line):
        if len(line) > 80:
            self.shortdesc += " ({} characters)".format(len(line))
            return True
        return False
