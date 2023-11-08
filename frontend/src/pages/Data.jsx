import React, { useEffect, useState } from 'react';
import Charts from '../components/Charts'
import Lilo from '../components/Lilo';
import GetSensors from '../components/GetSensors'
import Alarms from './Alarms';
const Data = () => {
  const [page, setPage] = useState(true);
  const [loaded, setLoaded] = useState(false);
  
  
  return (
    <div className='bg-black h-full'>
      <div className='bg-[#f18912] w-full flex justify-between border-y-2 border-black items-center h-[58px]'>
          <h1 className='text-black px-[72px] font-bold text-3xl'>DASHBOARD</h1>
          <div className='flex flex-row '>
            <h1 className='text-black font-semibold px-[64px] py-[32px] text-xl'>User@882003</h1>
            <Lilo></Lilo>
          </div>
      </div>
      <div className='w-full flex flex-col items-center justify-center h-[120px] bg-[#5A5A5A]'>
        <div className=' w-[90%] px-6 pt-6 '>
            <h1 className='font-extrabold text-5xl text-white'>Device: 30082003</h1>
        </div>
        <div className='w-[30%] ml-[70%] flex flex-row pt-2 '>
        <button 
        
        className='border-x-4 border-t-4 hover:border-[#111111] focus:bg-black focus:border-black rounded-md py-1  px-4 text-3xl font-bold text-white '
        onClick={() => setPage(true)}
        >
          Raw Data
        </button>
        <button
        
        className='border-x-4 border-t-4  ml-[-1px] hover:border-[#111111] focus:bg-black focus:border-black rounded-md py-1 px-4 text-3xl font-bold text-white '
        onClick={() => setPage(false)}
        >
          Alarms
        </button>
        
        </div>
      </div>
    
      
        {page ? (
            <GetSensors/>
        ) : (           
          <Alarms/> 
        )}
    
           
     

          
      
    </div>
  );
};

export default Data;
