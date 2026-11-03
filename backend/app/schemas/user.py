from pydantic import BaseModel, EmailStr, Field, ConfigDict, model_validator

class UserRegister(BaseModel):
    username: str = Field(..., example="srinivas")
    email: EmailStr = Field(..., example="xxx@xxx.com")
    password: str = Field(..., min_length=8, example="password123")
    first_name: str = Field(..., example="srinivas")
    last_name: str = Field(..., example="reddy")
    phone_number: str | None = Field(None, example="1234567890")

class UserUpdate(BaseModel):
    first_name: str | None = Field(None, example="srinivas")
    last_name: str | None = Field(None, example="reddy")
    phone_number: str | None = Field(None, example="1234567890")
    
class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8)
    confirm_password: str

    @model_validator(mode="after")
    def validate_passwords(self):
        if self.new_password != self.confirm_password:
            raise ValueError(
                "New password and confirm password do not match"
            )

        if self.current_password == self.new_password:
            raise ValueError(
                "New password must be different from current password"
            )

        return self
     
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: str | None
    is_admin: bool

    model_config = ConfigDict(from_attributes=True)