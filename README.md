# orders-api

HTTP API that accepts and tracks customer orders.

## Deployment

Every push to `main` runs `.github/workflows/deploy.yml`. It deploys to the `staging`
environment first and then to `production`. Production needs an approval from a
required reviewer and waits five minutes before it starts.

Production incidents are tracked as issues with the `incident` label.
