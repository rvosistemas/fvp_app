FROM python:3.12-slim

ARG FAST_API_WORKDIR

WORKDIR /${FAST_API_WORKDIR}

COPY requirements.txt /${FAST_API_WORKDIR}/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /${FAST_API_WORKDIR}/requirements.txt

COPY . /${FAST_API_WORKDIR}