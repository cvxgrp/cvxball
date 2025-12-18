# Docker Build Configuration

This directory contains the Dockerfile and related configuration for building container images.

## Files

- Dockerfile — Multi-stage Docker build configuration
- Dockerfile.dockerignore — Build-context ignore rules scoped to this Dockerfile (see Notes)

## Building the Image

Build from the repository root, using the root directory as the build context:

```bash
# Validate locally (loads the image into your Docker engine)
docker buildx build \
  --file docker/Dockerfile \
  --tag <image-name> \
  --load \
  .
```

This is the same command used by the CI workflow (see .github/workflows/docker.yml).

## Notes on Dockerfile.dockerignore

- Docker/BuildKit supports a per-Dockerfile ignore file located next to the Dockerfile, named `Dockerfile.dockerignore`.
- This file applies only when building that specific Dockerfile and allows us to keep all Docker-related files together inside the `docker/` folder.
- No repository-root `.dockerignore` or symlink is required.
- The ignore rules are evaluated relative to the build context (here: the repository root `.`). Use paths accordingly.
- You need BuildKit-enabled Docker (e.g., `docker buildx`, which is enabled by default in modern Docker versions).
