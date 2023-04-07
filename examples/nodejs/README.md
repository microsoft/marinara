## How to build a distroless nodejs image

Follow the [Quick Guide](/instructions/quickstart.md) to learn about creating custom distroless images.

Assuming you have the prerequisites (such as minimum system requirements, familiarity with Marinara) satisfied, you can run the following docker build command to create a nodejs distroless image:

`docker build . -t distroless/nodejs:16 -f dockerfiles/dockerfile-new-image --build-arg MARINER_VERSION=2.0 --build-arg IMAGE_TYPE="custom" --build-arg PACKAGES_TO_INSTALL="distroless-packages-minimal nodejs"`

Take a look at the [Docker Commands](/instructions/dockercommands.md) to learn more about the other variations that are available while creating nodejs distroless image, such as `debug`, `nonroot`, and `debug-nonroot`.