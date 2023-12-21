import importlib
import os
from flask import Flask, request
import json
import cadquery as cq
import numpy as np
from codex import generate_cq_obj
from utils.json import NumpyEncoder
from utils.tessellate import tessellate
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask import request

from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@cross_origin()
@app.route("/cad", methods=["GET"])
def cad():
    query = request.args.get("query")
    obj = generate_cq_obj(query)
    try:
        converted_obj = tessellate([obj])
        return jsonify(json.loads(json.dumps(converted_obj, cls=NumpyEncoder)))
    except Exception as e:
        print(e)
        return jsonify({"error": f"Something went wrong.{e}"})
    

if __name__ == "__main__":
    app.run(debug=True, port=5001)
