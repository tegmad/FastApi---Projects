from pydantic import BaseModel, Field, EmailStr, ConfigDict
from fastapi import FastAPI
import uvicorn 

app = FastAPI()

data = {
    'email': 'tegmadi@gmail.com',
    'bio': "Я Пирожок Вкусный",
    'age': 10
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=100)
    model_config = ConfigDict(extra='forbid')

class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)

users = []

@app.post('/users', summary='Добавить Пользователя', tags=['Добавить'])
def add_user(user: UserAgeSchema):
    users.append(user)
    return {'sucess': True, 'message': 'Юзер добавлен'}

@app.get('/users', summary='Получить Пользователя', tags=['Получить'])
def get_users() -> list[UserAgeSchema]:
    return users 


print(repr(UserAgeSchema(**data)))

if __name__ == "__main__":
    uvicorn.run("test:app", reload=True, host="127.0.0.1", port=3000)