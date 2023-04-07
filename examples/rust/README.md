## How to build a distroless cc image to run rust applications

Follow the [Quick Guide](/instructions/quickstart.md) to learn about creating custom distroless images.

Assuming you have the prerequisites (such as minimum system requirements, familiarity with Marinara) satisfied, you can run the following docker build command to create a cc distroless image:

`docker build . -t distroless/cc:2.0 -f dockerfiles/dockerfile-new-image --build-arg MARINER_VERSION=2.0 --build-arg IMAGE_TYPE="custom" --build-arg PACKAGES_TO_INSTALL="distroless-packages-minimal libgcc"`

Take a look at the [Docker Commands](/instructions/dockercommands.md) to learn more about the other variations that are available while creating cc distroless image, such as `debug`, `nonroot`, and `debug-nonroot`.