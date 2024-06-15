import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Dashboard() {
    const [data, setData] = useState(null);

    useEffect(() => {
        axios.get('/contract/example_address')
            .then(response => setData(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>
            {data ? (
                <div>
                    <p>Market Cap: {data.market_cap}</p>
                    <p>Total Holders: {data.total_holders}</p>
                </div>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}

export default Dashboard;
