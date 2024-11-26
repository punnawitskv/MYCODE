import { useState } from 'react';

const MessageForm = () => {
    const [message, setMessage] = useState('');

    const handleSubmit = async () => {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/messages`, {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: message,
            }),
        });
        if (res.status === 201) {
            window.location.reload();
        }
    };

    return (
        <div className="flex flex-col space-y-2">
            <textarea
                className="w-full h-64 p-4 border rounded-lg outline-none"
                style={{ resize: 'none' }}
                name="input-message"
                type="text"
                placeholder="type something here!"
                value={message}
                onChange={(e) => {
                    setMessage(e.target.value);
                }}
            />
            <button className="p-2 border rounded-lg font-bold text-white bg-green-600 hover:bg-green-500 active:bg-green-600" type="button" onClick={handleSubmit}>
                Submit
            </button>
        </div>
    );
};

export default MessageForm;
