from typing import Optional
from pydantic import BaseModel
import uvicorn
import json
import copy
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import sys

from pyMongoHelper import PyMongoHelper

class MovieHelper(PyMongoHelper):
    def __init__(self,**kwargs):
        super(MovieHelper, self).__init__(**kwargs)
        
    # def runTime(self, minrt=0, maxrt=99999, skip=0, limit=100):
    #     """ Add comments soon
    #     """
    #     self.cnx.setCollection('title_basics')

    #     query = { 
    #         "runtimeMinutes":{
    #              "$gt": minrt,
    #              "$lt":maxrt}
    #     }

    #     params = {
    #         "minrt":minrt,
    #         "maxrt":maxrt
    #     }
        
    #     data = self.get(query)

    #     return self.packageResults("runtime",data,params,skip,limit)

    # def moviesByActor(self,actorName,skip=0,limit=100):
    #     """
    #     Runs the following queries to make this work. 
    #     1) Get the name constant:   
    #         db.name_basics.find({primaryName:"Sandra Bullock"}).pretty()
    #     2) Get the titles for that name const: 
    #         db.title_principals.find({nconst:"nm0000113"},{_id:0,tconst:1})
    #     3) Get all the actors in all the titles: 
    #         db.title_principals.find({tconst: {$in: ["tt0096931", "tt0098185", "tt0098832", "tt0098951", "tt0100930", "tt0102343", "tt0105807", "tt0106697", "tt0106913", "tt0108327", "tt0108473", "tt0108596", "tt0111257", "tt0113957",  "tt0114924", "tt0116621"]}},{_id:0,nconst:1}).count()

    #     """
    #     self.setCollection("name_basics")

    #     query = {
    #         "primaryName":actorName
    #     }

    #     result1 = list(self.coll.find(query,{"_id":0,"nconst":1}))
    #     nconst = result1[0]["nconst"]

    #     print(nconst)

    #     self.setCollection("title_principals")
    #     result2 = list(self.coll.find({"nconst":nconst},{"_id":0,"tconst":1}))
        
    #     movies = []
    #     for row in result2:
    #         movies.append(row["tconst"])

    #     result3 = list(self.coll.find({"tconst": {"$in": movies}},{"_id":0,"nconst":1}))

    #     nconsts = []
    #     for row in result3:
    #         nconsts.append(row["nconst"])

        

    #     self.setCollection("name_basics")

    #     # sendBack = []

    #     # for nconst in nconsts:
    #     #     result = list(self.coll.find({"nconst": nconst},{"_id":0,"primaryName":1}))
    #     #     sendBack.append(result[0])

    #     # return sendBack

    #     data = list(self.coll.find({"nconst": {"$in": names}},{"_id":0,"primaryName":1}))

    #     filteredData = {}
    #     for row in data:
    #         if not row["primaryName"] in filteredData:
    #             filteredData[row["primaryName"]] = 0
    #         filteredData[row["primaryName"]] += 1

    #     names = sorted(list(filteredData.keys()))

    #     return {"count":len(names),"data":names}



# def workedWith(self,actorName):
#     pass


def packageResults(self,route,query,params,skip,limit):
    results1 = list(self.coll.find(query,{"_id":0}))
    total = len(results1)
    pages = ceil(float(total)/float(limit))

    #query["isAdult"] = 0

    results2 = list(self.coll.find(query,{"_id":0}).skip(skip).limit(limit))

    #skip = 400 , limit=100
    if skip > 0:
        current_page = (skip/limit) + 1
    else:
        current_page = 1

    prevVal = skip - limit
    if skip < 0:
        skip = 0

    nextVal = skip + limit
    if nextVal > total:
        nextVal = total-limit

    pstring = ""

    for k,v in params.items():
        pstring += f"{k}={v}&"


    prevLink = f"http://killzombieswith.us:8000/{route}/?{pstring}skip={prevVal}"
    nextLink = f"http://killzombieswith.us:8000/{route}/?{pstring}skip={nextVal}"

    return {"count":total,"pages":pages,"current_page":current_page,"prev":prevLink,"next":nextLink,"data":results2}



description = """
ChaChaCha-Movie API helps you do awesome movie trivia. 🚀

## Movies

* **Find Movies** (_not implemented_).

## Actors

You will be able to:

* **Find Actors** (_not implemented_).
"""

