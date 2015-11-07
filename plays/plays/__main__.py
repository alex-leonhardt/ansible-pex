#!/usr/bin/env python


import argparse
import sys
import run

parser = argparse.ArgumentParser(
    description='Pexsible - Run Ansible w/o installing it or required playbooks, all from within pex'
)

parser.add_argument('--diff', required=False, action='store_true', default=False,
                  help='Show diff when files based on templates are being changed (default: False)')

parser.add_argument('--noop', required=False, action='store_true', default=False,
                    help='Dry-run (no op) only, do not change anything (default: False)')

parser.add_argument('--debug', required=False, action='store_true', default=False,
                    help='Run ansible with -vvv (default: False)')

parser.add_argument('--playbook', '-p', required=True,
                  help='The playbook to run (default: None, required: True)')

argv = parser.parse_args()

sys.exit(run.main(argv))
