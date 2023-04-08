import React, {useState} from "react"
import {useHistory, useLocation} from "react-router-dom"
import "./ShopCard.css"


export default function ShopCard({id, neighborhood, img, address}){

  return (
    <div className="shopDiv">
    <li className="shop_card">
      <h3 className='shop_name'>{neighborhood}</h3>
      <img 
      src={img} 
      alt={neighborhood}
      //onClick = {handleClick} 
      />
      <p className="address_label">Address: {address}</p>
      <p className="address_label">Phone Number: 555-555-5555</p>
      <p className="address_label">Hours: 7 days a week, 9:00 AM - 7:00 PM</p>
    </li>
    </div>
  );
}