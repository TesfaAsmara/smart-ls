import os
from pathlib import Path
import time

class DirectoryEntry:
    """
    A class to represent a directory entry (file or directory) with its name and access time.

    Attributes:
    name (str): The name of the directory entry.
    access_time (float): The last access time of the directory entry.
    """

    def __init__(self, name, access_time):
        """
        Initialize a DirectoryEntry instance.

        Parameters:
        name (str): The name of the directory entry.
        access_time (float): The last access time of the directory entry.
        """
        self.name = name
        self.access_time = access_time

    # special method for representing the objects in a class as a string
    def __repr__(self):
        """
        Represent a DirectoryEntry instance as a string.

        Returns:
        str: A string representation of the DirectoryEntry instance.
        """
        return f"{self.name}: Last accessed on {time.ctime(self.access_time)}"


def get_directory_entries(directory):
    """
    Retrieve entries (files and directories) in a specified directory,
    along with their last access times.

    Args:
        directory (Path-like object): The directory from which to retrieve entries.

    Returns:
        list[DirectoryEntry]: List of DirectoryEntry objects.
    """
    entries = []
    # scandir returns an iterator of os.DirEntry objects 
    # corresponding to the entries in the given directory. 
    with os.scandir(directory) as it:
        for entry in it:
            # regardless of whether it is a file or directory
            access_time = entry.stat().st_atime
            entries.append(DirectoryEntry(entry.name, access_time))
    return entries

def main():
    """
    Main function to execute the script. Lists files and directories in the
    current directory sorted by their last access time.
    """
    # get a path object representing the current directory
    current_dir = Path.cwd()
    entries = get_directory_entries(current_dir)
    # by default sorted returns the earliest first, so we must reverse it
    sorted_entries = sorted(entries, key=lambda e: e.access_time, reverse=True)

    for entry in sorted_entries:
        print(entry)

if __name__ == "__main__":
    main()

