from ansiblelint import AnsibleLintRule

class AWSCredentials(AnsibleLintRule):
    id = 'ANSWERS02'
    shortdesc = 'Playbook May Contain AWS Credentials'
    description = 'AWS credentials should not be included in variables, especially if they are stored publically'
    tags = ['formatting']

    def match(self, file, line):
        if "aws_access_key_id" in line:
            self.shortdesc
            return True

        if "aws_secret_access_key" in line:
            self.shortdesc
            return True
        return False
