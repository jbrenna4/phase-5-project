import React, {useReducer, useState} from "react"
import {useHistory, useLocation} from "react-router-dom"
import "./ReservationCard.css"


export default function ReservationCard({user}){

const handleDelete = async () => {
    try {
        const response = await fetch(`/api/reservations/${user.reservations.id}`, {
        method: "DELETE",
        });
        if (!response.ok) {
        throw new Error("Failed to delete reservation");
        }
        //onDelete(); probaby to update the dom...local update
    } catch (error) {
        console.error(error);
    }
    };

const handleEdit = async () => {
    try {
        const response = await fetch(`/api/reservations/${user.reservations.id}`, {
        method: "Patch",
        });
        if (!response.ok) {
        throw new Error("Failed to patch reservation");
        }
        //onDelete(); probaby to update the dom...local update
    } catch (error) {
        console.error(error);
    }
    };


const scheduledTime = user.reservations[0].scheduled_time;
const date = new Date(scheduledTime);
const formattedDate = date.toLocaleDateString();
const formattedTime = date.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
const formattedScheduledTime = `${formattedDate} ${formattedTime}`;
    return(
        <div>
            <h2>Prepare to meet Santa!</h2>
            <img src = "https://assets.rockettes.com/wp-content/uploads/2019/11/RCCS_SantaKids_Horizontal_1.jpg.jpeg"/>
            <p>Your reservation is at our {user.reservations[0].shop.neighborhood} location</p>
            <p>at {formattedScheduledTime}</p>
            <button onClick={handleDelete}>Delete</button>
            <button onClick={handleDelete}>Edit</button>
        </div>

        )
}

