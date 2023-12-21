import importlib
import os
import cadquery as cq


def get_donwload_string(id: str, extension: str = "step"):
    # Export the box
    cad_file_path = f"generated/{id}.{extension}"
    if not os.path.exists(cad_file_path):
        spec = importlib.util.spec_from_file_location(
            "obj_module", f"generated/{id}.py"
        )
        obj_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(obj_module)

        cq.exporters.export(obj_module.obj, cad_file_path)
    return cad_file_path
