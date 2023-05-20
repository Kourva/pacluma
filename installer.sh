#!/bin/bash

# Function to check root access
check_root() {
    [[ $EUID -eq 0 ]]
}

# Check if pacluma is already installed
check_installed() {
    [[ -f "/usr/bin/pacluma" ]]
}

# Installing process
installer() {
    if check_installed; then
        # If package is already installed, print message and exit
        echo -e "\ninfo: pacluma is already installed."
        exit 0
    fi

    # Print install message
    echo -e "\ninfo: installing package for you."

    # Copy file to /usr/bin
    if ! cp pacluma.py /usr/bin/pacluma; then
        echo "error: failed to copy file to /usr/bin"
        exit 1
    fi

    # Change permissions
    if ! chmod 755 /usr/bin/pacluma; then
        echo "error: failed to set executable permission for /usr/bin/pacluma"
        exit 1
    fi

    # Print success message
    echo "success: pacluma has been installed."
}

# Uninstalling process
uninstaller() {
    # Print uninstall message
    echo -e "\ninfo: uninstalling package from your system."

    # Remove file from /usr/bin
    if check_installed; then
        if ! rm /usr/bin/pacluma; then
            echo "error: failed to remove /usr/bin/pacluma"
            exit 1
        fi

        # Print success message
        echo "success: pacluma has been uninstalled."
    else
        # If package is not installed, print message and exit
        echo "info: pacluma is not installed."
        exit 0
    fi
}

if check_root; then
    if [[ $# -gt 0 && "$1" == "--uninstall" ]]; then
        uninstaller
    else
        installer
    fi
else
    echo "error: you cannot perform this operation unless you are root."
    exit 1
fi
