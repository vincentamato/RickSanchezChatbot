# Use an official Python runtime as a parent image
FROM python:3.11.5-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install dependencies
# gcc and git are required for building some of the dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
# It's a good practice to pin the versions for reproducibility
RUN pip install --no-cache-dir torch transformers bitsandbytes trl peft datasets scipy

# Install transformers from source
RUN pip install --no-cache-dir git+https://github.com/huggingface/transformers
RUN pip install --no-cache-dir git+https://github.com/huggingface/peft


# Copy the current directory contents into the container at /usr/src/app
COPY . .

CMD [ "python", "./test.py" ]
