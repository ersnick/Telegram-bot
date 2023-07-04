import React, {useState, useEffect} from "react";
import Users from "../components/Users";
import axios from 'axios'


function Students() {

    const [statements, setStatements] = useState([]);


    useEffect(() => {
        const apiUrl = 'http://45.9.42.26:8000/api/statements';
        axios.get(apiUrl).then((resp) => {
            const users = resp.data;
            setStatements(users);
        });
    }, [setStatements]);

    const [filter, setFilter] = useState("all");

    const handleFilterChange = (event) => {
        setFilter(event.target.value);
    };

    const filteredStatements = statements.filter((statement) => {
        if (filter === "all") {
            return true;
        } /*else if (filter === "checked") {
            return statement.is_checked;
        }*/ else if (filter === "unChecked") {
            return !statement.is_checked;
        }
    });

    let handleEdit = function (user) {
        let usersCopy = statements
        usersCopy[user.id] = user
        console.log(statements)
        setStatements(usersCopy)
    }

    return (
        <div>
            <h1>Заявки</h1>
            <input
                type="radio"
                id="all"
                name="choose"
                value="all"
                checked={filter === "all"}
                onChange={handleFilterChange}
            />
            <label htmlFor="all">Все</label>
            {/*<input*/}
            {/*    type="radio"*/}
            {/*    id="checked"*/}
            {/*    name="choose"*/}
            {/*    value="checked"*/}
            {/*    checked={filter === "checked"}*/}
            {/*    onChange={handleFilterChange}*/}
            {/*/>*/}
            {/*<label htmlFor="checked">Принятые</label>*/}
            <input
                type="radio"
                id="unChecked"
                name="choose"
                value="unChecked"
                checked={filter === "unChecked"}
                onChange={handleFilterChange}
            />
            <label htmlFor="unChecked">Ожидают проверки</label>
            <main>
                <Users users={filteredStatements} handleEdit={handleEdit}/>
            </main>
        </div>)
}

export default Students