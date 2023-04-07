# Quick Start Guide

Marinara docker image `marinara` with current tags `1.0` and `2.0` can be used to build CBL-Mariner distroless image from scratch or extend a CBL-Mariner distroless image.

## How to use marinara docker image with dockerfile-new-image to build a distroless image from scratch

Follow the instructions below to use Marinara to build distroless image from scratch:
- Clone the source repository. Run the following command in your terminal:

    `git clone https://github.com/microsoft/marinara`

- Change directory to **marinara**. Run the following command in your terminal:

    `cd marinara`

- Run the docker build command that is suitable for your use case. Follow the `dockercommands.md` instructions guide (located at `marinara/instructions`) to learn how a specific docker build command can be used to produce a distroless image for your specific use case. For example, to produce a distroless minimal image without the debug option and without a nonroot user, run the following command:

    `docker build . -t distroless/minimal:2.0 -f dockerfiles/dockerfile-new-image --build-arg MARINER_VERSION=2.0 --build-arg IMAGE_TYPE="minimal"`

Read the following build arguments and their possible values to create different flavors of distroless images.

### Build Arguments for `dockerfile-new-image`

| Build Argument Name | Possible Values |
|-|-|
| MARINER_VERSION | `1.0`, `2.0` |
| PACKAGES_TO_INSTALL* | Mariner packages separated by space surrounded by double quotes. For example: `"pkg1 pkg2 pkg3"` |
| PACKAGES_TO_HOLDBACK** | Mariner packages separated by space surrounded by double quotes. For example: `"pkg1 pkg2 pkg3"` |
| IMAGE_TYPE | `minimal`, `minimal-nonroot`, `minimal-debug`, `minimal-debug-nonroot`, `base`, `base-nonroot`, `base-debug`, `base-debug-nonroot`, `custom`, `custom-nonroot`, `custom-debug`, `custom-debug-nonroot` |
| USER*** | `nonroot`  or any username for nonroot user |
| USER_UID*** | `numeric` value for nonroot user other than `0` |

> \* If the value for **IMAGE_TYPE** argument contains `custom`, then you *must* pass a list of valid package name(s) via the **PACKAGES_TO_INSTALL** build argument. That said, you can also pass a value with package names via the **PACKAGES_TO_INSTALL** argument when the **IMAGE_TYPE** argument is `minimal-*` or `base-*` to use these image types as a base for your custom distroless image.

> \** This is an experimental feature that allows for holding back certain packages from getting installed. This argument can be used to forcibly avoid installing dependencies (that would normally get installed as part of package installation) that are not needed in a distroless image enviroment.

> \*** If the value for **IMAGE_TYPE** argument contains `nonroot`, then you must pass a non "`root`" user name via the **USER** build argument and a non "`0`" numeric id via the **USER_UID** build argument.

## How to use marinara docker image with dockerfile-extend-image to extend a distroless image by adding more packages

Follow the instructions below to use Marinara to extend a distroless image:
- Clone the source repository. Run the following command in your terminal:

    `git clone https://github.com/microsoft/marinara`

- Change directory to **marinara**. Run the following command in your terminal:

    `cd marinara`

- Run the docker build command that is suitable for your use case. Follow the `dockercommands.md` instructions guide (located at `marinara/instructions`) to learn how a specific docker build command can be used to extend a distroless image for your specific use case. For example, to extend a preexisting distroless minimal image by adding `libgcc` package to it, run the following command:

    `docker build . -t distroless/minimal:2.0 -f dockerfile-extend-image --build-arg MARINER_VERSION=2.0 --build-arg IMAGE_TO_MODIFY="distroless/minimal:2.0" --build-arg PACKAGES_TO_INSTALL="libgcc"`

Read the following build arguments and their possible values to create different extended images from an existing distroless image.

### Build Arguments for `dockerfile-extend-image`

| Build Argument Name | Possible Values |
|-|-|
| IMAGE_TO_MODIFY | Any CBL-Mariner distroless image that exists either in the local enviroment or can be pulled from a container registry. For example, `distroless/minimal:2.0` |
| MARINER_VERSION* | `1.0`, `2.0` |
| PREEXISTING_MANIFEST_LOCATION** | `"/var/lib/rpmmanifest"` |
| PACKAGES_TO_INSTALL*** | Mariner packages separated by space surrounded by double quotes. For example: `"pkg1 pkg2 pkg3"` |
| PACKAGES_TO_HOLDBACK**** | Mariner packages separated by space surrounded by double quotes. For example: `"pkg1 pkg2 pkg3"` |

> \* The value for **MARINER_VERSION** has to match the CBL-Mariner version for the image passed in **IMAGE_TO_MODIFY**. For example, if the **IMAGE_TO_MODIFY** is `distroless/minimal:2.0`, then the **MARINER_VERSION** has to be `2.0`. The value for **MARINER_VERSION** is not inferred from the **IMAGE_TO_MODIFY**'s value because your tag may not indicate the CBL-Mariner version (i.e., it could be `latest` or something other than `1.0` and `2.0`).

> \** No need to explictly pass this value as it is defaulted to this value. This is the location of the container manifest files i.e., `container-manifest-1` and `container-manifest-2`. These container manifests are used to keep track of the installed packages in the distroless image.

> \*** This is a required argument when using `dockerfile-extend-image`.

> \**** This is an experimental feature that allows for holding back certain packages from getting installed. This argument can be used to forcibly avoid installing dependencies (that would normally get installed as part of package installation) that are not needed in a distroless image enviroment.