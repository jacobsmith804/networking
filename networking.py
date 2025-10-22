#!/usr/bin/env python3
from extras.scripts import Script

name = "Networking"

class Networking(Script):

    class Meta:
        name = "Networking Script"
        commit_default = False

    def run(self, data, commit):
        import subprocess
        self.log_info(f"Successful")
        result = subprocess.run(['whoami'], capture_output=True, text=True)
        self.log_info(f"Current user: {result.stdout.strip()}")
