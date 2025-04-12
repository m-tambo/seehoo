import { NavLink } from 'react-router'

const Nav = () => {
  const links = [
    { to: '/', children: <i>home</i> },
    { to: '/calendar', children: <i>calendar_today</i> },
    { to: '/map', children: <i>map</i> },
    { to: '/user', children: <i>person</i> },
  ]

  const renderLinks = () => links.map(l => (
    <NavLink 
      {...l} 
      className={({ isActive }) => isActive ? "active" : ""}
    />
  ))

  return (
    <nav>
      {renderLinks()}
    </nav>
  )
}

export default Nav
