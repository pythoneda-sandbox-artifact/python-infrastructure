"""
pythoneda/artifact/infrastructure/cli/__init__.py

This file ensures pythoneda.artifact.infrastructure.cli is a namespace.

Copyright (C) 2023-today rydnr's pythoneda-shared-pythoneda/domain-artifact-infrastructure

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
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from .artifact_changes_committed_cli_handler import ArtifactChangesCommittedCliHandler
from .artifact_commit_pushed_cli_handler import ArtifactCommitPushedCliHandler
from .artifact_commit_tagged_cli_handler import ArtifactCommitTaggedCliHandler
from .artifact_tag_pushed_cli_handler import ArtifactTagPushedCliHandler
from .committed_changes_pushed_cli_handler import CommittedChangesPushedCliHandler
from .committed_changes_tagged_cli_handler import CommittedChangesTaggedCliHandler
from .git_post_commit_hook_cli import GitPostCommitHookCli
from .staged_changes_committed_cli_handler import StagedChangesCommittedCliHandler
from .tag_pushed_cli_handler import TagPushedCliHandler
