#!/bin/bash

set -e

# Variables
PACKAGE_NAME="py_binance"
PACKAGE_URL="http://127.0.0.1:5500/py_binance.zip" # Replace with the actual URL
DOWNLOAD_DIR="/tmp/${PACKAGE_NAME}_download"
PACKAGE_ZIP_PATH="${DOWNLOAD_DIR}/${PACKAGE_NAME}.zip"
PYTHON_SITE_PACKAGES=$(python3 -c "import site; print(site.getsitepackages()[0])")
DESTINATION="${PYTHON_SITE_PACKAGES}/${PACKAGE_NAME}"

# Functions
function download_package() {
    echo "Downloading ${PACKAGE_NAME}..."
    mkdir -p "${DOWNLOAD_DIR}"
    curl -o "${PACKAGE_ZIP_PATH}" -L "${PACKAGE_URL}"
    echo "Downloaded ${PACKAGE_NAME} to ${PACKAGE_ZIP_PATH}"
}

function extract_package() {
    echo "Extracting ${PACKAGE_NAME}..."
    unzip -q "${PACKAGE_ZIP_PATH}" -d "${DOWNLOAD_DIR}"
    echo "Extracted to ${DOWNLOAD_DIR}/${PACKAGE_NAME}"
}

function install_package() {
    echo "Installing ${PACKAGE_NAME} to site-packages..."
    if [ -d "${DESTINATION}" ]; then
        echo "Removing existing ${PACKAGE_NAME} from site-packages..."
        rm -rf "${DESTINATION}"
    fi
    cp -r "${DOWNLOAD_DIR}/${PACKAGE_NAME}" "${DESTINATION}"
    echo "Installed ${PACKAGE_NAME} to ${DESTINATION}"
}

function clean_up() {
    echo "Cleaning up temporary files..."
    rm -rf "${DOWNLOAD_DIR}"
    echo "Clean up complete."
}

# Confirmation Prompt
function confirm_installation() {
    echo "The package will be installed in the following directory:"
    echo "${DESTINATION}"
    echo ""
    read -p "Do you want to proceed with this installation? (y/n): " confirm
    if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
        echo "Installation aborted."
        echo "Suggestion: Enable a virtual environment and rerun this script for isolated installation."
        echo "To enable a virtual environment, use the following commands:"
        echo ""
        echo "    python3 -m venv myenv"
        echo "    source myenv/bin/activate"
        echo ""
        echo "Then rerun this script in the virtual environment."
        exit 1
    fi
}

# Main Execution
confirm_installation
download_package
extract_package
install_package
clean_up

echo "Installation of ${PACKAGE_NAME} complete!"
