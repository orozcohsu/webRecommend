#!/usr/bin/python 

import re

with open('/tmp/result.txt','r') as myfile:
    aa = myfile.readlines()

pat = '[0-9.]+'

result_file = open("/tmp/mahout_result.csv","w")

for a in aa:
    bb = re.findall(pat, a)
    
    if len(bb) == 7:
        result_file.write("%s,%s,%.10f\n" % (bb[0],bb[1],float(bb[2])))
        result_file.write("%s,%s,%.10f\n" % (bb[0],bb[3],float(bb[4])))
        result_file.write("%s,%s,%.10f\n" % (bb[0],bb[5],float(bb[6])))
    
result_file.close()