app = FastAPI(
    title="ChaChaCha-Movies",
    description=description,
    version="0.0.1",
    terms_of_service="http://killzonmbieswith.us/terms/",
    contact={
        "name": "Cha Cha Schwarzenegger",
        "url": "http://killzonmbieswith.us/contact/",
        "email": "chacha@killzonmbieswith.us",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


movieHelp = MovieHelper(db='moviesDb',collName='name_basics')


#####################################################

class MovieTitle(BaseModel):
    Subj: Optional[str] = None
    Crse: Optional[str] = None
    tconst: Optional[str] = None
    titleType: Optional[str] = None
    primaryTitle: Optional[str] = None
    originalTitle: Optional[str] = None
    isAdult: Optional[int] = None
    startYear: Optional[int] = None
    endYear: Optional[int] = None
    runtimeMinutes: Optional[int] = None
    genres: Optional[str] = None


"""
  ___  ___  _   _ _____ ___ ___ 
 | _ \/ _ \| | | |_   _| __/ __|
 |   / (_) | |_| | | | | _|\__ \
 |_|_\\___/ \___/  |_| |___|___/
                               
"""

@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")

@app.post("/titlekw/")
async def getNames(title:MovieTitle):
    query = {}
    for k,v in dict(title).items():
        print(k,v)
        if not v is None:
            query[k] = v
    return movieHelp.getSome(coll="title_basics",query=query)
    
@app.get("/names/")
async def getNames(skip: int = 0, limit: int = 100, page:int = None):
    """ 
    Description:
        Get all information (documents) dealing with names in the movie industry
    Params: 
        (int) skip : how many docs to skip
        (int) limit: max returned documents 
        (int) page : page determines how many docs (rows) to skip
    Returns:
        dict / json 
    """
    return movieHelp.getAll(coll="name_basics",skip=skip,limit=limit,page=page)

@app.get("/title/")
async def getTitles(skip: int = 0, limit: int = 100, page:int = None):
    """ 
    Description:
        Get all docs dealing with movie titles
    Params: 
        (int) skip : how many docs to skip
        (int) limit: max returned documents 
        (int) page : page determines how many docs (rows) to skip
    Returns:
        dict / json 
    """
    return movieHelp.getAll(coll="title_basics",skip=skip,limit=limit,page=page)

@app.get("/principals/")
async def getPrincipals(skip: int = 0, limit: int = 100, page:int = None):
    """ 
    Description:
        Get all documents dealing with people who worked on movies: actors, directors, key grips, etc.
    Params: 
        (int) skip : how many docs to skip
        (int) limit: max returned documents 
        (int) page : page determines how many docs (rows) to skip
    Returns:
        dict / json 
    """
    movieHelp.setCollection("title_principals")
    return movieHelp.getAll(coll="title_principals",skip=skip,limit=limit,page=page)

@app.get("/rating/")
async def getRating(min:float = None, max:float = None, skip: int = 0, limit: int = 100, page:int = None):
    """ 
    Description:
        Get all documents dealing with movie ratings
    Params: 
        (int) min :  min rating
        (int) max :  max rating
        (int) skip : how many docs to skip
        (int) limit: max returned documents 
        (int) page : page determines how many docs (rows) to skip
    Returns:
        dict / json 
    """
    query = {}
    if min != None and max != None:
        query["averageRating"]  = {
            "$gte": min,
            "$lte": max
        }
    elif min != None:
        query["averageRating"]  = {
            "$gte": min
        }
    elif max != None:
        query["averageRating"]  = {
            "$lte": max
        }
        
    return movieHelp.getSome(coll="title_ratings",query=query,skip=skip,limit=limit,page=page)

@app.get("/runtime/")
async def getTitlesByRuntime(minrt: int=0,maxrt:int = 99999, skip: int = 0, limit: int = 100):
    return movieHelp.runTime(minrt, maxrt, skip, limit)

# @app.get("/movieByActor/")
# async def movieByActor(actorName:str, skip: int = 0, limit: int = 100):
#     return movieHelp.moviesByActor(actorName,skip,limit)


# @app.get("/genres/")
# async def getGenres():
#     movieHelp.setCollection("title_basics")
#     genres = []
#     skip = 0

#     for i in range(500):
#         result = movieHelp.getSome({},{"genres":1},skip,1000)
    
#         # {'genres': ['Animation', 'Short']}
#         for row in result:
#             if row['genres']:
#                 genres.extend(row['genres'])

#         skip += 1000

#     fixed = sorted(list(set(genres)))
#     return {"genres":fixed,"count":len(fixed)}

@app.get("/genres/")
async def getGenres():

    result = movieHelp.get(collName="genres")

    genres = result[0]["genres"]

    return {"genres":genres,"count":len(genres)}



if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, log_level="info", reload=True)





