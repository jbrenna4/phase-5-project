import React, {useEffect, useReducer, useState} from "react"
import {useHistory, useLocation} from "react-router-dom"
import "./ReservationCard.css"

export default function ReservationCard({user, setRefresh}) {
const history = useHistory();
const [shop, setShop] = useState(null);

useEffect(() => {
    async function fetchShop() {
    try {
        const response = await fetch(`/shops/${user.reservations[0].shop_id}`);
        if (!response.ok) {
        throw new Error("Failed to fetch shop");
        }
        const shopData = await response.json();
        setShop(shopData);
    } catch (error) {
        console.error(error);
    }
    }
    fetchShop();
}, [user.reservations]);

const handleDelete = async () => {
    try {
    const response = await fetch(`/reservations/${user.reservations[0].id}`, {
        method: "DELETE",
    });
    if (!response.ok) {
        throw new Error("Failed to delete reservation");
    }
    history.push("/"); // redirect to the homepage after deleting
    setRefresh(prev => !prev);
    } catch (error) {
    console.error(error);
    }
};

const handleEdit = async () => {
    const newScheduledTime = prompt("Enter new appointment time (YYYY-MM-DD HH:mm:ss):");
    try {
    const response = await fetch(`/reservations/${user.reservations[0].id}`, {
        method: "PATCH",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify({ scheduled_time: newScheduledTime }),
    });
    if (!response.ok) {
        throw new Error("Failed to update reservation");
    }
    const updatedReservation = await response.json();
    console.log("Reservation updated:", updatedReservation);
    setRefresh(prev => !prev);
    history.push("/"); // redirect to the homepage after updating
    } catch (error) {
    console.error(error);
    }
};

const scheduledTime = user.reservations[0].scheduled_time;
const date = new Date(scheduledTime);
const formattedDate = date.toLocaleDateString();
const formattedTime = date.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
const formattedScheduledTime = `${formattedDate} ${formattedTime}`;

return (
    <div>
    <h2>Prepare to meet Santa!</h2>
    <img src="https://assets.rockettes.com/wp-content/uploads/2019/11/RCCS_SantaKids_Horizontal_1.jpg.jpeg"/>
    {shop ? (
        <p>Your reservation is at our {shop.address} location in {shop.neighborhood}</p>
    ) : (
        <p>Loading shop information...</p>
    )}
    <p>at {formattedScheduledTime}</p>
    <button onClick={handleDelete}>Delete</button>
    <button onClick={handleEdit}>Edit</button>
    </div>
);
}