from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import auth_router
from routes.events import event_router
from routes.scheduling import scheduling_router

# ✅ Create FastAPI app
app = FastAPI(
    title="AI-Powered Smart Calendar Assistant",
    description="An intelligent calendar assistant with AI-based scheduling and event management.",
    version="1.0.0"
)

# ✅ Enable CORS (For React.js Frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Change to specific domains in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allow all headers
)

# ✅ Include API routes
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(event_router, prefix="/events", tags=["Events"])
app.include_router(scheduling_router, prefix="/scheduling", tags=["Scheduling"])

# ✅ Root Endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the AI-Powered Smart Calendar Assistant!"}
