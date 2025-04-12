import { Route } from "react-router"

const U = () => (
  <div>
    hello user
  </div>
)

const User = <Route path="/user" element={<U />} />

export default User
