FROM python:3.12-slim-bookworm

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000

RUN apt-get update \
    && apt-get install -y --no-install-recommends bash ca-certificates curl git \
    && groupadd --gid "${USER_GID}" "${USERNAME}" \
    && useradd --uid "${USER_UID}" --gid "${USER_GID}" --create-home --shell /bin/bash "${USERNAME}" \
    && python -m venv /opt/venv \
    && chown -R "${USERNAME}:${USERNAME}" /opt/venv \
    && rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY backend/requirements.txt backend/requirements-dev.txt /tmp/backend/
RUN python -m pip install --no-cache-dir -r /tmp/backend/requirements-dev.txt

WORKDIR /workspaces/workshop
USER ${USERNAME}
