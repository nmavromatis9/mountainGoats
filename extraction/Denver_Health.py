import json
import csv

#JSON script to extract data from JSON sheet

print("HELLO WORLD!")

try:
    f = open("./../JSON Files/denverhealth.json", 'rb')
except OSError:
    print ("Could not open/read file poudrevalley.json")
    sys.exit()
    
data=json.load(f)

l=len(data[0]['item'])
#print("LEN=", l)

cpt_codes=[10160,11010,21048,21557,32440,32480,32505,33218,33330,33361,33533,36415,45315,45380,45385,50040,59510,61518,71260,72125,72192,72195,72196,73000,74150,74250,80053,81210,81235,81272,82465,82803,82947,83874,84484,85025,86703,88230,99202,99203,99204,99205,99218,99219,99220,99281,99282,99283,99284,99285]

#convert ints to strings with list comprehension
cpt_codes = [str(x) for x in cpt_codes]

for i in range(l):
    for j in cpt_codes:   
        if(data[0]['item'][i]['Associated_Codes'] == j):
            print(data[0]['item'][i])
            #print(i)
