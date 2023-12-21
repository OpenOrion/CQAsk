"use client"


import { Alert, Layout, Space, theme } from 'antd'
import Search from 'antd/es/input/Search'
import { useState } from 'react'
import { getCadShapes } from './api/cad'
import CadViewer from './components/cad-viewer'

const { Content, } = Layout


export default function Home() {
  const {
    token: { colorBgContainer },
  } = theme.useToken()

  const [cadShapes, setCadShapes] = useState([])
  const [isError, setIsError] = useState(false)
  // const [UUID, setUUID] = useState<string>()

  const onSearch = async (value: string) => {
    try {
      const shapes = await getCadShapes(value)
      // setUUID(shapes.data.uuid)
      setCadShapes(shapes.data)
      setIsError(false)
    } catch {
      console.log("error")
      setIsError(true)

    }

  }

  return (
    <Layout style={{ height: "100vh" }}>

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

