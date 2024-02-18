from fastapi import FastAPI

app = FastAPI()

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

@app.get("/")
async def root():
    test01 = get_full_name("john", "doe")
    test02 = get_name_with_age(test01, 20)
    return {"HEEHE": test01, "Jackson":test02}