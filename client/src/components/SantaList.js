import React, {useState} from "react"
import {useHistory, useLocation} from "react-router-dom"
import "./SantaList.css"
import SantaCard from "./SantaCard"

export default function SantaList({workers}){

    const santaWorkers = workers.filter((worker) => worker.role === "santa");
    const cards = santaWorkers.map((worker) => (
        <SantaCard
          key = {worker.id}
          id = {worker.id}
          name = {worker.name}
          img = {worker.img}
          bio = {worker.bio}
          role = {worker.role}
        />
      ))
    
      return (
        <ul className="santa_cards">{cards}</ul>
      );
    }
