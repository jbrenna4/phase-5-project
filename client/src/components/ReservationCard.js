import React, {useReducer, useState} from "react"
import {useHistory, useLocation} from "react-router-dom"
import "./ReservationCard.css"
import Reservation from "./Reservation"

export default function ReservationCard(user, reservations){

const handleDelete = async () => {
    try {
        const response = await fetch(`/api/reservations/${reservation.id}`, {
        method: "DELETE",
        });
        if (!response.ok) {
        throw new Error("Failed to delete reservation");
        }
        onDelete();
    } catch (error) {
        console.error(error);
    }
    };

    return(
        <div>
            <h2>Prepare to meet Santa!</h2>
            <img src = "https://assets.rockettes.com/wp-content/uploads/2019/11/RCCS_SantaKids_Horizontal_1.jpg.jpeg"> </img>
            <p>Your reservation is at {user.reservation.scheduled_time}</p>
            <button onClick={handleDelete}>Delete</button>
        </div>

        )
}

