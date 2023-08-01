import os
from kubernetes import client, configdef main():
config.load_kube_config()
v1 = client.CoreV1Api()
print("Listing pods with their status:")pod_status = os.getenv('POD_STATUS')

ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    if i.status.phase == pod_status:
        print("%s\\t%s\\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
if **name** == '**main**':
main()
