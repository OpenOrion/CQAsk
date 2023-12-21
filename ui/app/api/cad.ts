import axios from "axios"
import { downloadAxiosResponse } from "../utils"

const BASE_URL = "http://127.0.0.1:5001"

export function getCadShapes(query: string, uuid: string | null = null) {
  let config = {
    method: 'get',
    maxBodyLength: Infinity,
    "Content-Type": "application/json",
    url: `${BASE_URL}/cad`,
    headers: {},
    params: {
      query,
      uuid,
    },

  }

  return axios.request(config)
    .then(async (response) => {
      return response.data
    })
    .catch((error) => {
      console.log(error)
    })
}


export function getCadDownload(id: string, file_type: "step" | "stl") {
  let config = {
    method: 'get',
    maxBodyLength: Infinity,
    responseType: 'arraybuffer',
    "Content-Type": "application/json",
    url: `${BASE_URL}/download`,
    headers: {},
    params: {
      id,
      file_type,
    },

  }

  return axios.request(config)
    .then(async (response) => {
      console.log(response)
      downloadAxiosResponse(`${id}.${file_type}`, response)
    })
    .catch((error) => {
      console.log(error)
    })
}


