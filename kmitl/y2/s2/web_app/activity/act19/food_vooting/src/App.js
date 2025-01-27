import React, { useState } from "react";

const App = () => {
  const [votes, setVotes] = useState({
    friedRice: false,
    sweetSoup: false,
  });

  const toggleVote = (food) => {
    setVotes((prevVotes) => ({
      ...prevVotes,
      [food]: !prevVotes[food],
    }));
  };

  return (
    <div className="bg-gray-800 min-h-screen flex flex-col items-center p-4">
      <h1 className="text-4xl font-bold text-yellow-500 mb-6">โหวตอาหาร</h1>
      <div className="space-y-6">
        {/* Fried Rice Card */}
        <div className="bg-amber-100 rounded-2xl shadow-lg p-4 flex w-full max-w-2xl">
          <div className="w-1/2">
            <h2 className="text-2xl font-bold">อาหารคาว</h2>
            <h3 className="text-lg font-semibold">ข้าวผัด</h3>
            <p className="mt-2 text-sm text-gray-700">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ligula nisi, porta luctus elit vitae, faucibus commodo est.
            </p>
            <div className="mt-4">
              <button
                onClick={() => toggleVote("friedRice")}
                className={`px-4 py-2 rounded-full font-bold text-white ${
                  votes.friedRice ? "bg-green-500" : "bg-blue-500"
                }`}
              >
                {votes.friedRice ? "MIN" : "Click to Vote"}
              </button>
            </div>
          </div>
          <img
            src="https://via.placeholder.com/150"
            alt="Fried Rice"
            className="w-1/2 h-auto rounded-xl object-cover ml-4"
          />
        </div>

        {/* Sweet Soup Card */}
        <div className="bg-amber-100 rounded-2xl shadow-lg p-4 flex w-full max-w-2xl">
          <div className="w-1/2">
            <h2 className="text-2xl font-bold">อาหารหวาน</h2>
            <h3 className="text-lg font-semibold">บัวลอย</h3>
            <p className="mt-2 text-sm text-gray-700">
              Fusce elit massa, pulvinar ac magna molestie, cursus ullamcorper nibh.
            </p>
            <div className="mt-4">
              <button
                onClick={() => toggleVote("sweetSoup")}
                className={`px-4 py-2 rounded-full font-bold text-white ${
                  votes.sweetSoup ? "bg-green-500" : "bg-blue-500"
                }`}
              >
                {votes.sweetSoup ? "MIN" : "Click to Vote"}
              </button>
            </div>
          </div>
          <img
            src="https://via.placeholder.com/150"
            alt="Sweet Soup"
            className="w-1/2 h-auto rounded-xl object-cover ml-4"
          />
        </div>
      </div>
    </div>
  );
};

export default App;
