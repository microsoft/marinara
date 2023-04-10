# Marinara

Build distroless images for **CBL-Mariner**!

Marinara is a distroless image builder for CBL-Mariner. It is intended to be modular to create several variations of a distroless image such as `standard` distroless image, distroless image with `debug` option, distroless image with `nonroot` user, or distroless image with both `debug` option and `nonroot` user.

It is designed to be easily used with Docker.

## Getting Started
-  How to use Marinara

    1.  Clone the source repository.
    2.  Change directory to `marinara`.
    3.  Run the docker build command that is suitable for your use case. Follow the [Docker Commands](/instructions/dockercommands.md) (located at `marinara/instructions`) to learn how a specific docker build command can be used to produce or extend a distroless image for your specific use case.

    For more details, please read the [Quick Guide](/instructions/quickstart.md) under `marinara/instructions`.

-	Software dependencies
    - Linux System (For example, CBL-Mariner)
    - Docker CLI with Docker Engine version 20.10

## Features

### Create a distroless image from scratch
There are a few distroless image variants that can be created with Marinara. For example, you can create a `standard` distroless image with Mariner packages, or you can create a `debug` version of the image. There are also options to create a distroless image with `nonroot` user in it, and the final variant is a distroless image with **both** the `debug` option and a `nonroot` user.

Use a template dockerfile and a simple docker build command to produce a distroless image composed of Mariner packages from scratch. The template dockerfile `dockerfile-new-image` allows for passing build arguments to docker via the docker build command to create an image. Read more about these build arguments in the Build Arguments section.

### Extend a distroless image

Marinara can be used to extend a CBL-Mariner distroless image by adding packages to it. A CBL-Mariner distroless image has a couple of **container manifest files** (`container-manifest-1` and `container-manifest-2`) located at `/var/lib/rpmmanifest/` that are used to keep track of installed packages in the image. Extending a distroless image relies on these manifests and keeps these files up-to-date. The template dockerfile `dockerfile-extend-image` allows for passing build arguments to docker via the docker build command to extend an image. Read more about these build arguments in the Build Arguments section.

## Tools

### Marinara docker image

Marinara docker image is developed by Mariner team with the goal of producing distroless images. It is based on CBL-Mariner base container image. It is available on MCR for CBL-Mariner version `2.0`. Although, the `1.0` version of the image is not available in MCR, you can create it locally by following instructions in [Marinara image instructions](/instructions/marinaraimage.md).

Additionally, it comes with essential utilities and packages preinstalled that can be used to create a distroless image from scratch or extend a distroless image by adding more packages to it:

- **marinaracreate.py** - Composes an image, given an `image type`, `mariner version`, `packages to install`, and `user`. Some of the arguments can be optional depending on the image type.

- **marinaraextend.py** - Extends a CBL-Mariner distroless image, given an `image to extend`, `mariner version`, and `packages to install`.

Marinara uses `tdnf` package manager under the hood to install packages and their dependencies. The tooling included in the marinara docker image abstracts away the internals of tdnf installation process, along with the process of producing or keeping the container manifest files up-to-date. Although you have the ability to further modify, for a general use case, the starter dockerfiles do not require any modification to produce different flavors of a distroless image.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
