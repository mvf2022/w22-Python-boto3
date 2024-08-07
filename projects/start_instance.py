from awscode import listInstances,startInstances

dev_filter = {'Name': 'tag:env', 'Values': ['dev']}

l = listInstances(dev_filter)
startInstances(l)