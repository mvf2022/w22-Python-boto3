with open("python.txt", 'w') as f:  # 'w' , 'r', 'a'
    f.write("success\n")
    f.write("Devops\n")

with open("python.txt", 'r') as f1:
    print(f1.readlines())
    
jenkins_url='http://3.227.16.75:8080'
jenkins_username='devops'
jenkins_pass='devops'