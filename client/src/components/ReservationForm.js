import React, {useState} from "react"
import {useHistory, useLocation} from "react-router-dom"
import "./ReservationForm.css"


export default function ReservationForm({user, updateReservations}){
const [scheduled_time, setScheduledTime] = useState(new Date());
const [shop_id, setShopId] = useState("");
const history = useHistory();

const handleSubmit = (event) => {
    event.preventDefault();
    const reservation = { scheduled_time, shop_id, user_id: user.id };

    fetch("/reservations", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify(reservation),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log("Success:", data);
        updateReservations();
        history.push(`/reservations/${data.id}`);
    })
    // .catch((error) => {
    //     console.error("Error:", error);
    // });
};

const handleShopChange = (event) => {
    setShopId(event.target.value);
};

return (
    <form className="reservation-form" onSubmit={handleSubmit}>
    <h2>Create Reservation</h2>
    <label htmlFor="scheduled_time">Scheduled Time:</label>
    <input
        type="datetime-local"
        id="scheduled_time"
        name="scheduled_time"
        value={scheduled_time}
        onChange={(event) => setScheduledTime(event.target.value)}
        required
    />
    <label htmlFor="shop_id">Select a shop:</label>
    <select id="shop_id" name="shop_id" onChange={handleShopChange} required>
        <option value="">Choose a shop</option>
        <option value="1">Park Slope</option>
        <option value="2">Crown Heights</option>
        <option value="3">Bay Ridge</option>
    </select>
    <button type="submit">Create Reservation</button>
    </form>
);
}