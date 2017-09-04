import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import reducers from './js/reducers';
import Home from './js/components/Home';


// create store (where the app state (all the data) is stored)
const store = createStore(
    reducers,
)

const rootEl = document.getElementById('root')

const render = () => {
    ReactDOM.render(
        <Provider store={store}>
            <Home />
        </Provider>,
        rootEl
    )
}

render()
store.subscribe(render) // connects store to elements in render
