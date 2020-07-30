"""
Liest alle Dateien aus dem static Unterverzeichnis aus und gibt sie als Liste wieder
"""

import os


def get_files(relative_path):
    folder = os.path.join('static/', relative_path)
    files = [f for f in os.listdir(
        folder) if os.path.isfile(os.path.join(folder, f))]
    return files
