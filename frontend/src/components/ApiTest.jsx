import React, { useState, useEffect } from "react";
import { Text } from "@mantine/core";
const ApiTest = () => {
    // Declare state for the selected team
    const [message, setMessage] = useState(null);

    useEffect(() => {
        fetch("/api/test", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "X-Requested-With": "XMLHttpRequest"
            }
        })
            .then((response) => response.json())
            .then((data) => {
                setMessage(data.message);
            });
    }, []);

    return <Text>{message}</Text>;
};

export default ApiTest;
