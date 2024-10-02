/* eslint no-magic-numbers: 0 */
import React, { useState } from 'react';

import { DashMosaic } from '../lib';

const App = () => {

    const [state, setState] = useState({value:'', label:'Type Here'});
    const setProps = (newProps) => {
            setState(newProps);
        };

    return (
        <div>
            <DashMosaic
                setProps={setProps}
                {...state}
            />
        </div>
    )
};


export default App;
