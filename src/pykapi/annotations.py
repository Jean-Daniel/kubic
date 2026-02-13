import pathlib

import yaml


class AnnotationProvider:
    def __init__(self, dir_path: pathlib.Path):
        self.dir = dir_path
        self.cached = {}

    def __call__(self, group: str) -> dict:
        if group in self.cached:
            return self.cached[group]

        filename = group + ".yaml"

        # lookup in annotations dirs first
        annotations = None
        if self.dir:
            try:
                with self.dir.joinpath(filename).open("rb") as f:
                    annotations = yaml.load(f, yaml.CSafeLoader)
            except FileNotFoundError:
                pass

        if annotations is None:
            annotations = {}

        self.cached[group] = annotations
        return annotations
