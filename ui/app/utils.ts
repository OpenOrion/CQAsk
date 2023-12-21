import { AxiosResponse } from "axios"

export function downloadAxiosResponse(fileName: string, response: AxiosResponse) {
    // Create a Blob from the response data
    const blob = new Blob([response.data])

    // Create a link element to download the file
    const downloadLink = document.createElement('a')
    downloadLink.href = window.URL.createObjectURL(blob)
    downloadLink.download = fileName // Set the filename you want

    // Append the link to the DOM and trigger the download
    document.body.appendChild(downloadLink)
    downloadLink.click()

    // Clean up by removing the link from the DOM
    document.body.removeChild(downloadLink)
}

