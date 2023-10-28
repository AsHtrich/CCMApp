import React from 'react';
import ReactDOM from 'react-dom/client';
import Ash from './ash';
import { UserProvider } from './context/UserContext';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <UserProvider>
     <Ash />
  </UserProvider>
   

);

