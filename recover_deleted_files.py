import os
import shutil
import argparse

def recover_deleted_files(drive_letter: str, destination: str) -> None:
    # Create the destination folder if it doesn't already exist
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Iterate over the files in the specified drive
    for root, _, files in os.walk(drive_letter):
        for file in files:
            # Check if the file has been deleted (i.e. it starts with "~$")
            if file.startswith("~$"):
                # Get the full path to the file
                file_path = os.path.join(root, file)

                # Attempt to recover the file by copying it to the destination folder
                try:
                    shutil.copy(file_path, destination)
                except shutil.Error as e:
                    print(f"Error recovering {file}: {e}")
                except IOError as e:
                    print(f"Error accessing {file}: {e}")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Recover deleted files from an NTFS drive")
    parser.add_argument("drive", help="The drive letter of the NTFS drive to scan (e.g. C:)")
    parser.add_argument("destination", help="The destination folder to save the recovered files")
    args = parser.parse_args()

    # Recover deleted files from the specified drive
    recover_deleted_files(args.drive, args.destination)
