"use client"

import { useEffect, useRef } from 'react'
import "../../dist/three-cad-viewer/three-cad-viewer.css"
import { Viewer } from "../../dist/three-cad-viewer/three-cad-viewer.esm.js"

function nc(change) {}

export interface CadViewerProps {
    cadShapes: any
}


export default function CadViewer({ cadShapes }: CadViewerProps) {
    const ref = useRef(null)
    const { innerWidth: width, innerHeight: height } = window

    const viewerOptions = {
        theme: "light",
        ortho: true,
        control: "trackball", // "orbit",
        normalLen: 0,
        cadWidth: width,
        height: height * 0.85,
        ticks: 10,
        ambientIntensity: 0.9,
        directIntensity: 0.12,
        transparent: false,
        blackEdges: false,
        axes: true,
        grid: [false, false, false],
        timeit: false,
        rotateSpeed: 1,
        tools: false,
        glass: false
    }

    const renderOptions = {
        ambientIntensity: 1.0,
        directIntensity: 1.1,
        metalness: 0.30,
        roughness: 0.65,
        edgeColor: 0x707070,
        defaultOpacity: 0.5,
        normalLen: 0,
        up: "Z"
    }


    useEffect(() => {
        const container = ref.current //document.getElementById("cad_view")

        // 2) Create the CAD display in this container
        // const display = new Display(container, options)

        // 3) Create the CAD viewer

        // var shapesStates = viewer.renderTessellatedShapes(shapes, states, options)
        if (cadShapes && cadShapes.length > 0) {
            const viewer = new Viewer(container, viewerOptions, nc)

            render("input", ...cadShapes)
            function render(name: string, shapes, states) {
                viewer?.clear()
                const [unselected, selected] = viewer.renderTessellatedShapes(shapes, states, renderOptions)
                console.log(unselected)
                console.log(selected)

                viewer.render(
                    unselected,
                    selected,
                    states,
                    renderOptions,
                )
            }
        }


    }, [cadShapes])

    return (
        <div ref={ref}></div>
    )
}