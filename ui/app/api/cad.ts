import axios from "axios"



export function getCadShapes(query: string, uuid: string | null = null) {
  let config = {
    method: 'get',
    maxBodyLength: Infinity,
    "Content-Type": "application/json",
    url: 'http://127.0.0.1:5001/cad',
    headers: {},
    params: {
      query,
      uuid,
    },

  }

  return axios.request(config)
    .then(async (response) => {
      console.log(response)
      return response
    })
    .catch((error) => {
      console.log(error)
    })
}


