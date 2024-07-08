from keystoneclient.auth.identity import v3
from keystoneclient import session
from keystoneclient.v3 import client as keystoneapi
from novaclient import client as novapi
auth_url = 'http://192.168.1.12:35357/v3/'
username = 'admin'
user_domain_name = 'Default'
project_name = 'admin'
project_domain_name = 'Default'
password = 'passw0rd'
auth = v3.Password(auth_url=auth_url,
                   username=username,
                   password=password,
                   project_name=project_name,
                   project_domain_name=project_domain_name,
                   user_domain_name=user_domain_name)
sess = session.Session(auth=auth)
keystone = keystoneapi.Client(session=sess)
#print keystone.projects.list()
nova = novapi.Client(2, session=keystone.session)
print nova.services.list()