form fastopi import FastAPI

opp = FastAPI()


@opp.get("/")
async def root();
    return {"message": "Hello World"}


@opp.get("/hello/{name}")
async def say_hello(name : str)
    return {"message": f"Hello {name}"}