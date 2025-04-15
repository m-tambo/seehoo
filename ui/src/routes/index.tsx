import { ReactElement } from 'react';
import { Routes as Router, Route } from 'react-router';
import App from 'components/App';
import * as routes from 'views'

const Routes = () => {
    const renderRoutes = () => Object.values(routes).reduce((ros, r) => {
        if (r.type === Route) ros.push(r)
        return ros
    }, [] as ReactElement[])

    return (
        <Router>
           <Route element={<App />}>
              {renderRoutes()}
           </Route> 
        </Router>
    )
}

export default Routes
