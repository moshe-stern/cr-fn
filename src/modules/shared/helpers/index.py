from celery_app import celery


def divide_list(lst, n):
    """
    Divide a list into n approximately equal parts.

    Args:
        lst (list): The list to be divided.
        n (int): Number of parts to divide the list into.

    Returns:
        list: A list of n sublists, each containing a portion of the input list.
    """
    avg = len(lst) // n
    remainder = len(lst) % n
    parts = []
    start = 0
    for i in range(n):
        end = start + avg + (1 if i < remainder else 0)
        parts.append(lst[start:end])
        start = end
    return parts


class AuthorizationSettingsNotFound(Exception):
    pass


class NoAppointmentsFound(Exception):
    pass


def update_task_progress(task_id, progress, child_id):
    parent_meta = celery.backend.get_task_meta(task_id)
    existing = parent_meta.get("result") or {}
    existing[f"child_progress_{child_id}"] = progress
    celery.backend.store_result(task_id, existing, "PENDING")
