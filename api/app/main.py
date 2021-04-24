import os
import uuid

import uvicorn
from fastapi import FastAPI
from fastapi import File
from fastapi import Request
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from tools.merge_pdf import MakeAsScan

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/tmp", StaticFiles(directory="tmp"), name="media")


@app.post("/upload/")
async def upload(file: bytes = File(...)):
    target_path = f'tmp/{uuid.uuid4()}.pdf'
    with open(target_path, 'wb') as f:
        f.write(file)
    return target_path


@app.delete("/upload/")
async def delete(request: Request):
    body = await request.body()
    os.remove(body[1:-1])


class Scan(BaseModel):
    path: str


@app.post("/scan/")
async def make_scan(scan: Scan):
    output_path = f'tmp/{uuid.uuid4()}.pdf'
    MakeAsScan(scan.path, output_path).process_file()
    return output_path


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0',
                port=8000,
                reload=True)
