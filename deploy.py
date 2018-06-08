import os
import subprocess
import urllib.request

if not os.path.isfile("helper.py"):
	urllib.request.urlretrieve("https://raw.githubusercontent.com/VladasZ/shell/master/helper.py", "helper.py")
	subprocess.call("deploy.py", shell=True)
	exit()
else:
	import helper

run=helper.run

run('pip install cmake')

