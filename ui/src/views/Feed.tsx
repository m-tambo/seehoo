import { Route } from "react-router"

const F = () => (
  <div>
    hello feed
  </div>
)

const Feed = <Route path="/" element={<F />} />

export default Feed
