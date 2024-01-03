import jenkins
import os



host_name = os.environ.get("JENKINS_HOST", "localhost:8008")
port = "8080"
url = f"https://{host_name}/version"
server = jenkins.Jenkins(url, username='myuser', password='mypassword')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
