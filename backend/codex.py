import importlib
import os
import openai
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ["OPENAI"]


def generate_cq_obj(user_msg: str):
    # Define the system message
    system_msg = """
    You are a strict assistant, translating natural language to Python CadQuery code. 
    Please do not explain, just write code. VERY IMPORTANT to name the output variable obj and do not use show_object or any show functions.
    Here is the Cadquery API as a helpful resource:
 
    cq.Workplane.center(x, y)- Shift local coordinates to the specified location.
    cq.Workplane.lineTo(x, y[, forConstruction])- Make a line from the current point to the provided point
    cq.Workplane.line(xDist, yDist[, forConstruction])- Make a line from the current point to the provided point, using dimensions relative to the current point
    cq.Workplane.vLine(distance[, forConstruction])- Make a vertical line from the current point the provided distance
    cq.Workplane.vLineTo(yCoord[, forConstruction])- Make a vertical line from the current point to the provided y coordinate.
    cq.Workplane.hLine(distance[, forConstruction])- Make a horizontal line from the current point the provided distance
    cq.Workplane.hLineTo(xCoord[, forConstruction])- Make a horizontal line from the current point to the provided x coordinate.
    cq.Workplane.polarLine(distance, angle[, ...])- Make a line of the given length, at the given angle from the current point
    cq.Workplane.polarLineTo(distance, angle[, ...])- Make a line from the current point to the given polar coordinates
    cq.Workplane.moveTo([x, y])- Move to the specified point, without drawing.
    cq.Workplane.move([xDist, yDist])- Move the specified distance from the current point, without drawing.
    cq.Workplane.spline(listOfXYTuple[, tangents, ...])- Create a spline interpolated through the provided points (2D or 3D).
    cq.Workplane.parametricCurve(func[, N, start, ...])- Create a spline curve approximating the provided function.
    cq.Workplane.parametricSurface(func[, N, ...])- Create a spline surface approximating the provided function.
    cq.Workplane.threePointArc(point1, point2[, ...])- Draw an arc from the current point, through point1, and ending at point2
    cq.Workplane.sagittaArc(endPoint, sag[, ...])- Draw an arc from the current point to endPoint with an arc defined by the sag (sagitta).
    cq.Workplane.radiusArc(endPoint, radius[, ...])- Draw an arc from the current point to endPoint with an arc defined by the radius.
    cq.Workplane.tangentArcPoint(endpoint[, ...])- Draw an arc as a tangent from the end of the current edge to endpoint.
    cq.Workplane.mirrorY()- Mirror entities around the y axis of the workplane plane.
    cq.Workplane.mirrorX()- Mirror entities around the x axis of the workplane plane.
    cq.Workplane.wire([forConstruction])- Returns a CQ object with all pending edges connected into a wire.
    cq.Workplane.rect(xLen, yLen[, centered, ...])- Make a rectangle for each item on the stack.
    cq.Workplane.circle(radius[, forConstruction])- Make a circle for each item on the stack.
    cq.Workplane.ellipse(x_radius, y_radius[, ...])- Make an ellipse for each item on the stack.
    cq.Workplane.ellipseArc(x_radius, y_radius[, ...])- Draw an elliptical arc with x and y radiuses either with start point at current point or or current point being the center of the arc
    cq.Workplane.polyline(listOfXYTuple[, ...])- Create a polyline from a list of points
    cq.Workplane.close()- End construction, and attempt to build a closed wire.
    cq.Workplane.rarray(xSpacing, ySpacing, xCount, ...)- Creates an array of points and pushes them onto the stack.
    cq.Workplane.polarArray(radius, startAngle, ...)- Creates a polar array of points and pushes them onto the stack.
    cq.Workplane.slot2D(length, diameter[, angle])- Creates a rounded slot for each point on the stack.
    cq.Workplane.offset2D(d[, kind, forConstruction])- Creates a 2D offset wire.
    cq.Workplane.placeSketch(*sketches)- Place the provided sketch(es) based on the current items on the stack.
    cq.Workplane.gear(gear: BevelGear|CrossedHelicalGear|RackGear|RingGear|Worm)- Create a gear from the provided gear class.
    
    Here are also some gear classes from the library, use this as input to cq.Workplane.gear

    import cq_gears

    cq_gears.BevelGear(module, teeth_number, cone_angle, face_width, pressure_angle=20.0, helix_angle=0.0, clearance=0.0, backlash=0.0, bore_d)
    cq_gears.CrossedHelicalGear(module, teeth_number, width, pressure_angle=20.0, helix_angle=0.0, clearance=0.0, backlash=0.0, bore_d)
    cq_gears.RackGear(module, length, width, height, pressure_angle=20.0, helix_angle=0.0, clearance=0.0, backlash=0.0, bore_d)
    cq_gears.RingGear(module, teeth_number, width, rim_width, pressure_angle=20.0, helix_angle=0.0, clearance=0.0, backlash=0.0, bore_d)
    cq_gears.Worm(module, lead_angle, n_threads, length, pressure_angle=20.0, clearance=0.0, backlash=0.0, bore_d)
    cq_gears.SpurGear(self, module, teeth_number, width, pressure_angle=20.0, helix_angle=0.0, clearance=0.0, backlash=0.0, bore_d)
    
    Here is a way to generate airfoils with the coordinates being fed into cq.Workplane.polyline followed by a cq.Workplane.polyline.close

    For NACA airfoils use get_coords() for the following classes

    You MUST: import parafoil

    parafoil.CamberThicknessAirfoil(inlet_angle, outlet_angle, chord_length, angle_units="rad"|"deg")
    parafoil.NACAAirfoil(naca_string, chord_length)
    

    """

    # Create a dataset using GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
    )

    id = datetime.now().isoformat()

    # create directory "generated" if does not exist
    if not os.path.exists("generated"):
        os.makedirs("generated")

    file_name = f"generated/{id}.py"
    with open(file_name, "w") as f:
        f.write(
            f'import cadquery as cq\n{response["choices"][0]["message"]["content"]}'
        )

    spec = importlib.util.spec_from_file_location("obj_module", file_name)
    obj_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj_module)
    return id, obj_module.obj
