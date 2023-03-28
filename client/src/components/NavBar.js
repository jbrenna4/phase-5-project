import React from "react";

import { NavLink } from "react-router-dom"

import Users from "./Users"
import Store from "./Store";
import Library from "./Library";
import Community from "./Community";


function NavBar() {

    return (
    <nav className="topnav">
        <ul>
          <li>
            <NavLink exact to="/">Home</NavLink>
          </li>
          <li>
            <NavLink to="/store">Store</NavLink>
          </li>
          <li>
            <NavLink to="/library">Library</NavLink>
          </li>
          <li>
            <NavLink to="/community">Community</NavLink>
          </li>
          <li>
            <NavLink to="/user">Profile</NavLink>
          </li>
          <li>
            <NavLink to="/support">Support</NavLink>
          </li>

        </ul>
    </nav>
  )
}
  
  export default NavBar;