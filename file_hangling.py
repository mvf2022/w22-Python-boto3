with open("chart.yaml", 'r') as f:
    test=f.readlines()
    
with open("change.yaml", 'w') as l:
    for line in test:
        if 'version:' in line:
            l.write('version: 2.0\n')
        else:
            l.write(line)

            