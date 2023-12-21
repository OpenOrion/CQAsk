from ocp_tessellate.convert import to_assembly
from ocp_tessellate import PartGroup
from ocp_tessellate.convert import (
    tessellate_group,
    to_assembly,
)

def tessellate(
    *cad_objs, names=None, colors=None, alphas=None, progress=None, **kwargs
):
    global FIRST_CALL

    part_group = to_assembly(
        *cad_objs,
        names=names,
        colors=colors,
        alphas=alphas,
        progress=progress,
    )

    if len(part_group.objects) == 1 and isinstance(
        part_group.objects[0], PartGroup
    ):
        part_group = part_group.objects[0]


    instances, shapes, states, _ = tessellate_group(part_group)

    return shapes, states
