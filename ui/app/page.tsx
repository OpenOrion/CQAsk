"use client"


import { Alert, Layout, Select, Space, theme } from 'antd'
import Search from 'antd/es/input/Search'
import { useState } from 'react'
import { getCadDownload as downloadCadFile, getCadShapes as getCadObject } from './api/cad'
import CadViewer from './components/cad-viewer'
const { Content, } = Layout



export default function Home() {
  const {
    token: { colorBgContainer },
  } = theme.useToken()

  const [cadShapes, setCadShapes] = useState([])
  const [isError, setIsError] = useState(false)
  const [cadID, setCadID] = useState<string>("2023-12-21T00:45:37.267438")

  // const [UUID, setUUID] = useState<string>()

  const onSearch = async (value: string) => {
    try {
      const cadObject = await getCadObject(value)
      // setUUID(shapes.data.uuid)
      setCadShapes(cadObject.shapes)
      setCadID(cadObject.id)
      setIsError(false)
    } catch {
      console.log("error")
      setIsError(true)

    }
  }

  const onDownload = async (file_type: "stl" | "step") => {
    console.log(cadID, file_type)
    if (cadID) {
      await downloadCadFile(cadID, file_type)
    }
  }

  return (
    <Layout style={{ height: "100vh" }}>
      <Space wrap>
        <Select
          placeholder='Download'
          value={"Download"}
          style={{ width: 120 }}
          onChange={onDownload}
          options={[
            { value: 'step', label: 'STEP' },
            { value: 'stl', label: 'STL' },

            { value: 'amf', label: 'AMF' },
            { value: '3mf', label: '3MF' },
            { value: 'vrml', label: 'VRML' },

          ]}
        />
      </Space >

      <Layout>
        <Layout style={{ padding: '0 24px 24px' }}>
          <Content
            style={{
              margin: 0,
              minHeight: 280,
            }}
          >
            <Layout>
              <CadViewer cadShapes={cadShapes} />

            </Layout>

          </Content>


          {
            isError ? (
              <Space direction="vertical" style={{ width: '100%' }}>

                <Alert
                  message="Error Generating"
                  description="Please try again. To debug check logs and 'generated' directory for latest file"
                  type="error"
                />
              </Space>
            ) : null
          }


          <Search placeholder="input search text" size="large" onSearch={onSearch} />


        </Layout>



      </Layout>
    </Layout >
  )
}

function Project() {
  throw new Error('Function not implemented.')
}

