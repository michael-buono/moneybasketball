import React, { useState, useEffect } from "react";
import { Text, Title } from "@mantine/core";

const Teams = () => {
    // Declare state for the selected team
    const [teams, setTeams] = useState(null);

    useEffect(() => {
        fetch("/api/teams", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "X-Requested-With": "XMLHttpRequest"
            }
        })
            .then((response) => response.json())
            .then((data) => {
                setTeams(data.teams);
            });
    }, []);

    return (
        <>
            <Title size="lg" weight={500}>
                NBA Teams
            </Title>
            <div>{teams && teams.map((team) => <Text key={team}>{team}</Text>)}</div>
        </>
    );
};

export default Teams;
