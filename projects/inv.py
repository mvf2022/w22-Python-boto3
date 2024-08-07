import os 
import platform 
import psutil 



# if 'Windows' in platform.system():
#     os.system('clear')
#     cpu_count = os.cpu_count()
#     mem_info = psutil.virtual_memory().total
#     os_version = platform.platform()
#     python_version = platform.python_version()
#     print(f"""
#           number of cpu: {cpu_count} 
#           Total Memory: {mem_info/(1024**3):.2f} GB 
#           Os Version: {os_version} 
#           Python Version: {python_version}""")
    
# else:
#     pass   
os.system('clear')
cpu_count = os.cpu_count()
mem_info = psutil.virtual_memory().total
os_version = platform.platform()
python_version = platform.python_version()
print(f"""
    number of cpu: {cpu_count} 
    Total Memory: {mem_info/(1024**3):.2f} GB 
    Os Version: {os_version} 
    Python Version: {python_version}""")