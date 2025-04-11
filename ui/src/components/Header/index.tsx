import { Link, NavLink } from 'react-router'

import './Header.scss'

const Header = () => {
    const links = [
        { to: '/calendar', children: <i>calendar_today</i> },
        { to: '/map', children: <i>map</i> },
        { to: '/user', children: <i>person</i> },
    ]

    const renderLinks = () => links.map(l => (
        <NavLink {...l} className={({ isActive }) => isActive ? "active" : ""}/>
    ))

    return (
        <header>
            <Link to="/">
                <h1>seehoo</h1>
            </Link>
            <nav>
                {renderLinks()}
            </nav>
        </header>
    )
}

export default Header 
