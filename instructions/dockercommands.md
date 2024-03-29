# Docker Commands

## Use the following docker commands to generate different variations of the distroless container images

### To create distroless container images from scratch, use the following instructions

|Distroless Image|Docker Command|
|-|-|
| **distroless/minimal:2.0** | `docker build . -t distroless/minimal:2.0 -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="minimal"` |
| **distroless/minimal:2.0-nonroot** | `docker build . -t distroless/minimal:2.0-nonroot -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="minimal-nonroot" --build-arg USER="nonroot" --build-arg USER_UID=65532` |
| **distroless/minimal:2.0-debug** | `docker build . -t distroless/minimal:2.0-debug -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="minimal-debug"` |
| **distroless/minimal:2.0-debug-nonroot** | `docker build . -t distroless/minimal:2.0-debug-nonroot -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="minimal-debug-nonroot" --build-arg USER="nonroot" --build-arg USER_UID=65532` |
| **distroless/base:2.0** | `docker build . -t distroless/base:2.0 -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="base"` |
| **distroless/base:2.0-nonroot** | `docker build . -t distroless/base:2.0-nonroot -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="base-nonroot" --build-arg USER="nonroot" --build-arg USER_UID=65532` |
| **distroless/base:2.0-debug** | `docker build . -t distroless/base:2.0-debug -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="base-debug"` |
| **distroless/base:2.0-debug-nonroot** | `docker build . -t distroless/base:2.0-debug-nonroot -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="base-debug-nonroot" --build-arg USER="nonroot" --build-arg USER_UID=65532` |
| **distroless/cc:2.0** | `docker build . -t distroless/cc:2.0 -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base libgcc"` |
| **distroless/cc:2.0-nonroot** | `docker build . -t distroless/cc:2.0-nonroot -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom-nonroot" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base libgcc" --build-arg USER="nonroot" --build-arg USER_UID=65532` |
| **distroless/cc:2.0-debug** | `docker build . -t distroless/cc:2.0-debug -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom-debug" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base libgcc"` |
| **distroless/cc:2.0-debug-nonroot** | `docker build . -t distroless/cc:2.0-debug-nonroot -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom-debug-nonroot" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base libgcc" --build-arg USER="nonroot" --build-arg USER_UID=65532` |
| **distroless/nodejs:18** | `docker build . -t distroless/nodejs:18 -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base nodejs18"` |
| **distroless/nodejs:18-nonroot** | `docker build . -t distroless/nodejs:18-nonroot -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom-nonroot" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base nodejs18" --build-arg USER="nonroot" --build-arg USER_UID=65532` |
| **distroless/nodejs:18-debug** | `docker build . -t distroless/nodejs:18-debug -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom-debug" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base nodejs18"` |
| **distroless/nodejs:18-debug-nonroot** | `docker build . -t distroless/nodejs:18-debug-nonroot -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom-debug-nonroot" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base nodejs18" --build-arg USER="nonroot" --build-arg USER_UID=65532` |
| **distroless/python:3** | `docker build . -t distroless/python:3 -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base python3"` |
| **distroless/python:3-nonroot** | `docker build . -t distroless/python:3-nonroot -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom-nonroot" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base python3" --build-arg USER="nonroot" --build-arg USER_UID=65532` |
| **distroless/python:3-debug** | `docker build . -t distroless/python:3-debug -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom-debug" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base python3"` |
| **distroless/python:3-debug-nonroot** | `docker build . -t distroless/python:3-debug-nonroot -f dockerfiles/dockerfile-new-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TYPE="custom-debug-nonroot" --build-arg PACKAGES_TO_INSTALL="distroless-packages-base python3" --build-arg USER="nonroot" --build-arg USER_UID=65532` |

### To extend existing distroless container images, use the following instructions

|Distroless Image|Docker Command|
|-|-|
| **distroless/python:2.0** | `docker build . -t distroless/python:2.0 -f dockerfiles/dockerfile-extend-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TO_MODIFY="distroless/minimal:2.0" --build-arg PACKAGES_TO_INSTALL="python3"` |
| **distroless/python:2.0-debug** | `docker build . -t distroless/python:2.0-debug -f dockerfiles/dockerfile-extend-image --build-arg AZL_VERSION=2.0 --build-arg IMAGE_TO_MODIFY="distroless/minimal:2.0-debug" --build-arg PACKAGES_TO_INSTALL="python3"` |
| **distroless/python:3.0** | `docker build . -t distroless/python:3.0 -f dockerfiles/dockerfile-extend-image --build-arg AZL_VERSION=3.0 --build-arg IMAGE_TO_MODIFY="distroless/minimal:3.0" --build-arg PACKAGES_TO_INSTALL="python3"` |
| **distroless/python:3.0-debug** | `docker build . -t distroless/python:3.0-debug -f dockerfiles/dockerfile-extend-image --build-arg AZL_VERSION=3.0 --build-arg IMAGE_TO_MODIFY="distroless/minimal:3.0-debug" --build-arg PACKAGES_TO_INSTALL="python3"` |