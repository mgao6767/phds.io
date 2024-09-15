import pathlib

from flask import Flask, request, session, flash
from kerko.config_helpers import config_update


def load_flash_message(app: Flask, path_spec: str, url_path: str):

    msg = ""
    cwd_parents = [pathlib.Path.cwd(), *pathlib.Path.cwd().parents]
    instance_path = pathlib.Path(app.instance_path)
    instance_parents = [instance_path, *instance_path.parents]
    try_parents = cwd_parents + [p for p in instance_parents if p not in cwd_parents]
    for parent in try_parents:
        path = parent / path_spec.strip()
        if path.is_file():
            with open(path, "r", encoding="utf-8") as f:
                msg = f.read()
            config_update(app.config, {"flash_message": msg})
            break

    if msg:

        @app.before_request
        def intercept_request():
            # Check if the flash message has already been shown for this session
            if "flash_shown" not in session and request.path == url_path:
                flash(msg, "info")
                session["flash_shown"] = True
