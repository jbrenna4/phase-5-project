import React, {useEffect, useState} from "react"
import {Route, Switch, useHistory} from "react-router-dom"

import NavBar from "./NavBar"
import Header from "./Header"
import Profile from "./Profile"
import Community from "./Community"
import GameStore from "./ShopList"
import GameLibrary from "./GameLibrary"
import Authentication from "./Authentication"
import ShopList from "./ShopList"

export default function App(){
  const [user, setUser] = useState(null)
  const [shops, setShops] = useState([])
  const [workers, setWorkers] = useState([])
  const [searchGenre, setSearchGenre] = useState("")
  const [searchTitle, setSearchTitle] = useState("")

  useEffect(() => {
    fetchUser()
  },[])

  useEffect(() => {
    updateUsers()
  }, [])

  useEffect(() => {
    fetch("/shops")
      .then(r => r.json())
      .then(data => {
        setShops(data)})
  }, [])

  useEffect(() => {
    fetch("/workers")
      .then(r => r.json())
      .then(data => {
        setWorkers(data)})
  }, [])

  const fetchUser = () => {
    fetch('/authorized')
    .then (r => {
      if (r.ok){
        r.json().then(user => setUser (user))
      }else{
        setUser(null)
      }
    })
  }

  const updateUsers = () => {
    fetch("/users", )
    .then(r => r.json())
    .then(data => {
      setUsers(data)})
  }

  const updateUser = user => setUser(user)

  return(
    <main className="app">
      <Header updateUser={updateUser} user={user}/>
      <NavBar user={user}/>
      <Switch>
        <Route exact path="/">
          {useHistory().push('/store')}
        </Route>
        <Route path="/shop">
          <ShopList shops={shops} searchGenre={searchGenre} onChangeGenre={setSearchGenre} searchTitle={searchTitle} onChangedTitle={setSearchTitle} user={user}/>
        </Route>
        {user ? <Route exact path="/library">
          <GameLibrary user={user}/>
        </Route> : null}
        <Route path="/community">
          {users ? <Community users = {users}/> : null}
        </Route>
        <Route exact path="/login">
          <Authentication updateUser={updateUser} updateUsers={updateUsers}/>
        </Route>
        {user ? <Route exact path="/profile">
          <Profile user={user} updateUsers={updateUsers}/>
        </Route> : null}
        <Route path="*">
            <h1>404 not found</h1>
        </Route> 
      </Switch>
    </main>
  )
}