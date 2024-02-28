#!/usr/bin/python3
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import argparse
import glob
import marinaracommon
import os
import shutil

class BuildData:
    def __init__(self,
               imageType,
               azureLinuxVersion,
               location,
               packagesToAdd,
               packagesToHoldback,
               addNonroot,
               user,
               userUid,
               userGid,
               manifestsDirectory):
        self.imageType = imageType
        self.azureLinuxVersion = azureLinuxVersion
        self.location = location
        self.packagesToAdd = packagesToAdd
        self.packagesToHoldback = packagesToHoldback
        self.addNonroot = addNonroot
        self.user = user
        self.userUid = userUid
        self.userGid = userGid
        self.manifestsDirectory = manifestsDirectory

    def __repr__(self):
        return str(self.__dict__)

imageTypes = ["minimal", "minimal-nonroot", "minimal-debug", 
              "minimal-debug-nonroot", "base", "base-nonroot", 
              "base-debug", "base-debug-nonroot", "custom", 
              "custom-nonroot", "custom-debug", "custom-debug-nonroot"]
minimalPackages = "distroless-packages-minimal"
basePackages = "distroless-packages-base"
debugPackages = "busybox"
manifestsSubDirectory = "/var/lib/rpmmanifest"

def readArgs():
    parser = argparse.ArgumentParser(
        description="Build an Azure Linux Distroless Image from Scratch.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--image-type", required=True, type=str, help="Image type to create.",
    )
    parser.add_argument(
        "--azure-linux-version", required=True, type=str, help="Azure Linux version (2.0, 3.0).",
    )
    parser.add_argument(
        "--location", required=True, type=str, help="Directory location to install the packages in.",
    )
    parser.add_argument(
        "--add-packages", type=str, help="Packages to install.",
    )
    parser.add_argument(
        "--packages-to-holdback", type=str, help="Packages to holdback from getting installed.",
    )
    parser.add_argument(
        "--user", type=str, help="User to add as nonroot.",
    )
    parser.add_argument(
        "--user-uid", type=int, help="User's UID.",
    )
    parser.add_argument(
        "--user-gid", type=int, help="User's GID.",
    )

    return parser.parse_args()

def validateArgs(args):
    # Validate image type
    if args.image_type not in imageTypes:
        raise ValueError("Invalid value \"%s\" passed for argument %s." % (args.image_type, "--image-type"))

    # Validate packages
    if "custom" in args.image_type and not args.add_packages.strip():
        raise ValueError("Invalid value \"%s\" passed for argument %s." % (args.add_packages, "--add-packages"))

    # Validate Azure Linux version
    if args.azure_linux_version != "1.0" and args.azure_linux_version != "2.0":
        raise ValueError("Invalid value \"%s\" passed for argument %s." % (args.azure_linux_version, "--azure-linux-version"))

    # Validate nonroot user
    if "nonroot" in args.image_type:
        if args.user == "root":
            raise ValueError("User name cannot be root.")
        if not args.user.strip():
            raise ValueError("User name cannot be empty.")
        if args.user_uid == 0:
            raise ValueError("User UID cannot be 0")
        if args.user_gid == 0:
            raise ValueError("User GID cannot be 0")

def prepareBuild(args):
    addNonrootUser = False
    if "nonroot" in args.image_type:
        addNonrootUser = True

    addPackages = args.add_packages.split()

    if "minimal" in args.image_type:
        addPackages.append(minimalPackages)
    elif "base" in args.image_type:
        addPackages.append(basePackages)

    if "debug" in args.image_type:
        addPackages.append(debugPackages)

    packagesToHoldback = args.packages_to_holdback.split()

    manifestsDirectory = args.location + manifestsSubDirectory
    os.makedirs(manifestsDirectory)

    return BuildData(
        args.image_type,
        args.azure_linux_version,
        args.location,
        addPackages,
        packagesToHoldback,
        addNonrootUser,
        args.user,
        args.user_uid,
        args.user_gid,
        manifestsDirectory
    )

def buildImage(buildData):
    marinaracommon.installAzureLinuxPackages(
        buildData.azureLinuxVersion,
        buildData.location,
        buildData.packagesToAdd,
        buildData.packagesToHoldback
    )

    marinaracommon.createContainerManifestFiles(buildData.location, buildData.manifestsDirectory)

    files = glob.glob('*.txt', recursive=False)

    # iterating over all the .txt files in the root directory of marinara image
    for file in files:
        shutil.copy2(os.path.join("/", file), buildData.location)

    if buildData.addNonroot:
        marinaracommon.addNonrootUser(buildData.user, buildData.userUid, buildData.userGid, buildData.location)

    marinaracommon.cleanup(buildData.location)

args = readArgs()
validateArgs(args)
buildData = prepareBuild(args)
print(buildData)
buildImage(buildData)
