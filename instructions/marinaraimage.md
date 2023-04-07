# Marinara Docker Image

## Build Marinara image
### Use the following docker commands to generate **marinara** docker images locally

|Marinara Image|Docker Command|
|-|-|
| **marinara:1.0** | `docker build . -t marinara:1.0 -f dockerfile-marinara --build-arg MARINER_VERSION=1.0 --no-cache` |
| **marinara:2.0** | `docker build . -t marinara:2.0 -f dockerfile-marinara --build-arg MARINER_VERSION=2.0 --no-cache` |
