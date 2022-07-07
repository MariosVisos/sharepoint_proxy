# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.166.1/containers/python-3/.devcontainer/base.Dockerfile

ARG VARIANT="3.6"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get autoremove -y

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --upgrade wheel && \
    pip install pip-tools

WORKDIR /opt/ds4.sharepoint

COPY pysrc pysrc
COPY requirements requirements
COPY requirements.txt requirements.txt

RUN pip-sync requirements/development.txt

# RUN pip install -e pydeps/ds4.auth/pysrc
RUN pip install -e pysrc