import React, {useState} from "react"
import {useHistory, useLocation} from "react-router-dom"
import "./ReservationForm.css"


export default function ReservationForm({shop_id, user_id}){

    const [scheduled_time, setScheduledTime] = useState(new Date())
    const history = useHistory()

    const handleSubmit = (event) => {
        event.preventDefault()
        const reservation = {scheduled_time, shop_id, user_id}

        fetch('/reservations', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(reservation)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            history.push(`/reservations/${data.id}`)
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    return(
        <form className="reservation-form" onSubmit={handleSubmit}>
            <h2>Create Reservation</h2>
            <label htmlFor="scheduled_time">Scheduled Time:</label>
            <input type="datetime-local" id="scheduled_time" name="scheduled_time" value={scheduled_time} onChange={(event) => setScheduledTime(event.target.value)} required/>
            <button type="submit">Create Reservation</button>
        </form>
    )        
}