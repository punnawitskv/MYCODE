import { useEffect, useState } from 'react';

const MessageList = () => {
    const [messages, setMessages] = useState([]);

    const handleDeleteById = async (id) => {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/messages/${id}`, {
            method: 'delete',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        if (res.status === 204) {
            window.location.reload();
        }
    };

    useEffect(() => {
        const fetchMessages = async () => {
            let res = await fetch(`${import.meta.env.VITE_API_URL}/messages`, {
                method: 'get',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            res = await res.json();
            setMessages(res);
        };
        fetchMessages();
    }, []);

    return (
        <div className="flex flex-col space-y-2">
            {messages.map((message) => {
                return (
                    <div key={message.id} className="flex flex-row items-center space-x-2">
                        <button
                            className="px-2 py-1 border rounded-lg font-bold text-white bg-red-600 hover:bg-red-500 active:bg-red-600"
                            type="button"
                            onClick={() => {
                                handleDeleteById(message.id);
                            }}
                        >
                            Delete
                        </button>
                        <p>{message.text}</p>
                    </div>
                );
            })}
        </div>
    );
};

export default MessageList;
