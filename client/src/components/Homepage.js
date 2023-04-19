import React, {useState} from "react"
import {useHistory, useLocation} from "react-router-dom"
import "./Homepage.css"


export default function Homepage(){

    return (
        <div className="homepage">
          <h1 className="homepage_header">Take a Picture with Santa</h1>
          <img className="homepage_image" src="https://images.theconversation.com/files/302306/original/file-20191118-169393-r78x4o.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=900.0&fit=crop" alt="Santa Claus" />
          <p className="homepage_text">
            Welcome to our Christmas Village, where you can take a picture with
            Santa Claus and create cherished memories with your loved ones.
          </p>
        </div>
      );
    }