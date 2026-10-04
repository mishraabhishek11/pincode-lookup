from fastapi import FastAPI
from exceptions import (NotFoundPinCodeError, not_found_pincode_handler,
                        InvalidPinCodeError, invalid_pincode_handler)
from models import BulkRequest, BulkResponse, LocationResponse
from data import pincode_db


app = FastAPI(
    title="Pin code lookup API",
    description="Find City, State for India with Pin Code",
)

app.add_exception_handler(NotFoundPinCodeError, not_found_pincode_handler)
app.add_exception_handler(InvalidPinCodeError, invalid_pincode_handler)


@app.get("/")
def root():
    return {"message": "Pin code lookup API"}


@app.get("/pincode/{code}", response_model=LocationResponse)
def get_pincode(code: str):
    if not len(code) == 6 or not code.isdigit():
        raise InvalidPinCodeError(code, reason="pin code must be 6 digit")

    if not code in pincode_db:
        raise NotFoundPinCodeError(code)

    return pincode_db[code]


@app.post("/pincode/bulk", response_model=BulkResponse)
def bulk_lookup(request: BulkRequest):
    results = []
    missing = []

    for code in request.pincodes:
        if code in pincode_db:
            results.append(pincode_db[code])
        else:
            missing.append(code)

    return BulkResponse(
        found=len(results),
        not_found=len(missing),
        results=results,
        missing=missing
    )
