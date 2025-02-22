#!/bin/bash
set -e

echo "Building Docker image for amd64/linux using gcloud build..."
gcloud builds submit --config cloudbuild.yaml

echo "Deployment complete!"
