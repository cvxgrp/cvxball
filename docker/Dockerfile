# syntax=docker/dockerfile:1.14
FROM python:3.13-slim

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:0.6.9 /uv /bin/uv
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

# Create non-root user early
RUN useradd -m app_user && \
    chown app_user:app_user /app

# Copy and install dependencies first for better caching
COPY --chown=app_user:app_user uv.lock pyproject.toml README.md /app/

# No dev dependencies,
RUN uv sync --frozen --no-dev && rm -rf /uv /bin/uv && rm uv.lock pyproject.toml

# Copy the application code
COPY --chown=app_user:app_user src/cvx/ball/ ./cvx/ball/

# Switch to non-root user
USER app_user

# Expose the Flight server port
EXPOSE 8080

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Run the server
CMD [".venv/bin/python", "cvx/ball/server.py"]
