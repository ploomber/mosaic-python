import { Streamlit } from "streamlit-component-lib"
import { useRenderData } from "streamlit-component-lib-react-hooks"
import React, { useState, useEffect, useRef } from "react"
import * as vg from "@uwdata/vgplot";
import { parseSpec, astToDOM, Spec } from "@uwdata/mosaic-spec";

// Create a global WASM connector
const globalWasmConnector = vg.wasmConnector();

function Mosaic() {
  const renderData = useRenderData()
  const spec: Spec = renderData.args["spec"]
  const uri: string = renderData.args["uri"]
  const height: number = renderData.args["height"]

  const chartRef = useRef<HTMLDivElement | null>(null);
  const [isLoading, setIsLoading] = useState(true);



  useEffect(() => {
    const renderChart = async () => {
      if (chartRef.current) {
        setIsLoading(true);

        let connector;

        if (!uri) {
          connector = globalWasmConnector;
        } else if (uri.startsWith('ws')) {
          connector = vg.socketConnector(uri);
        } else if (uri.startsWith('http')) {
          connector = vg.restConnector(uri);
        } else {
          throw new Error('Invalid URI format. Must start with "ws" or "http".');
        }

        await vg.coordinator().databaseConnector(connector)

        const parsedSpec = parseSpec(spec);
        const {
          element, // root DOM element of the application
          params   // Map of all named Params and Selections
        } = await astToDOM(parsedSpec);

        chartRef.current.innerHTML = '';
        chartRef.current.appendChild(element);
        setIsLoading(false);

        Streamlit.setFrameHeight(height);
      }
    };

    renderChart();

    return () => {
      if (chartRef.current) {
        chartRef.current.innerHTML = '';
      }
    };
  }, []);

  return (
    <div>
      {isLoading ? (
        <div className="loading-message" style={{ height: 50 }}>
          <p>Loading<span className="loading-dots">
            <span>.</span><span>.</span><span>.</span>
          </span></p>
        </div>
      ) : null}
      <div ref={chartRef} style={{ display: isLoading ? 'none' : 'block' }}></div>
      <style>{`
                @keyframes blink {
                    0% { opacity: .2; }
                    20% { opacity: 1; }
                    100% { opacity: .2; }
                }
                .loading-dots span {
                    animation-name: blink;
                    animation-duration: 1.4s;
                    animation-iteration-count: infinite;
                    animation-fill-mode: both;
                }
                .loading-dots span:nth-child(2) {
                    animation-delay: .2s;
                }
                .loading-dots span:nth-child(3) {
                    animation-delay: .4s;
                }
            `}</style>
    </div>
  );
}

export default Mosaic
