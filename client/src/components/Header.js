import React from "react"
import {NavLink, useHistory} from "react-router-dom"

export default function Header({updateUser, user}) {
  const history = useHistory()

  const handleLogout = () => {
    fetch('/logout',{
      method: 'DELETE'
    })
    .then(r => {
      if(r.ok){
        updateUser(null)
        history.push('/store')
      }
    })
  }

  return(
    <header className="header">
      <ul>
        <h2 className="logo_text">Santa</h2>
        <img src="https://static.vecteezy.com/system/resources/previews/008/604/918/original/cartoon-santa-claus-carrying-sack-free-vector.jpg" alt="Santa" className="logo"></img>
        <div className="dropdown">
          <button onClick={user ? handleLogout : null} className="dropbtn">
          <NavLink to="/login">{user ? 'Logout' : 'Login'}</NavLink>
            {user ? <>
              {/* <img src={user.img} className="header__image"></img> */}
              <p>{user.name}</p>
            </> : null}
          </button>
        </div>
      </ul>       
    </header>
  )
}