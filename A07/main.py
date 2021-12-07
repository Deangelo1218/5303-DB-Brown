from fastapi import FastAPI
from routes.schedules_routes import student_api_route
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(student_api_route)

origins = ['http://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)
