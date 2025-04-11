import { Route } from "react-router"

const M = () => (
  <div>
    hello map
  </div>
)

const Map = <Route path="/map" element={<M />} />

export default Map
