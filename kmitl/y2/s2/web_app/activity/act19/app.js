import React, { useState } from 'react';

function FoodVotingApp() {
  const [votes, setVotes] = useState({ rice: 0, dessert: 0 });

  const handleVote = (type) => {
    setVotes({ ...votes, [type]: votes[type] + 1 });
  };

  const handleUnvote = (type) => {
    if (votes[type] > 0) {
      setVotes({ ...votes, [type]: votes[type] - 1 });
    }
  };

  return (
    <div className="min-h-screen bg-gray-800 text-gray-100 p-6">
      <h1 className="text-4xl font-bold text-center mb-6 text-yellow-500">โหวตอาหาร</h1>

      <div className="grid gap-6 max-w-3xl mx-auto">
        {/* อาหารคาว */}
        <div className="bg-gray-100 text-gray-900 rounded-2xl p-4 flex items-center gap-4 shadow-lg">
          <img
            src="https://via.placeholder.com/150" // Replace with your image link
            alt="ข้าวผัด"
            className="w-32 h-32 rounded-lg object-cover"
          />
          <div className="flex-1">
            <h2 className="text-2xl font-bold">อาหารคาว</h2>
            <h3 className="text-lg font-semibold text-gray-700">ข้าวผัด</h3>
            <p className="text-sm text-gray-600 mt-2">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ligula nisi, porta luctus elit vitae, faucibus commodo est.
            </p>
            <div className="mt-4 flex items-center gap-4">
              <button
                onClick={() => handleVote('rice')}
                className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600">
                Click to Vote
              </button>
              <span className="bg-green-500 text-white px-4 py-2 rounded-lg">{votes.rice} MIN</span>
              <button
                onClick={() => handleUnvote('rice')}
                className="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600">
                Click to Unvote
              </button>
            </div>
          </div>
        </div>

        {/* อาหารหวาน */}
        <div className="bg-gray-100 text-gray-900 rounded-2xl p-4 flex items-center gap-4 shadow-lg">
          <img
            src="https://via.placeholder.com/150" // Replace with your image link
            alt="บัวลอย"
            className="w-32 h-32 rounded-lg object-cover"
          />
          <div className="flex-1">
            <h2 className="text-2xl font-bold">อาหารหวาน</h2>
            <h3 className="text-lg font-semibold text-gray-700">บัวลอย</h3>
            <p className="text-sm text-gray-600 mt-2">
              Fusce elit massa, pulvinar ac magna molestie, cursus ullamcorper nibh. Quisque ut nibh vel enim viverra tempor quis in nulla.
            </p>
            <div className="mt-4 flex items-center gap-4">
              <button
                onClick={() => handleVote('dessert')}
                className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600">
                Click to Vote
              </button>
              <span className="bg-green-500 text-white px-4 py-2 rounded-lg">{votes.dessert} MIN</span>
              <button
                onClick={() => handleUnvote('dessert')}
                className="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600">
                Click to Unvote
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default FoodVotingApp;
