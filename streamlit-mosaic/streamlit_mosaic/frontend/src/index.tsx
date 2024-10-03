import React from "react"
import ReactDOM from "react-dom"
import { StreamlitProvider } from "streamlit-component-lib-react-hooks"
import Mosaic from "./Mosaic"

ReactDOM.render(
  <React.StrictMode>
    <StreamlitProvider>
      <Mosaic />
    </StreamlitProvider>
  </React.StrictMode>,
  document.getElementById("root")
)
