FROM python:3.11.9-slim

ENV PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd --create-home --shell /usr/sbin/nologin appuser && chown -R appuser:appuser /app

USER appuser

CMD ["python", "-c", "from src.state.schema import AgentState; print(AgentState())"]
