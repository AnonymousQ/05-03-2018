import json
import os
import csv

path_redCarpet = 'C:/Users/gaurav_pandey/Downloads/Softwares/Data File/RedCarpet/socialmediadata-tweets-' \
                 'of-congress-november/socialmediadata-tweets-of-congress-november'

os.chdir(path_redCarpet)
print os.getcwd();

# files=[f for f in os.listdir('.') if os.path.isfile(f)]
# print(files)
# with open('2017-11-01.json','r') as f:
#    data=json.load(f)
# print(data)
# for file in glob.glob("*.json"):
#    print file
# python treats data from json file as a string and not as a dictionary.

# json_data='{"a":1,"b":2,"c":3,"d":4,"e":5}'
# print(json.loads(json_data))

# loaded_json=json.loads(json_data)
# for i in loaded_json:
#    print("%s: %d" %(i,loaded_json[i]))
# json_dictionary={"ham":"YES","egg":"YES","yolk":"NO"}
# print(json_dictionary["egg"])

 redCarpet_data_1ist = json.load(open('2017-11-01.json'))
 redCarpet_data_1ist = redCarpet_data_1ist + json.load(open('2017-11-02.json'))
 redCarpet_data_1ist = redCarpet_data_1ist + json.load(open('2017-11-03.json'))

# for i in redCarpet_data_1ist:
#    for key, value in i.iteritems():
#        print key, value
# print(type(redCarpet_data_1ist))


for i in redCarpet_data_1ist:
    print(i)

# Metrics involved in the data: ID, ScreenName, User_ID, Time, Link, Text, Source
# with open("consolidated_RedCarpet.csv",'wb') as main_file:
#    write = csv.writer(main_file,quoting=csv.QUOTE_NONE)
#    write.writerow(redCarpet_data_1ist)
