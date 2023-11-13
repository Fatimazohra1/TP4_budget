import os
import subprocess

badhash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
goodhash="e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c "
os.system(f'git bisect start {badhash} {goodhash}')
os.system('git bisect run python manage.py test')
os.system('git bisect reset')
