import React, { useEffect,useContext } from "react";
import Register from "./components/Register";
import { UserContext } from "./context/UserContext";
import Login from "./components/Login";
import App from "./App";

const Ash = () => {
  const [token] = useContext(UserContext);

  const getWelcomeMessage = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch("/api", requestOptions);
    const data = await response.json();

    if (!response.ok) {
      console.log("Something went wrong with /api boi");
    } else {
      
      console.log(data)
    }
  };
  useEffect(()=> {
    getWelcomeMessage();
  }, []);
  return (
    <>
      <div className="columns">
        <div className="column"></div>
        <div className="column m-5 is-two-thirds">
          {!token ? (
            <div className="columns">
              <Register/> <Login />
            </div>
          ) : (  
            <App/>
          )}
        </div>
        <div className="column"></div>
      </div>
      
    </>
  );
};

export default Ash;
