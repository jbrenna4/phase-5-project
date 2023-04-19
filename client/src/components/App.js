import React, {useEffect, useState, createContext} from "react"
import {Route, Switch, useHistory} from "react-router-dom"

import NavBar from "./NavBar"
import Header from "./Header"
import Authentication from "./Authentication"
import ShopList from "./ShopList"
import SantaList from "./SantaList"
import Reservation from "./Reservation"
import Homepage from "./Homepage"

export const UserContext = createContext()

export default function App(){
  const [user, setUser] = useState(null)
  const [shops, setShops] = useState([])
  const [workers, setWorkers] = useState([])
  const [reservations, setReservations] = useState([])  
  const [refresh, setRefresh] = useState(false);


  useEffect(() => {
    fetchUser()
  },[, refresh])



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

  useEffect(() => {
    fetch("/reservations")
      .then(r => r.json())
      .then(data => {
        setReservations(data)})
  }, [])

  const fetchUser = () => {
    fetch('/authorized')
    .then (r => {
      if (r.ok){
        r.json().then(user => setUser(user))
      }
    })
  }

  // const updateUsers = () => {
  //   fetch("/users", )
  //   .then(r => r.json())
  //   .then(data => {
  //     setUser(data)})
  // }

  const updateUser = user => setUser(user)

    return(
      <main className="app">
        <UserContext.Provider value = {[user]}>
        <Header updateUser={updateUser} user={user}/>
        <NavBar user={user}/>
        <Switch>
          <Route exact path="/">
            <Homepage/>
          </Route>
          <Route path="/shop">
            <ShopList shops={shops} user={user}/>
          </Route>
          <Route path="/reservation">
            <Reservation reservations = {reservations} updateReservations = {setReservations} user ={user} setRefresh ={setRefresh}/>
          </Route>
          <Route exact path="/login">
            <Authentication updateUser={updateUser}/>
          </Route>
          <Route exact path="/santas">
            <SantaList workers = {workers} updateWorkers = {setWorkers}/>
          </Route>
          <Route path="*">
              <h1>404 not found</h1>
          </Route> 
        </Switch>
        </UserContext.Provider>
      </main>
    )
  }
