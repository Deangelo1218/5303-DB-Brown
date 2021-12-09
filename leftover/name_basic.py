from os import read
from pydantic.errors import NumberNotMultipleError
from mysqlCnx import MysqlCnx
from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
import csv


with open('/var/www/html/api/movies/.config.json') as f:
    config = json.loads(f.read())

cnx = MysqlCnx(**config)
#Reading TSV file:
#create a List of Professions at the top in line 7
#Add Professions =Set()
#Add count =0
Profession =set()
count =0
name =''
# tsv_file = open("/var/www/html/api/movies/name.basics.tsv")

# #new_file = open("names.txt", "x")
# read_tsv = csv.reader(tsv_file, delimiter="\t")
# heading = next(read_tsv)
# inserting some info from the file to profession table :
##proffesions
# for row in read_tsv:
#     pass
# sql_query= "INSERT INTO `people`(`pid`, `Name`, `birth`, `died`) VALUES ({person_id},{Name},{birth},{died})"
# sql ='INSERT INTO `Genre` (`gid`, `genre`) VALUES ("{names}", "{genre}")'.format(names=name,genre=gen)

# for row in read_tsv:
#     # temp = row[4].split(',')
#     if row[1] == '\\N':
#         Name = None
#     else:
#         Name = row[1]

#     if row[2] == '\\N':
#         birth = None
#     else:
#         birth = row[2]
    
#     if row[3] == '\\N':
#         died = None
#     else:
#         died = row[3]
    
#     person_id = row[0]

# `mid` varchar(10) NOT NULL,
#   `avgRating` float(5,2) DEFAULT NULL,
#   `numVotes` 

#Loading title.ratings file into ratings table

# new_tsv_file = open("/var/www/html/api/movies/title.ratings.tsv")
# read_file = csv.reader(new_tsv_file, delimiter="\t")
# heading = next(read_file)

# for row in read_file:
#     mid = row[0]
#     if row[1] == '':
#         avgRating = None
#     else:
#         avgRating = row[1]
#     if row[2] == '':
#         numVotes = None
#     else:
#         numVotes = row[2]

    #sql_query = 'INSERT INTO `ratings`(`mid`, `avgRating`, `numVotes`) VALUES ("{mid}","{avgRating}","{numVotes}")'.format(mid=mid, avgRating= avgRating, numVotes= numVotes)

    #cnx.query(sql_query)

title_basics_tsv = open("/var/www/html/api/movies/title.basics.tsv")
read_title = csv.reader(title_basics_tsv, delimiter="\t")
heading = next(read_title)
i = 0
f = open("sql.out","w")
	# mid	title	adult	released	runTime
for row in read_title:
    mid = row[0]
    if row[2] == ' ':
        title = None
    else:
        title = row[2]
    if row[4] == '\\N':
        adult = None
    else:
        adult = row[4]
    if row[5] == '\\N':
        released = None
    else:
        released = row[5]
    if row[7] == '\\N':
        runTime = 0
    else:
        runTime = row[7]
    
    

    sql_query = 'INSERT INTO `movie`(`mid`, `title`, `adult`, `released`, `runTime`) VALUES ("{mid}","{title}","{adult}","{released}","{runTime}")'.format(mid=mid, title=title, adult=adult, released=released, runTime=runTime)
    #f.write(sql_query+'\n')
    i+=1
    if i >= 1000:
        break
    result = cnx.query(sql_query)
    if not result['success']:
        f.write(str(result['error'])+'\n')
        f.write(sql_query+'\n')
        
    #cnx.query(sql_query)
    #print(mid, avgRating, numVotes)

    



    #print(person_id, Name, birth, died)
    #sql_query= 'INSERT INTO `people`(`pid`, `Name`, `birth`, `died`) VALUES ("{pid}","{Name}","{birth}","{died}")'.format(pid=person_id,Name=Name,birth=birth, died=died)


    # insert_query = (person_id, Name, birth, died)
    #cnx.query(sql_query)


    # for profession in temp:
    #     if('//' in profession):
            
    # print(temp)
    # if ('actor' in temp) or ('writer' in temp) or ('director' in temp) or ('actress' in temp) or ('soundtrack' in temp)  and 1 == 0:
    #     if row[1] == '\\N':
    #         name = None
    #     else:
    #         name = row[1].split(' ')
    #         first_name = name[0]
    #         last_name = name[1]
        
    #     if row[2] == '\\N':
    #         birthYear = None
    #     else:
    #         birthYear = row[2]
        
    #     if row[3] == '\\N':
    #         deathYear = None
    #     else:
    #         deathYear = row[3]
    #     if row[4] == '\\N':
    #         professions = None
    #     else:
    #         professions = row[4].split(',')
    #         if len(professions) == 3:
    #             first_profession = professions[0]
    #             second_profession = professions[1]
    #             thrid_profession = professions[2]
    #         elif len(professions) == 2:
    #             first_profession = professions[0]
    #             second_profession = professions[1]
    #         elif len(professions) == 1:
    #             first_profession = professions[0]
    #     if row[5] == '\\N':
    #         knownFor = None
    #     else:
    #         knownFor = row[5]
        
    #     actorID = row[0]
    # data = (actorID, first_name, last_name, birthYear, deathYear, first_profession , second_profession, thrid_profession, knownFor)
    # print(data)
    # for movies in data:
    #     n_id = data[0]
    #     print(n_id)
       

    # person = data[0]
    #print(person)
    #adding column 5 to profession one by one:
    #prof = row[4].split(',') # this is Column 5
    #print(prof)
    # for p in prof:
    #     if('//' not in p):
    #         #print(p)
    #         Profession.add(p)
            #new_file.write(str(Profession))
            #print(Profession)
    # if row[1] == '\\N':
    #     actor_name = None
    # # else:
    #     actor_name = row[1].split(' ')
    # if len(actor_name) == :
    #     middle_name = actor_name[1]
    
   
    # if len(first_name) <= 2:
    #      print(first_name)
   
   
    # for first_name in actor_name:
    #     first_name_variable = first_name[0]
    #     print(first_name_variable)
    #new_file.write(actor_name)

    
    #print(actor_name)



        

    # for profs in Profession:
    #     if(profs != ''):
    #         name = "p00"+str(count)
    #         print(prof, name)
    #         ##sql ='INSERT INTO `Profession` (`proid`, `profession`)  VALUES ("{ProfessionID}", "{Job}")'.format(ProfessionID=name,Job=profs)
    #     ## cnx.query(sql)

    #         count+=1
            #print(prof, name)
        


# if row[1] == '\\N':
#                 name = None
#             else:
#                 name = row[1]
            
#             if row[2] == '\\N':
#                 birthYear = None
#             else:
#                 birthYear = row[2]
            
#             if row[3] == '\\N':
#                 deathYear = None
#             else:
#                 deathYear = row[3]
            
#             if row[4] == '\\N':
#                 professions = None
#             else:
#                 professions = row[4]
            
#             if row[5] == '\\N':
#                 knownFor = None
#             else:
#                 knownFor = row[5]

# # Loop through rows first name middle name last name example
# for row in reader:
#     names = row["name"].split()

#     if len(names) == 2:
#         first = names[0].strip()
#         last = names[1].strip()
#         db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
#                    first, None, last, row["house"], int(row["birth"]))

#     elif len(names) == 3:
#         first = names[0].strip()
#         middle = names[1].strip()
#         last = names[2].strip()
#         db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
#                    first, middle, last, row["house"], int(row["birth"]))