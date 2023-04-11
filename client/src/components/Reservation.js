import React, {useReducer, useState, useContext} from "react"
import {useHistory, useLocation} from "react-router-dom"
import "./Reservation.css"
import ReservationForm from "./ReservationForm"
import ReservationCard from "./ReservationCard"
import {UserContext} from "./App"

export default function Reservation({reservations, updateReservations}){

const [user] = useContext(UserContext)   
console.log(user)


    if (user && user.reservations && user.reservations.length > 0){
        return(
            <ReservationCard user={user}/>
        )
    } else {
        return(    
        <ReservationForm user = {user} updateReservations = {updateReservations}/>
        )        
    }
}
