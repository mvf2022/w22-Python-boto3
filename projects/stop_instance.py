from awscode import listInstances,stopInstance

dev_filter = {'Name': 'tag:env', 'Values': ['dev']}

instances = listInstances(dev_filter)
stopInstance(instances)

