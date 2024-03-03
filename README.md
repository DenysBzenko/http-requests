# Middleware to measure the execution time of each request

The PerformanceMiddleware middleware allows us to measure the time of each request to our Django project. It records the start time and end time of that request and writes to a file, such as the HTTP method, URL, and response status. This allows you to analyze server performance and identify possible delays in request processing.

# Logging configuration

The project is configured to record messages of different levels in two different files: debug.log and errors.log. The debug.log file records, for example, informational messages about requests and responses. errors.log records error messages and helps to identify and fix problems with the server.
# Error handling
The project handles errors in accordance with HTTP standards, providing appropriate HTTP statuses in response to incorrect requests or internal errors. In addition, all internal errors are logged for further analysis and correction.
