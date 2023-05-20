# Libraries
import os, sys, shutil


# Function to check root access
def check_root():
    return not os.geteuid()


# Check if pacluma is already installed
def check_installed():
    return os.path.exists("/usr/bin/pacluma")


# Installing process
def installer():
    if check_installed():
        # If package is already installed, print message and exit
        print("\ninfo: pacluma is already installed.")
        sys.exit(0)

    # Print install message
    print("\ninfo: installing package for you.")

    # Copy file to /usr/bin
    try:
        shutil.copyfile("pacluma.py", "/usr/bin/pacluma")
    except:
        print("error: failed to copy file to /usr/bin")
        sys.exit(1)

    # Change permissions
    try:
        os.chmod("/usr/bin/pacluma", 0o755)
    except:
        print("error: failed to set executable permission for /usr/bin/pacluma")
        sys.exit(1)

    # Print success message
    print("success: pacluma has been installed.")


# Uninstalling process
def uninstaller():
    # Print uninstall message
    print("\ninfo: uninstalling package from your system.")

    # Remove file from /usr/bin
    if check_installed():
        try:
            os.remove("/usr/bin/pacluma")
        except:
            print("error: failed to remove /usr/bin/pacluma")
            sys.exit(1)

        # Print success message
        print("success: pacluma has been uninstalled.")
    else:
        # If package is not installed, print message and exit
        print("info: pacluma is not installed.")
        sys.exit(0)


if __name__ == "__main__":
    if check_root():
        if len(sys.argv) > 1 and sys.argv[1] == "--uninstall":
            uninstaller()
        else:
            installer()
    else:
        raise sys.exit("error: you cannot perform this operation unless you are root.")
