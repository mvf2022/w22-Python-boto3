import jenkins
import csv

def listJenkinJobs(url,username,password):
    server = jenkins.Jenkins(url, username=username, password=password)

    _jobs = server.get_all_jobs()
    job_list=[]
    for job in _jobs:
        job_name= job.get('name')
        job_url= job.get('url')
        job_color=job.get('color')
        job_list.append([job_name,job_url,job_color])
    return job_list
    
def storeJenkinsInfo(file_name,job_list):
    with open(file_name, 'w',newline='') as f:
        writer = csv.writer(f)
        HEADER=['Job_name', 'Job_url', 'Job_color']
        writer.writerow(HEADER)
        for j in job_list:
            writer.writerow(j)
            
def main():
    jobs=listJenkinJobs('http://3.227.16.75:8080','devops','devops') 
    storeJenkinsInfo("week22.csv",jobs)
    print("File generated successfully")          

if __name__=="___main___":    
    main()   