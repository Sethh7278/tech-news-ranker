FROM python:3.13-slim

WORKDIR /tech-news-ranker

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your project in
COPY . .

# The command that runs when the container starts
CMD ["python", "tech-news-ranker.py"]