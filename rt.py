import jenkins 

def jenkins_login(url,username,password):
    server = jenkins.Jenkins(url,username=username, password=password)
    return server

def print_jobs(server):
    number_jobs=server.jobs_count()
    user = server.get_whoami()['fullName']
    _jobs = server.get_all_jobs()
    for job in _jobs:
        print("***********************************************************")
        print(job)

def main():
    try:
        instance=jenkins_login('http://3.227.16.75:8080', 'devops','devops')
        print_jobs(instance)
    except:
        print("Error: Unable to connect to jenkins server")
        
if __name__ == "__main__":
    
    main()          
    