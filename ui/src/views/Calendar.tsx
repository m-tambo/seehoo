import { Route } from "react-router"

const C = () => (
  <div>
    hello feed
  </div>
)

const Calendar = <Route path="/calendar" element={<C />} />

export default Calendar
