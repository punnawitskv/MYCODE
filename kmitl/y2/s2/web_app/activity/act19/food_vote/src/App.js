import React, { useState } from "react";

// FoodCard Component
function FoodCard({ category, name, description, image, votes, onVote, onUnvote }) {
   const getVoteDisplay = (count) => (count === 0 ? "MIN" : count >= 10 ? "MAX" : count);

   return (
      <div className="bg-orange-50 border-2 border-black rounded-2xl shadow-lg p-4 flex flex-col w-full max-w-2xl">
         <div className="flex w-full">
            <div className="flex-grow">
               <h2 className="text-2xl font-bold py-4">{category}</h2>
               <h3 className="text-lg font-semibold py-2">{name}</h3>
               <p className="mt-2 text-sm text-gray-700">{description}</p>
            </div>
            <img src={image} alt={name} className="w-[200px] h-[200px] object-cover" />
         </div>

         <div className="mt-4 flex justify-center items-center space-x-4">
            <button onClick={onVote} className="bg-white border border-black text-black px-3 py-1 hover:bg-slate-100">
               Click to Vote
            </button>
            <span className="flex items-center justify-center w-24 h-12 bg-lime-500 border-2 border-black text-violet-700 text-2xl font-bold rounded-lg">
               {getVoteDisplay(votes)}
            </span>
            <button onClick={onUnvote} className="bg-white border border-black text-black px-3 py-1 hover:bg-slate-100">
               Click to Unvote
            </button>
         </div>
      </div>
   );
}

// Parent Component
function FoodVotingApp() {
   const [votes, setVotes] = useState({ fire_rice: 0, bua_loi: 0 });

   const handleVote = (type) => {
      setVotes((prevVotes) => ({
         ...prevVotes,
         [type]: Math.min(prevVotes[type] + 1, 10),
      }));
   };

   const handleUnvote = (type) => {
      setVotes((prevVotes) => ({
         ...prevVotes,
         [type]: Math.max(prevVotes[type] - 1, 0),
      }));
   };

   return (
      <div className="bg-neutral-500 min-h-screen flex flex-col items-center p-4">
         <h1 className="text-4xl font-bold text-yellow-500 mb-6">โหวตอาหาร</h1>
         <div className="space-y-6">
            <FoodCard
               category="อาหารคาว"
               name="ข้าวผัด"
               description="Lorem ipsum odor amet, consectetuer adipiscing elit. 
               Vulputate platea at rhoncus purus pharetra curae. 
               Viverra malesuada eleifend et augue sapien faucibus vehicula. 
               Luctus dolor suscipit morbi urna accumsan. 
               Volutpat nunc felis luctus placerat auctor. 
               Molestie sapien venenatis suspendisse enim tortor. 
               Iaculis aliquam egestas etiam id cras sodales ullamcorper eleifend."
               image="https://i.postimg.cc/7ZctmTC1/fr.jpg"
               votes={votes.fire_rice}
               onVote={() => handleVote("fire_rice")}
               onUnvote={() => handleUnvote("fire_rice")}
            />
            <FoodCard
               category="อาหารหวาน"
               name="บัวลอย"
               description="Lorem ipsum odor amet, consectetuer adipiscing elit. 
               Eleifend porta fringilla fusce dis dapibus ad. 
               Non facilisi quis facilisi ridiculus viverra mi. 
               Arcu ut placerat iaculis curae primis justo auctor adipiscing. 
               Amet sagittis velit etiam porta senectus felis. 
               Penatibus est curabitur cubilia pulvinar lectus duis blandit vulputate. 
               Nullam in potenti commodo magnis iaculis."
               image="https://i.postimg.cc/9Q4JRFxD/bl.jpg"
               votes={votes.bua_loi}
               onVote={() => handleVote("bua_loi")}
               onUnvote={() => handleUnvote("bua_loi")}
            />
         </div>
      </div>
   );
}

export default FoodVotingApp;
