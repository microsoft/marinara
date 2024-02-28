# Marinara Docker Image

## Build Marinara image locally
### Use the following docker commands to generate **marinara** docker images locally

|Marinara Image|Docker Command|
|-|-|
| **marinara:2.0** | `docker build . -t marinara:2.0 -f dockerfile-marinara --build-arg AZL_VERSION=2.0 --no-cache` |
| **marinara:3.0** | `docker build . -t marinara:3.0 -f dockerfile-marinara --build-arg AZL_VERSION=3.0 --no-cache` |