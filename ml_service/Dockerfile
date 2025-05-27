FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask scikit-learn joblib
CMD ["python", "app.py"]