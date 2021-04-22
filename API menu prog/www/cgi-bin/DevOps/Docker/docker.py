#!/usr/bin/python3

import cgi
import subprocess
print("content-type: text/html")
print()

form = cgi.FieldStorage()
operation = form.getvalue("id")
image = form.getvalue("image")
container = form.getvalue("container")
options = form.getvalue("options")

print('<pre>')

if operation == 'run_a_container_with_options':
    image = form.getvalue()
    print(subprocess.getoutput('sudo docker run {} {} {}'.format(options,container,image)))
elif operation == 'create_start_run_a_command':
    image = form.getvalue()
    print(subprocess.getoutput('sudo docker run -it {}'.format(image)))
elif operation == 'start_a_container_and_keep_it_running':
    image = form.getvalue()
    print(subprocess.getoutput('sudo docker run -td {}'.format(image)))
elif operation == 'list_running_containers':
    print(subprocess.getoutput('sudo docker ps'))
elif operation == 'list_of_all_containers':
    print(subprocess.getoutput('sudo docker ps -a'))
elif operation == 'list_the_log_of_running_container':
    container = form.getvalue()
    print(subprocess.getoutput('sudo docker logs {}'.format(container)))
elif operation == 'list_low_level_information_of_docker_containers':
    container = form.getvalue()
    print(subprocess.getoutput('sudo docker inspect {} {}'.format(options,container)))
elif operation == 'history_of_an_image':
    image = form.getvalue()
    print(subprocess.getoutput('sudo docker history {}'.format(image)))
elif operation == 'create_an_image_using_Dockerfile':
    options = form.getvalue()
    print(subprocess.getoutput('sudo docker built {}'.format(options)))
elif operation == 'pull_an_image':
    image = form.getvalue()
    print(subprocess.getoutput('sudo docker pull {}'.format(image)))
elif operation == 'create_an_image_from_a_container':
    container = form.getvalue()
    image_name = form.getvalue()
    print(subprocess.getoutput('sudo docker commit {} {}'.format(container,image_name)))
elif operation == 'remove_an_image':
    image = form.getvalue()
    print(subprocess.getoutput('sudo docker rmi {}'.format(image)))
elif operation == 'start_a_container':
    container = form.getvalue()
    print(subprocess.getoutput('sudo docker start {}'.format(container)))
elif operation == 'stop_a_container':
    container = form.getvalue()
    print(subprocess.getoutput('sudo docker stop {}'.format(container)))
elif operation == 'restart_a_container':
    container = form.getvalue()
    print(subprocess.getoutput('sudo docker restart {}'.format(container)))
elif operation == 'kill_a_container':
    container = form.getvalue()
    print(subprocess.getoutput('sudo docker kill {}'.format(container)))
elif operation == 'attach_a_container':
    container = form.getvalue()
    print(subprocess.getoutput('sudo docker attach {}'.format(container)))

print('</pre>')
