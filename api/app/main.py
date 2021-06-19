import os
import uuid
from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi import File
from fastapi import Request
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from tools.make_as_scan import MakeAsScan
from tools.merge_pdfs import merge_pdfs

app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://46.101.193.74",
    "http://46.101.193.74:8080"
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
    pages: List[int]
    signature: str


@app.post("/scan/")
async def make_scan(scan: Scan):
    output_path = f'tmp/{uuid.uuid4()}.pdf'
    MakeAsScan(
        scan.path,
        output_path,
        pages_with_signatures=scan.pages,
        signatures=[scan.signature]
    ).process_file()
    return output_path


class MergeInput(BaseModel):
    pdfs: List[str]


@app.post("/merge/")
async def merge(payload: MergeInput):
    output_path = f'tmp/{uuid.uuid4()}.pdf'
    merge_pdfs(payload.pdfs, output_path)
    return output_path


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0',
                port=8000,
                reload=True)
