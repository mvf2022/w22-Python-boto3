import jenkins

try:
    Jenkins_url='http://54.160.108.55:8080'
    Jenkins_username='devops'
    Jenkins_pass='devops'
    server = jenkins.Jenkins(Jenkins_url, Jenkins_username, Jenkins_pass)
    number_job = server.jobs_count()
    job_name=server.get_all_jobs()
    #list_job = server.get
    user=server.get_whoami()
    jobs=server.get_all_jobs()
    print(number_job)
    print(job_name)
    print("************************************")
    print(user)
    for job in jobs:
        print("**********************************************")
        print(job["name"])
except:
    print("Please double check jenkins url and credentials")