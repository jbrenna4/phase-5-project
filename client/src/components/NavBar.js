import React from "react"
import {NavLink} from "react-router-dom"



export default function NavBar({user}){
  // function handleLogoutClick() {
  //   fetch("/logout", { method: "DELETE" }).then((r) => {
  //     if (r.ok) {
  //       setUser(null);
  //     }
  //   });
  // }
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
        {/* <Button variant="outline" onClick={handleLogoutClick}>
          Logout
        </Button> */}
      </ul>
    </nav>
  )
}