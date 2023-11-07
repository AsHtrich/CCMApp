import React, { useEffect, useState } from 'react';
import Charts from '../components/Charts'
import Lilo from '../components/Lilo';
import GetSensors from '../components/GetSensors'
const Analytics = () => {
  const [page, setPage] = useState(false);
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
            <h1 className='font-extrabold text-4xl text-white'>Device: 30082003</h1>
        </div>
        <div className='w-[20%] mr-[40%] flex flex-row pt-4 '>
        <button 
        className='border-x-4 mx-4 mr-6 hover:border-[#111111] focus:bg-black focus:border-black  py-1 mt-[4px] px-4 text-xl font-bold text-white '
        onClick={() => setPage(false)}
        >
          Overview
        </button>
        <button 
        className='border-x-4 mx-4 mr-6 hover:border-[#111111] focus:bg-black focus:border-black  py-1 mt-[4px] px-4 text-xl font-bold text-white '
        onClick={() => setPage(true)}
        >
          Raw Data
        </button>
        </div>
      </div>
      {!page ? (
           <Charts/> 
       ) : (           
        <GetSensors/>
       )}

          
      
    </div>
  );
};

export default Analytics;
