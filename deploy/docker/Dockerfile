# Ledger — container image (scaffold)
FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    default-mysql-client \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir ledger

ENV LEDGER_HOME=/var/lib/ledger
VOLUME /var/lib/ledger

USER nobody
ENTRYPOINT ["ledger"]
CMD ["dashboard"]
