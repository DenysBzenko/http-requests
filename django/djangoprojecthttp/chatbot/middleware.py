import time
import logging

logger = logging.getLogger(__name__)

class PerformanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        end_time = time.time()
        execution_time = end_time - start_time

        self.log_performance(request, response, execution_time)

        return response

    def log_performance(self, request, response, execution_time):
        logger.info(
            f"Request: {request.method} {request.path}, "
            f"Status: {response.status_code}, "
            f"Execution Time: {execution_time:.2f} seconds"
        )
