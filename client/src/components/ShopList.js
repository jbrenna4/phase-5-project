import React from "react"
import {useLocation} from 'react-router-dom'
import "./ShopList.css"

import ShopCard from "./ShopCard"

export default function ShopList({shops, searchGenre, onChangeGenre, onChangedTitle, searchTitle, user}){

  const location = useLocation()

  const handleChangeGenre = event => onChangeGenre(event.target.value)

  const handleChangeTitle = event => onChangedTitle(event.target.value)

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