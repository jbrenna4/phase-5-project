import React, {useState} from "react";

function UserContainer( {user} ) {
  
  const[clicked, setClicked] = useState(false);

  function handleClick() {
    if (clicked == true) {
      setClicked(false);
    }
    else{
        setClicked(true);
    }
  }

  return (
    <li className="cards__item">
      <div className="card">
        <img
          onClick = {handleClick}
          src={user.img}
          alt={user.name}
          className="card__image"
        />
        <div className="card__content">
          <div className="card__title">{user.name}</div>
          <p className="card__text">{clicked ? user.bio : user.user_games}</p>
          <div className="card__detail">
          </div>
        </div>
      </div>
    </li>
  );
}

export default UserContainer;