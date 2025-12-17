# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Generate the model inside the container (since it's gitignored)
# This respects the constraint of not uploading large files to git
RUN python forecasting_model.py

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variable
ENV PORT=5000

# Run gunicorn when the container launches
# Bind to 0.0.0.0 to make it accessible from outside the container
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
