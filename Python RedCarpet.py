#import json
#import os
#import csv

#path_redCarpet = 'C:/Users/gaurav_pandey/Downloads/Softwares/Data File/RedCarpet/socialmediadata-tweets-' \
                 'of-congress-november/socialmediadata-tweets-of-congress-november'

#os.chdir(path_redCarpet)
#print os.getcwd();

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

# redCarpet_data_1ist = json.load(open('2017-11-01.json'))
# redCarpet_data_1ist = redCarpet_data_1ist + json.load(open('2017-11-02.json'))
# redCarpet_data_1ist = redCarpet_data_1ist + json.load(open('2017-11-03.json'))

# for i in redCarpet_data_1ist:
#    for key, value in i.iteritems():
#        print key, value
# print(type(redCarpet_data_1ist))


#for i in redCarpet_data_1ist:
#    print(i)

# Metrics involved in the data: ID, ScreenName, User_ID, Time, Link, Text, Source
# with open("consolidated_RedCarpet.csv",'wb') as main_file:
#    write = csv.writer(main_file,quoting=csv.QUOTE_NONE)
#    write.writerow(redCarpet_data_1ist)

#05-03-2018

import json
import os
import csv
import pandas as pd

path_redCarpet = 'C:/Users/gaurav_pandey/Downloads/Softwares/Data File/RedCarpet/socialmediadata-tweets-' \
                 'of-congress-november/socialmediadata-tweets-of-congress-november'

os.chdir(path_redCarpet)
print os.getcwd();

redCarpet_data_1ist = json.load(open('2017-11-01.json'))
redCarpet_data_1ist = redCarpet_data_1ist + json.load(open('2017-11-02.json'))
redCarpet_data_1ist = redCarpet_data_1ist + json.load(open('2017-11-03.json'))

final_redCarpet = pd.DataFrame.from_records(redCarpet_data_1ist)

final_redCarpet.to_csv("consolidated_RedCarpet.csv",sep=",",encoding='utf-8')

#749 unique accounts
new_selection_all = final_redCarpet.groupby('user_id').agg({'user_id':"count"})
print(new_selection_all.count())

#254 unique accounts that have called-up Trump in Text column.
new_selection_trump = final_redCarpet[final_redCarpet['text'].str.contains('Trump')].groupby('user_id').agg({'user_id':"count"})
print(new_selection_trump.count())





