import React, { useContext } from "react";
import { UserContext } from "../context/UserContext";

const Lilo = () => {
  const [token, setToken] = useContext(UserContext);

  const handleLogout = () => {
    setToken(null);
  };

  return (
    <div className="text-center m-6">
      {token && (
        <button className="button" onClick={handleLogout}>
          Logout
        </button>
      )}
    </div>
  );
};

export default Lilo;