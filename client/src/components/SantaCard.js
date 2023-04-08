import React, {useState} from "react"
import {useHistory, useLocation} from "react-router-dom"
import "./SantaCard.css"


export default function SantaCard({id, name, img, bio}){

    return (
        <div className="santDiv">
        <li className="sant_card">
          <h3 className='santa_name'>{name}</h3>
          <img 
          src={img} 
          alt={name}
          //onClick = {handleClick} 
          />
          <p className="bio_label">Bio: {bio}</p>
        </li>
        </div>
      );
    }