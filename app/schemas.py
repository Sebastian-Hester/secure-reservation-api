from pydantic import BaseModel, EmailStr, Field

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ReservationCreate(BaseModel):
    date: str = Field(min_length=10, max_length=10)  # YYYY-MM-DD (we'll validate later)
    party_size: int = Field(ge=1, le=20)
    notes: str | None = Field(default=None, max_length=500)

class ReservationResponse(BaseModel):
    id: int
    user_id: int
    date: str
    party_size: int
    notes: str | None

    class Config:
        from_attributes = True
