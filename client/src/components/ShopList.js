import React from "react"
import {useLocation} from 'react-router-dom'
import "./ShopList.css"

import ShopCard from "./ShopCard"

export default function ShopList({shops}){


    const cards = shops.map((shop) => (
      <ShopCard
        key = {shop.id}
        id = {shop.id}
        neighborhood = {shop.neighborhood}
        img = {shop.img}
        address = {shop.address}
      />
    ))
  
    return (
      <ul className="shop_cards">{cards}</ul>
    );
  }