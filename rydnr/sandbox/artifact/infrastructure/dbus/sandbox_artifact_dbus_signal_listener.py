"""
rydnr/sandbox/artifact/infrastructure/dbus/sandbox_artifact_dbus_signal_listener.py

This file defines the SandboxArtifactDbusSignalListener class.

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
from dbus_next import BusType, Message
from pythoneda.event import Event
from pythoneda.shared.artifact_changes.events import (
    ArtifactChangesCommitted,
    ArtifactCommitPushed,
    ArtifactCommitTagged,
    ArtifactTagPushed,
    CommittedChangesPushed,
    CommittedChangesTagged,
    StagedChangesCommitted,
    TagPushed,
)
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import (
    DbusArtifactChangesCommitted,
    DbusArtifactCommitPushed,
    DbusArtifactCommitTagged,
    DbusArtifactTagPushed,
    DbusCommittedChangesPushed,
    DbusCommittedChangesTagged,
    DbusStagedChangesCommitted,
    DbusTagPushed,
)
from pythoneda.infrastructure.dbus import DbusSignalListener
from typing import Dict


class SandboxArtifactDbusSignalListener(DbusSignalListener):

    """
    A Port that listens to Sandbox-artifact-relevant d-bus signals.

    Class name: SandboxArtifactDbusSignalListener

    Responsibilities:
        - Connect to d-bus.
        - Listen to signals relevant to Sandbox-artifact.

    Collaborators:
        - pythoneda.application.pythoneda.PythonEDA: Receives relevant domain events.
        - pythoneda.shared.artifact_changes.events.infrastructure.dbus.*
    """

    def __init__(self):
        """
        Creates a new SandboxArtifactDbusSignalListener instance.
        """
        super().__init__()

    def signal_receivers(self, app) -> Dict:
        """
        Retrieves the configured signal receivers.
        :param app: The PythonEDA instance.
        :type app: pythoneda.application.PythonEDA
        :return: A dictionary with the signal name as key, and the tuple interface and bus type as the value.
        :rtype: Dict
        """
        result = {}
        key = self.__class__.full_class_name(ArtifactChangesCommitted)
        result[key] = [DbusArtifactChangesCommitted, BusType.SYSTEM]
        key = self.__class__.full_class_name(ArtifactCommitPushed)
        result[key] = [DbusArtifactCommitPushed, BusType.SYSTEM]
        key = self.__class__.full_class_name(ArtifactCommitTagged)
        result[key] = [DbusArtifactCommitTagged, BusType.SYSTEM]
        key = self.__class__.full_class_name(ArtifactTagPushed)
        result[key] = [DbusArtifactTagPushed, BusType.SYSTEM]

        key = self.__class__.full_class_name(CommittedChangesPushed)
        result[key] = [DbusCommittedChangesPushed, BusType.SYSTEM]
        key = self.__class__.full_class_name(CommittedChangesTagged)
        result[key] = [DbusCommittedChangesTagged, BusType.SYSTEM]
        key = self.__class__.full_class_name(StagedChangesCommitted)
        result[key] = [DbusStagedChangesCommitted, BusType.SYSTEM]
        key = self.__class__.full_class_name(TagPushed)
        result[key] = [DbusTagPushed, BusType.SYSTEM]
        return result
