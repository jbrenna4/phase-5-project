import React from "react"
import {NavLink} from "react-router-dom"

export default function NavBar({user}){
  return(
    <nav className="topnav">
      <ul>
        <li>
          <NavLink to="/">Homepage</NavLink>
        </li>
        <li>
          <NavLink to="/shop">Shops</NavLink>
        </li>
        <li>
          <NavLink to="/santas">Santas</NavLink>
        </li>
        <li>
          <NavLink to="/reservation">Reservations</NavLink>
        </li>
      </ul>
    </nav>
  )
}