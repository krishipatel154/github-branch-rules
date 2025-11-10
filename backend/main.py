from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Auth Demo API")

# Allow frontend from Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your Vercel URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    email: str
    password: str
    name: str | None = None

@app.get("/")
def home():
    return {"message": "Backend is live!"}

@app.post("/api/signup")
def signup(name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    return {"message": f"User {email} created successfully!"}

@app.post("/api/login")
def login(email: str = Form(...), password: str = Form(...)):
    # Demo: accept any login
    return {"message": "Login successful!", "user": {"email": email}}