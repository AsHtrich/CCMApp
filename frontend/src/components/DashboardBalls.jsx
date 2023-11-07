import React from 'react'
const DashboardBalls = () => {
    
    return (
    <div className='bg-[#5A5A5A] text-white'>
        <div className='flex justify-between rounded-full bg-black m-4 mt-6 px-16 py-8'>
            <div className='bg-[#1b72e3] w-[110px] border-2 items-center rounded-full flex flex-col border-white p-4'>
                <h1 className='text-white font-bold text-4xl'>63</h1>            
                <p className='text-white font-semibold text-2xl'>Trips</p>
            </div>
            <div className='bg-[#f54242] w-[110px] border-2 items-center rounded-full flex flex-col border-white p-4'>
                <h1 className='text-black font-bold text-4xl'>63</h1>            
                <p className='text-black font-semibold text-2xl'>Alarms</p>
            </div>
            <div className='bg-white w-[110px] border-4 items-center rounded-full flex flex-col border-white p-4'>
                <h1 className='text-black font-bold text-4xl'>63</h1>            
                <p className='text-black font-semibold text-2xl'>Assets</p>
            </div>
            <div className='bg-[#d9d321] w-[110px] border-2 items-center rounded-full flex flex-col border-white p-4'>
                <h1 className='text-black font-bold text-4xl'>63</h1>            
                <p className='text-black font-semibold text-2xl'>Devices</p>
            </div>
        </div>
        <div>

        </div>
    </div>
  )
}

export default DashboardBalls