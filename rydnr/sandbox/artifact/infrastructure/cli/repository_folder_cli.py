"""
rydnr/sandbox/artifact/infrastructure/cli/repository_folder_cli.py

This file defines the RepositoryFolderCli.

Copyright (C) 2023-today rydnr's rydnr/sandbox-artifact-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse
from pythoneda import BaseObject, PrimaryPort


class RepositoryFolderCli(BaseObject, PrimaryPort):

    """
    A PrimaryPort used to gather the repository folder information.

    Class name: RepositoryFolderCli

    Responsibilities:
        - Parse the command-line to retrieve the information about the repository folder.

    Collaborators:
        - PythonEDA subclasses: They are notified back with the information retrieved from the command line.
    """

    @classmethod
    @property
    def is_one_shot_compatible(cls) -> bool:
        """
        Retrieves whether this primary port should be instantiated when
        "one-shot" behavior is active.
        It should return False unless the port listens to future messages
        from outside.
        :return: True in such case.
        :rtype: bool
        """
        return True

    async def accept(self, app):
        """
        Processes the command specified from the command line.
        :param app: The PythonEDA instance.
        :type app: PythonEDA
        """
        parser = argparse.ArgumentParser(
            description="Provide the repository folder of the artifact"
        )

        parser.add_argument(
            "-r", "--repository-folder", required=True, help="The repository folder"
        )

        args, unknown_args = parser.parse_known_args()

        app.accept_repository_folder(args.repository_folder)
