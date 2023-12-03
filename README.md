![header](imgs/header.jpg)


# AlphaFold for RunPod

This repository is a fork of the official [AlphaFold repository](https://github.com/deepmind/alphafold), specifically modified to run seamlessly within the RunPod environment. This fork extends its usability by ensuring compatibility and optimized performance on RunPod's infrastructure.

## Modifications

The key modifications in this fork include:

- **Environment Configuration:** Adjustments to the docker image to work with RunPod. This includes the possibility to download the data on the platform and mount it afterwards. 
- **Dependency Management:** Updates to dependencies ensuring they are compatible with the RunPod platform.


## Getting Started

To use this modified version of AlphaFold in RunPod, follow these steps:

1. **Set Up RunPod Environment:** Ensure that your RunPod environment is properly configured for running containerized applications. Initialize the Runpod container with this repositorys Docker image. 

2. Clone this repository and `cd` into it.

    ```bash
    git clone https://github.com/deepmind/alphafold.git
    cd ./alphafold
    ```

3. Download genetic databases and model parameters:

    *   Install `aria2c`. On most Linux distributions it is available via the
    package manager as the `aria2` package (on Debian-based distributions this
    can be installed by running `sudo apt install aria2`).

    *   Please use the script `scripts/download_all_data.sh` to download
    and set up full databases. This may take substantial time (download size is
    556 GB), so we recommend running this script in the background:

    ```bash
    scripts/download_all_data.sh <DOWNLOAD_DIR> > download.log 2> download_all.log &
    ```

    *   **Note: The download directory `<DOWNLOAD_DIR>` should *not* be a
    subdirectory in the AlphaFold repository directory.** If it is, the Docker
    build will be slow as the large databases will be copied into the docker
    build context.
