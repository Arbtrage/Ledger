"""Rich progress displays for backup pipeline stages."""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager

from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskID,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

from ui.console import get_console


class BackupProgress:
    """Multi-stage progress: dump → compress → upload → verify."""

    def __init__(self) -> None:
        self._progress = Progress(
            SpinnerColumn(),
            TextColumn("[bold]{task.description}"),
            BarColumn(bar_width=40),
            TaskProgressColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
            MofNCompleteColumn(),
            console=get_console(),
            transient=False,
        )

    @contextmanager
    def stage(self, description: str) -> Iterator[TaskID]:
        """Context manager yielding a Rich task ID for a pipeline stage."""
        with self._progress:
            task_id = self._progress.add_task(description, total=100)
            yield task_id

    def update(self, task_id: TaskID, *, completed: float, description: str | None = None) -> None:
        """Update progress for a task (scaffold — wire to orchestrator later)."""
        self._progress.update(task_id, completed=completed, description=description or "")
