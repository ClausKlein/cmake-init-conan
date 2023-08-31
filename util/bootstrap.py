"""Bootstrap relevant functions.

This file bootstrap the system in order to make it usable for development.
This file is deprecated and will be removed if a container with all artifacts
preinstalled is provided.
"""

import logging
import subprocess
from pathlib import Path

log = logging.getLogger(__name__)

root = Path(__file__).parent.parent

LINUX_PACKAGES = [
    "python3-pip",
    "doxygen",
    "graphviz",
    "ninja-build",
    "cmake",
    "clang",
    "clang-tidy",
    "clang-format",
    "gcovr",
    "unzip",  # unzip of sonar-scanner
    "gdb",
    "iwyu",
    "clang-13",  # iwyu compatible version
    "ccache",  # enabled cache feature in project_options
]


def install_linux_packages():
    """Install Linux packages."""
    log.info("Install linux packages")
    # Workaround for hanging installation of tzdata
    # Ignore errors here
    cmd = "sudo ln -s /usr/share/zoneinfo/Europe/Berlin /etc/localtime"
    subprocess.run(cmd, shell=True)
    result = subprocess.run("sudo apt update", shell=True)
    if result.returncode != 0:
        raise Exception("apt update failed.")
    packages = " ".join(LINUX_PACKAGES)
    log.info(f"Install '{packages}'")
    cmd = f"sudo apt install {packages} --assume-yes"
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        raise Exception(f"Install of '{packages}' failed.")


def install_python_packages():
    """Install Python packages."""
    log.info("Install python packages")
    cmd = (
        "python3 -m pip install --user --upgrade "
        "-i http://pypi.rsint.net/api/pypi/rs_pypi_virtual/simple "
        f"--trusted-host pypi.rsint.net -r {root}/requirements.txt"
    )
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        raise Exception(f"Install of python packages failed.")


if __name__ == "__main__":
    install_linux_packages()
    install_python_packages()
