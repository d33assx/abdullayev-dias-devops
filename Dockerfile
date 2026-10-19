# Base image with Python installed
FROM python:3.12-alpine

# All following commands run inside /app in the container
WORKDIR /app

# Copy the application source code into the image
COPY app/ .

# Run the tests at build time and create a non-root user for the app
RUN python -m unittest -v test_app && adduser -D appuser

# Default student information (can be overridden with docker run -e)
ENV STUDENT_NAME=Dias \
    STUDENT_SURNAME=Abdullayev \
    STUDENT_GROUP=IT2-2313SE \
    STUDENT_ID=37240

USER appuser

# The application listens on port 8080
EXPOSE 8080

# Command executed when the container starts
CMD ["python", "-u", "app.py"]
