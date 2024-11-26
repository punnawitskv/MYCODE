import MessageForm from './components/MessageForm';
import MessageList from './components/MessageList';

const App = () => {
    return (
        <div className="flex flex-col items-center w-full h-screen">
            <p className="py-10 font-bold text-4xl">System Platform Administration - Web</p>
            <div className="flex flex-row justify-around w-full">
                <div className="w-3/12">
                    <MessageForm />
                </div>
                <div className="w-6/12">
                    <MessageList />
                </div>
            </div>
        </div>
    );
};

export default App;
