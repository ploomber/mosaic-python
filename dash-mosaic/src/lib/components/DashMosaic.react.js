import React, { useEffect, useRef, useState } from 'react';
import PropTypes from 'prop-types';
import * as vg from "@uwdata/vgplot";
import { parseSpec, astToDOM } from "@uwdata/mosaic-spec";

const DashMosaic = (props) => {
    const { id, spec, uri } = props;
    const chartRef = useRef(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        if (chartRef.current) {
            const renderChart = async () => {
                setIsLoading(true);
                let connector;
                if (!uri) {
                    connector = vg.wasmConnector();
                } else if (uri.startsWith('ws')) {
                    connector = vg.socketConnector(uri);
                } else if (uri.startsWith('http')) {
                    connector = vg.restConnector(uri);
                } else {
                    throw new Error('Invalid URI format. Must start with "ws" or "http".');
                }

                await vg.coordinator().databaseConnector(connector);

                const parsedSpec = parseSpec(spec);
                const {
                    element, // root DOM element of the application
                    params   // Map of all named Params and Selections
                } = await astToDOM(parsedSpec);

                chartRef.current.innerHTML = '';
                chartRef.current.appendChild(element);
                setIsLoading(false);
            };

            renderChart();

            return () => {
                chartRef.current.innerHTML = '';
            };
        }
    }, [spec, uri]);

    return (
        <div id={id}>
            {isLoading ? (
                <div className="loading-message">
                    <p>Loading<span className="loading-dots">
                        <span>.</span><span>.</span><span>.</span>
                    </span></p>
                </div>
            ) : null}
            <div ref={chartRef} style={{ display: isLoading ? 'none' : 'block' }}></div>
            <style jsx>{`
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
};

DashMosaic.defaultProps = {
    spec: {},
    uri: ''
};

DashMosaic.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The spec object to be visualized.
     */
    spec: PropTypes.object,

    /**
     * The URI for the database connector. If empty, uses wasmConnector.
     * If starts with 'ws', uses socketConnector. If starts with 'http', uses restConnector.
     */
    uri: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default DashMosaic;
