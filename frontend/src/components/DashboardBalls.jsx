import React from 'react'
const DashboardBalls = () => {
    
    return (
    <div className='bg-black text-[#EEEEEE]'>
        <div className='flex justify-between rounded-full bg-white m-4 mt-4 px-14 py-2'>
            <div className='bg-black cursor-pointer w-[110px] border-4 items-center rounded-full flex flex-col hover:border-[#f18912]  hover:text-[#f18912] border-white px-[100px] p-2'>
                <h1 className='font-bold text-4xl '>63</h1>            
                <p className=' font-semibold text-2xl'>Trips</p>
            </div>
            <div className='bg-black cursor-pointer w-[110px] border-4 items-center rounded-full flex flex-col hover:border-[#f18912] hover:text-[#f18912] border-white px-[100px] p-2'>
                <h1 className='font-bold text-4xl'>63</h1>            
                <p className=' font-semibold text-2xl'>Alarms</p>
            </div>
            <div className='bg-black cursor-pointer w-[110px] border-4 items-center rounded-full flex flex-col hover:border-[#f18912] hover:text-[#f18912] border-white px-[100px] p-2'>
                <h1 className=' font-bold text-4xl'>63</h1>            
                <p className=' font-semibold text-2xl'>Devices</p>
            </div>
        </div>
        <div>

        </div>
    </div>
  )
}

export default DashboardBalls