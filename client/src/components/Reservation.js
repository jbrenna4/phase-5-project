import React, {useReducer, useState} from "react"
import {useHistory, useLocation} from "react-router-dom"
import "./Reservation.css"
import ReservationForm from "./ReservationForm"
import ReservationCard from "./ReservationCard"

export default function Reservation({reservations, user}){

    if (user && user.reservation){
        return(
            <ReservationCard user={user}/>
        )
    } else {
        return(    
        <ReservationForm/>
        )        
    }
}
