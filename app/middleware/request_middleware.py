import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class RequestMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request:Request, call_next):
        start_time = time.time()
        
        request_id = str(uuid.uuid4())

        request.state.request_id = request_id

        response = await call_next(request)

        execution_time = time.time() - start_time

        response.headers["X-Request-ID"] = request_id

        response.headers["X-Execution-Time"] = f"{execution_time:.4f}"

        return response
